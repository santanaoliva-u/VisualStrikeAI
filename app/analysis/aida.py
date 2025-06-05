def analyze_aida(text, heatmap, image_shape):
    """Análisis AIDA básico basado en texto y heatmap."""
    h, w = image_shape[:2]
    heatmap_intensity = np.mean(heatmap) / 255.0
    attention_score = min(100, int(heatmap_intensity * 100))
    interest_score = 50 if len(text.split()) > 10 else 20
    desire_score = 70 if "beneficio" in text.lower() else 30
    action_score = 80 if bool(re.search(r"(compra|haz clic)", text.lower())) else 40
    
    return {
        "Attention": attention_score,
        "Interest": interest_score,
        "Desire": desire_score,
        "Action": action_score,
        "Total": (attention_score + interest_score + desire_score + action_score) // 4
    }

# Modificado por Santana Oliva (@santanaoliva_u, https://github.com/santanaoliva-u)
# Añadí un análisis AIDA preliminar basado en intensidad del heatmap y texto.
