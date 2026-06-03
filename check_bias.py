from safetensors.torch import load_file
import os

model_dir = r"C:\Users\admin\Desktop\iv sem\project\humanizer_site\models\zeal-humanizer-detector-v1.0"
weights_path = os.path.join(model_dir, "model.safetensors")

try:
    weights = load_file(weights_path)
    bias = weights["classifier.bias"]
    weight = weights["classifier.weight"]
    print(f"Classifier Bias: {bias.item():.4f}")
    print(f"Classifier Weight - Mean: {weight.mean().item():.4f}, Std: {weight.std().item():.4f}")
except Exception as e:
    print(f"Error: {e}")
