import os, sys
import torch

models_dir = os.path.abspath(os.path.join(os.path.dirname(os.path.abspath(__file__)), '..', 'models'))
LOCAL_MODEL_DIR = os.path.join(models_dir, 'zeal-humanizer-detector-v1.0')
model_path = os.path.join(LOCAL_MODEL_DIR, 'model.safetensors')

if not os.path.exists(model_path):
    # Try .bin file
    model_path = os.path.join(LOCAL_MODEL_DIR, 'pytorch_model.bin')

print(f"Loading weights from {model_path}...")
if model_path.endswith('.safetensors'):
    from safetensors.torch import load_file
    state_dict = load_file(model_path)
else:
    state_dict = torch.load(model_path, map_location='cpu')

print("\nFirst 20 keys in state dict:")
for i, key in enumerate(list(state_dict.keys())[:20]):
    print(f"  {key}")

print(f"\nTotal keys: {len(state_dict.keys())}")

# Let's check what classifier keys are there
print("\nClassifier keys:")
for key in state_dict.keys():
    if 'classifier' in key or 'linear' in key:
        print(f"  {key}")
