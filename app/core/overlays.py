import cv2
import numpy as np

def golden_ratio_overlay(image):
    """Aplica un overlay de proporción áurea."""
    h, w = image.shape[:2]
    phi = (1 + np.sqrt(5)) / 2
    new_w = int(h / phi)
    offset = (w - new_w) // 2
    
    overlay = image.copy()
    cv2.rectangle(overlay, (offset, 0), (offset + new_w, h), (0, 255, 0), 2)
    return overlay

def rule_of_thirds(image):
    """Aplica una cuadrícula de tercios."""
    h, w = image.shape[:2]
    overlay = image.copy()
    for i in range(1, 3):
        cv2.line(overlay, (0, i * h // 3), (w, i * h // 3), (0, 255, 0), 1)
        cv2.line(overlay, (i * w // 3, 0), (i * w // 3, h), (0, 255, 0), 1)
    return overlay

# Modificado por Santana Oliva (@santanaoliva_u, https://github.com/santanaoliva-u)
# Agregué cálculos matemáticos para proporción áurea y tercios.
