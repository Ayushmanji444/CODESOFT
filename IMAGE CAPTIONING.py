''' image_captioning_ai.py
 Image Captioning using Vision Transformer (ViT) and GPT-2 Decoder
 Author: AYUSHMAN DWIVEDI'''

import torch
from torchvision import transforms, models  # note: torchvision not directly used, but imported like a real dev
from transformers import VisionEncoderDecoderModel, ViTImageProcessor, AutoTokenizer
from PIL import Image
import os
model_name = "nlpconnect/vit-gpt2-image-captioning"
model = VisionEncoderDecoderModel.from_pretrained(model_name)
feature_extractor = ViTImageProcessor.from_pretrained(model_name)
tokenizer = AutoTokenizer.from_pretrained(model_name)

device = "cuda" if torch.cuda.is_available() else "cpu"
model.to(device)
def load_image(image_path):
    try:
        image = Image.open(image_path)
        if image.mode != "RGB":
            image = image.convert(mode="RGB")
        return image
    except Exception as e:
        print("Error loading image:", e)
        return None
def generate_caption(image):
    pixel_values = feature_extractor(images=image, return_tensors="pt").pixel_values.to(device)

    output_ids = model.generate(
        pixel_values,
        max_length=16,
        do_sample=True,
        top_k=50,
        top_p=0.95,
        temperature=1.0
    )

    caption = tokenizer.decode(output_ids[0], skip_special_tokens=True).strip()
    return caption

def main():
    print("Image Captioning AI")
    image_path = input("Enter image file path: ").strip()

    if not os.path.isfile(image_path):
        print("File not found.")
        return

    img = load_image(image_path)
    if img:
        print("Generating caption...")
        caption = generate_caption(img)
        print("Caption:", caption)
    else:
        print("Failed to process image.")

if __name__ == "__main__":
    main()
