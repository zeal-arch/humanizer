from safetensors.torch import load_file
import os

model_dir = r"C:\Users\admin\Desktop\iv sem\project\humanizer_site\models\zeal-humanizer-detector-v1.0"
weights_path = os.path.join(model_dir, "model.safetensors")

print("Loading safetensors keys (filtered out encoder layers)...")
try:
    weights = load_file(weights_path)
    for k in sorted(weights.keys()):
        if not k.startswith("model.encoder.layer."):
            print(f"Key: {k}, Shape: {list(weights[k].shape)}")
except Exception as e:
    print(f"Error: {e}")
