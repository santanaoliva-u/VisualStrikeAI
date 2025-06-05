import cv2
import numpy as np

def generate_heatmap(image_path):
    """
    Genera un mapa de calor de saliencia para la imagen dada.
    
    Args:
        image_path (str): Ruta a la imagen.
    
    Returns:
        tuple: (imagen original, mapa de saliencia).
    
    Raises:
        FileNotFoundError: Si la imagen no se puede cargar.
        ValueError: Si falla el cálculo de la saliencia.
        AttributeError: Si el módulo saliency no está disponible.
    """
    # Cargar la imagen
    image = cv2.imread(image_path)
    if image is None:
        raise FileNotFoundError(f"No se pudo cargar la imagen en {image_path}")
    
    # Verificar si el módulo saliency está disponible
    if not hasattr(cv2, 'saliency'):
        raise AttributeError("El módulo 'saliency' no está disponible en OpenCV. Asegúrate de instalar 'opencv-contrib-python'.")
    
    # Convertir a escala de grises
    gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)
    
    # Crear objeto de saliencia
    try:
        saliency = cv2.saliency.StaticSaliencySpectralResidual_create()
        (success, saliency_map) = saliency.computeSaliency(image)
        if not success:
            raise ValueError("Fallo al calcular la saliencia")
        
        # Normalizar el mapa de saliencia (0-255)
        saliency_map = (saliency_map * 255).astype(np.uint8)
        return image, saliency_map
    except AttributeError as e:
        raise AttributeError(f"Error al acceder al módulo de saliencia: {str(e)}. Asegúrate de usar 'opencv-contrib-python'.")
