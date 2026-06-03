import os
import torch
import torch.nn as nn
from transformers import AutoTokenizer, AutoConfig, AutoModel, PreTrainedModel, Trainer, TrainingArguments
from datasets import load_dataset
from peft import get_peft_model, LoraConfig, TaskType

# 1. Define the custom model class (same as in humanizer/detector.py)
class DesklibAIDetectionModel(PreTrainedModel):
    config_class = AutoConfig

    def __init__(self, config):
        super().__init__(config)
        self.model = AutoModel.from_config(config)
        self.classifier = nn.Linear(config.hidden_size, 1)
        self.post_init()

    def forward(self, input_ids, attention_mask=None, labels=None, **kwargs):
        outputs = self.model(input_ids, attention_mask=attention_mask)
        last_hidden_state = outputs[0]
        input_mask_expanded = attention_mask.unsqueeze(-1).expand(last_hidden_state.size()).float()
        sum_embeddings = torch.sum(last_hidden_state * input_mask_expanded, dim=1)
        sum_mask = torch.clamp(input_mask_expanded.sum(dim=1), min=1e-9)
        pooled_output = sum_embeddings / sum_mask

        logits = self.classifier(pooled_output)
        loss = None
        if labels is not None:
            loss_fct = nn.BCEWithLogitsLoss()
            loss = loss_fct(logits.view(-1), labels.float())

        output = {"logits": logits}
        if loss is not None:
            output["loss"] = loss
        return output

def main():
    model_path = os.path.abspath(os.path.join("models", "zeal-humanizer-detector-v1.0"))
    data_path = os.path.join("data", "wikipedia_ai_dataset.jsonl")
    
    print(f"Loading tokenizer and model from {model_path}...")
    tokenizer = AutoTokenizer.from_pretrained(model_path)
    model = DesklibAIDetectionModel.from_pretrained(model_path)
    
    # Enable gradient checkpointing for memory efficiency
    if hasattr(model.model, "gradient_checkpointing_enable"):
        model.model.gradient_checkpointing_enable()

    # 2. Setup LoRA
    # DeBERTa attention layers are typically named 'query_proj', 'value_proj'
    peft_config = LoraConfig(
        task_type=TaskType.SEQ_CLS,
        inference_mode=False,
        r=8,
        lora_alpha=16,
        lora_dropout=0.1,
        target_modules=["query_proj", "value_proj"]
    )
    
    # We must explicitly wrap the inner model or let PEFT handle it
    # We might need to adjust target_modules for DeBERTa. Often it's just "query_proj", "value_proj"
    model = get_peft_model(model, peft_config)
    model.print_trainable_parameters()

    # 3. Load dataset
    print(f"Loading dataset from {data_path}...")
    dataset = load_dataset("json", data_files={"train": data_path})["train"]

    def tokenize_function(examples):
        # We need input_ids, attention_mask, and labels
        tokenized = tokenizer(
            examples["text"], 
            padding="max_length", 
            truncation=True, 
            max_length=512
        )
        tokenized["labels"] = [float(l) for l in examples["label"]]
        return tokenized

    tokenized_datasets = dataset.map(tokenize_function, batched=True)
    
    # Split train/eval
    split = tokenized_datasets.train_test_split(test_size=0.1, seed=42)
    train_dataset = split["train"]
    eval_dataset = split["test"]

    # 4. Training Arguments
    training_args = TrainingArguments(
        output_dir="./detector_finetuned",
        learning_rate=2e-4,
        per_device_train_batch_size=1,        # Minimal memory footprint
        gradient_accumulation_steps=4,        # Simulates batch size of 4
        per_device_eval_batch_size=1,
        num_train_epochs=3,
        weight_decay=0.01,
        eval_strategy="epoch",
        save_strategy="epoch",
        logging_steps=10,
        fp16=torch.cuda.is_available(),       # Must use FP16 on 4GB GPU
        push_to_hub=False,
    )

    trainer = Trainer(
        model=model,
        args=training_args,
        train_dataset=train_dataset,
        eval_dataset=eval_dataset,
    )

    print("Starting fine-tuning...")
    trainer.train()
    
    print("Fine-tuning complete. Saving model...")
    # Save the un-wrapped model weights to the original directory
    merged_model = model.merge_and_unload()
    merged_model.save_pretrained(model_path)
    tokenizer.save_pretrained(model_path)
    print(f"Model saved back to {model_path}")

if __name__ == "__main__":
    main()
