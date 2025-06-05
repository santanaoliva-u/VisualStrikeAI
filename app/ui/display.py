import matplotlib.pyplot as plt
import cv2
import numpy as np

def show_with_heatmap(image, heatmap):
    """
    Muestra la imagen original y su mapa de calor lado a lado.
    
    Args:
        image: Imagen original en formato BGR (numpy array).
        heatmap: Mapa de calor en escala de grises (numpy array).
    """
    plt.figure(figsize=(10, 5))
    
    # Mostrar imagen original
    plt.subplot(1, 2, 1)
    plt.imshow(cv2.cvtColor(image, cv2.COLOR_BGR2RGB))
    plt.title("Original")
    plt.axis("off")

    # Asegurar que el heatmap sea un array válido
    if not isinstance(heatmap, np.ndarray):
        raise ValueError("El mapa de calor no es un array de NumPy válido")
    
    # Mostrar mapa de calor
    plt.subplot(1, 2, 2)
    plt.imshow(heatmap, cmap='hot')
    plt.title("Heatmap")
    plt.axis("off")
    
    plt.show()

# Modificado por Santana Oliva (@santanaoliva_u, https://github.com/santanaoliva-u)
# Quité los ejes para una visualización más limpia y añadí validación para el heatmap.
