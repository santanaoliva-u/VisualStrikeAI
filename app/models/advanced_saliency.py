import torch
import torchvision.transforms as T
from torchvision.models import resnet50
import cv2
import numpy as np

class SimpleSalicon:
    """Modelo básico inspirado en Salicon usando ResNet50."""
    def __init__(self):
        self.model = resnet50(pretrained=True)
        self.model.eval()
        self.transform = T.Compose([T.ToTensor(), T.Normalize(mean=[0.485, 0.456, 0.406], std=[0.229, 0.224, 0.225])])

    def predict(self, image_path: str):
        image = cv2.imread(image_path)
        if image is None:
            raise FileNotFoundError(f"No se pudo cargar la imagen en {image_path}")
        image_rgb = cv2.cvtColor(image, cv2.COLOR_BGR2RGB)
        input_tensor = self.transform(image_rgb).unsqueeze(0)
        with torch.no_grad():
            output = self.model(input_tensor)
        saliency_map = torch.sigmoid(output).squeeze().numpy()
        heatmap = cv2.resize(saliency_map, (image.shape[1], image.shape[0]))
        heatmap = (heatmap * 255).astype("uint8")
        return image, heatmap

# Modificado por Santana Oliva (@santanaoliva_u, https://github.com/santanaoliva-u)
# Implementé un modelo básico de saliencia con ResNet50 para Fase 2.
