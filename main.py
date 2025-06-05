import cv2
from app.ui.cli import app
from app.core.overlays import golden_ratio_overlay, rule_of_thirds
from app.utils.report import generate_pdf_report
from app.core.saliency import generate_heatmap
from app.analysis.text_analysis import analyze_copy_text
from app.analysis.aida import analyze_aida

if __name__ == "__main__":
    # Ejecutar CLI
    app()

    # Ejemplo de uso completo
    path = "assets/ad_sample.jpg"
    try:
        image, heatmap = generate_heatmap(path)
        text, findings = analyze_copy_text(image)
        aida_scores = analyze_aida(text, heatmap, image.shape)
        
        # Guardar heatmap temporal para el reporte
        cv2.imwrite("heatmap_temp.png", heatmap)
        
        # Generar overlays
        golden_image = golden_ratio_overlay(image)
        thirds_image = rule_of_thirds(image)
        
        # Generar reporte
        generate_pdf_report(path, heatmap, text, findings, aida_scores)
        
        print("Análisis completo. Reporte generado en report.pdf")
    except Exception as e:
        print(f"Error: {e}")

# Modificado por Santana Oliva (@santanaoliva_u, https://github.com/santanaoliva-u)
# Integré todas las fases en el main con manejo de errores.
