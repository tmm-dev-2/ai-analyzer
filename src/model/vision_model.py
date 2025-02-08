from transformers import VisionEncoderDecoderModel, ViTImageProcessor
import torch
from PIL import Image

class ChartVisionModel:
    def __init__(self):
        self.model = VisionEncoderDecoderModel.from_pretrained("microsoft/trocr-base-handwritten")
        self.processor = ViTImageProcessor.from_pretrained("microsoft/trocr-base-handwritten")
        self.device = "cuda" if torch.cuda.is_available() else "cpu"
        self.model.to(self.device)
