import torch
from humanizer.detector import DesklibAIDetectionModel, LOCAL_MODEL_DIR
from transformers import AutoTokenizer

tokenizer = AutoTokenizer.from_pretrained(LOCAL_MODEL_DIR)
model = DesklibAIDetectionModel.from_pretrained(LOCAL_MODEL_DIR)
model.eval()

sample_human = "I got up early this morning to walk the dog, and the weather was freezing. I made a quick cup of coffee before heading out the door. The streets were completely empty, except for one guy sweeping the sidewalk in front of the bakery. It was peaceful, but I couldn't wait to get back inside and warm up."

for ml in [512, 768]:
    print(f"\n--- Testing Human Sample with max_length={ml} ---")
    encoded = tokenizer(
        sample_human,
        padding='max_length',
        truncation=True,
        max_length=ml,
        return_tensors='pt'
    )
    with torch.no_grad():
        outputs = model(input_ids=encoded['input_ids'], attention_mask=encoded['attention_mask'])
        logits = outputs["logits"]
        prob = torch.sigmoid(logits).item()
        print(f"Logit: {logits.item():.4f}")
        print(f"Probability: {prob:.4f}")
