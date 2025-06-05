import pytesseract
import re

def analyze_copy_text(image):
    """Extrae y analiza el texto de la imagen con OCR."""
    text = pytesseract.image_to_string(image)
    if not text.strip():
        return "No se detectó texto", {"score": 0, "too_long": False, "has_cta": False}
    
    findings = {
        "too_long": len(text.split()) > 25,
        "has_cta": bool(re.search(r"(compra|haz clic|suscríbete|descubre|prueba)", text.lower())),
        "score": 100
    }
    if findings["too_long"]:
        findings["score"] -= 30
    if not findings["has_cta"]:
        findings["score"] -= 20
    return text, findings

# Modificado por Santana Oliva (@santanaoliva_u, https://github.com/santanaoliva-u)
# Añadí manejo para imágenes sin texto detectable.
