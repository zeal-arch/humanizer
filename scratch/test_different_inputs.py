import torch
from humanizer.detector import DesklibAIDetectionModel, LOCAL_MODEL_DIR
from transformers import AutoTokenizer

tokenizer = AutoTokenizer.from_pretrained(LOCAL_MODEL_DIR)
model = DesklibAIDetectionModel.from_pretrained(LOCAL_MODEL_DIR)
model.eval()

inputs = [
    "cat dog apple banana",
    "Hello how are you doing today?",
    "asdfasdfasdfasdfasdfasdfasdfasdfasdfasdf",
    "The importance of education cannot be overstated in modern society because it plays a key role in development.",
    "I got up early this morning to walk the dog, and the weather was freezing. I made a quick cup of coffee before heading out the door."
]

for idx, text in enumerate(inputs):
    print(f"\n--- Test {idx+1}: {text[:50]} ---")
    encoded = tokenizer(
        text,
        padding='max_length',
        truncation=True,
        max_length=512,
        return_tensors='pt'
    )
    with torch.no_grad():
        outputs = model(input_ids=encoded['input_ids'], attention_mask=encoded['attention_mask'])
        logits = outputs["logits"]
        prob = torch.sigmoid(logits).item()
        print(f"Logit: {logits.item():.4f}")
        print(f"Probability: {prob:.4f}")
