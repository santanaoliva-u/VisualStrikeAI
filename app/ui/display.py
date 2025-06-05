import matplotlib.pyplot as plt
import cv2

def show_with_heatmap(image, heatmap):
    """Muestra la imagen original y su mapa de calor lado a lado."""
    plt.figure(figsize=(10, 5))
    plt.subplot(1, 2, 1)
    plt.imshow(cv2.cvtColor(image, cv2.COLOR_BGR2RGB))
    plt.title("Original")
    plt.axis("off")

    plt.subplot(1, 2, 2)
    plt.imshow(heatmap, cmap='hot')
    plt.title("Heatmap")
    plt.axis("off")
    plt.show()

# Modificado por Santana Oliva (@santanaoliva_u, https://github.com/santanaoliva-u)
# Quité los ejes para una visualización más limpia.
