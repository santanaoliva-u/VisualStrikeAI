from reportlab.lib.pagesizes import letter
from reportlab.lib import colors
from reportlab.platypus import SimpleDocTemplate, Paragraph, Spacer, Image, PageBreak
from reportlab.lib.styles import getSampleStyleSheet, ParagraphStyle
from reportlab.lib.units import inch
from reportlab.pdfgen import canvas
import os
from datetime import datetime

def generate_pdf_report(image_paths, text_content, analysis_content, aida_content, output_filename="report.pdf"):
    """
    Genera un reporte en PDF profesional con imágenes y contenido estructurado.
    
    Args:
        image_paths (list): Lista de rutas a las imágenes a incluir.
        text_content (str): Texto general del reporte.
        analysis_content (str): Texto del análisis.
        aida_content (str): Texto AIDA.
        output_filename (str): Nombre del archivo PDF de salida.
    
    Raises:
        FileNotFoundError: Si alguna imagen no se puede cargar.
        Exception: Si falla la generación del PDF.
    """
    try:
        # Crear el documento PDF
        doc = SimpleDocTemplate(output_filename, pagesize=letter, rightMargin=0.75*inch, leftMargin=0.75*inch, 
                               topMargin=1*inch, bottomMargin=0.75*inch)
        story = []
        styles = getSampleStyleSheet()

        # Estilos personalizados
        title_style = ParagraphStyle(
            name='TitleCustom',
            parent=styles['Title'],
            fontSize=18,
            spaceAfter=12,
            textColor=colors.darkblue
        )
        heading_style = ParagraphStyle(
            name='HeadingCustom',
            parent=styles['Heading2'],
            fontSize=14,
            spaceAfter=8,
            textColor=colors.black
        )
        body_style = ParagraphStyle(
            name='BodyCustom',
            parent=styles['BodyText'],
            fontSize=12,
            spaceAfter=6,
            leading=14
        )

        # Encabezado
        story.append(Paragraph("VisualStrikeAI - Reporte de Análisis de Imagen", title_style))
        story.append(Spacer(1, 0.2*inch))

        # Información del reporte
        story.append(Paragraph(f"Fecha: {datetime.now().strftime('%Y-%m-%d %H:%M:%S')}", body_style))
        story.append(Spacer(1, 0.1*inch))

        # Sección: Texto General
        story.append(Paragraph("Resumen General", heading_style))
        story.append(Paragraph(text_content or "Análisis de la imagen proporcionada para identificar áreas de interés visual.", body_style))
        story.append(Spacer(1, 0.2*inch))

        # Sección: Análisis
        story.append(Paragraph("Análisis de Saliencia", heading_style))
        story.append(Paragraph(
            analysis_content or "El mapa de calor generado destaca las áreas de mayor atención visual en la imagen, "
            "basado en el algoritmo de saliencia espectral residual. Las regiones más brillantes indican mayor interés visual.",
            body_style
        ))
        story.append(Spacer(1, 0.2*inch))

        # Sección: AIDA
        story.append(Paragraph("Modelo AIDA", heading_style))
        story.append(Paragraph(
            aida_content or "AIDA (Atención, Interés, Deseo, Acción): Este análisis sugiere cómo las áreas resaltadas "
            "pueden influir en la atención del espectador, generando interés y motivando acciones específicas.",
            body_style
        ))
        story.append(Spacer(1, 0.2*inch))

        # Sección: Imágenes
        story.append(Paragraph("Imágenes del Análisis", heading_style))
        for i, image_path in enumerate(image_paths):
            if not os.path.exists(image_path):
                raise FileNotFoundError(f"No se pudo encontrar la imagen: {image_path}")
            # Etiquetas para las imágenes
            labels = ["Imagen Original", "Mapa de Calor de Saliencia", "Imagen con Overlay de Proporción Áurea"]
            story.append(Paragraph(labels[i] if i < len(labels) else f"Imagen {i+1}", body_style))
            img = Image(image_path, width=4*inch, height=3*inch, kind='proportional')
            story.append(img)
            story.append(Spacer(1, 0.1*inch))

        # Función para agregar encabezado y pie de página
        def add_header_footer(canvas, doc):
            canvas.saveState()
            # Encabezado
            canvas.setFont("Helvetica-Bold", 12)
            canvas.setFillColor(colors.darkblue)
            canvas.drawString(0.75*inch, doc.pagesize[1] - 0.5*inch, "VisualStrikeAI")
            # Pie de página
            canvas.setFont("Helvetica", 10)
            canvas.setFillColor(colors.grey)
            page_num = canvas.getPageNumber()
            canvas.drawString(0.75*inch, 0.5*inch, f"Página {page_num} | {datetime.now().strftime('%Y-%m-%d')}")
            canvas.restoreState()

        # Construir el PDF
        doc.build(story, onFirstPage=add_header_footer, onLaterPages=add_header_footer)
    except Exception as e:
        raise Exception(f"Error al generar el PDF: {str(e)}")
