import typer
from rich.console import Console
from rich.table import Table
from rich.panel import Panel
from rich.progress import track
from rich.text import Text
from rich.box import DOUBLE
import cv2
import os
import tempfile
import time
from app.core.saliency import generate_heatmap
from app.core.overlays import golden_ratio_overlay, rule_of_thirds
from app.ui.display import show_with_heatmap
from app.utils.report import generate_pdf_report

app = typer.Typer()
console = Console()

# Banner de bienvenida con arte ASCII
def print_welcome():
    banner = Text("✨ VisualStrikeAI ✨\n", style="bold magenta")
    banner.append("Analiza tus imágenes con estilo\n", style="italic cyan")
    console.print(Panel(banner, box=DOUBLE, border_style="green", padding=(1, 2)))
    console.print("📸 Preparado para hacer magia visual...\n", style="yellow")

# Mensaje de despedida decorado
def print_goodbye():
    console.print("\n🎉 [bold green]¡Análisis Completado![/bold green] 🎉")
    console.print("Gracias por usar VisualStrikeAI 🌟 ¡Vuelve pronto!", style="cyan")
    console.print("➤" * 40, style="dim green")

# Separador decorativo
def print_separator(title):
    console.print(f"\n[bold magenta]➤➤➤ {title} ➤➤➤[/bold magenta]\n")

@app.command()
def analyze(
    image_path: str = typer.Argument(..., help="Ruta a la imagen a analizar"),
    overlay: str = typer.Option("none", help="Overlay: golden, thirds, none"),
    report: bool = typer.Option(False, help="Generar reporte en PDF")
):
    """
    Analiza una imagen con un CLI decorado al máximo, lleno de estilo y color.
    
    Args:
        image_path: Ruta de la imagen a analizar.
        overlay: Tipo de overlay (golden, thirds, none).
        report: Generar o no un reporte en PDF.
    """
    print_welcome()

    # Interacción con el usuario
    print_separator("Configuración")
    if overlay == "none":
        console.print("🎨 ¿Qué overlay prefieres?", style="yellow")
        overlay = typer.prompt("Opciones: golden/thirds/none", default="none")
    if not report:
        console.print("📜 ¿Quieres un reporte en PDF?", style="yellow")
        report = typer.confirm("Sí o No", default=False)

    # Cargar imagen con barra de progreso
    print_separator("Cargando Imagen")
    console.print("🔍 [cyan]Cargando tu imagen...[/cyan]")
    for _ in track(range(100), description="📥 Procesando...", style="green"):
        time.sleep(0.01)  # Simulación
    image = cv2.imread(image_path)
    if image is None:
        console.print(f"[red]❌ Error: No se pudo cargar {image_path}[/red]")
        raise typer.Exit()

    # Generar heatmap con progreso
    print_separator("Análisis de Saliencia")
    console.print("🧠 [cyan]Generando mapa de calor...[/cyan]")
    for _ in track(range(100), description="🔥 Analizando...", style="magenta"):
        time.sleep(0.01)  # Simulación
    _, heatmap = generate_heatmap(image_path)

    # Aplicar overlay
    print_separator("Aplicando Overlay")
    image_with_overlay = image
    if overlay == "golden":
        image_with_overlay = golden_ratio_overlay(image)
        console.print("🌟 [green]Overlay de proporción áurea aplicado[/green]")
    elif overlay == "thirds":
        image_with_overlay = rule_of_thirds(image)
        console.print("📐 [green]Overlay de regla de los tercios aplicado[/green]")
    else:
        console.print("⭕ [dim]Sin overlay aplicado[/dim]")

    # Mostrar imagen
    show_with_heatmap(image_with_overlay, heatmap)
    console.print("🖼️ [cyan]Mostrando resultado con estilo...[/cyan]")

    # Generar reporte si se solicita
    if report:
        print_separator("Generando Reporte")
        console.print("📝 [yellow]Creando tu reporte en PDF...[/yellow]")
        with tempfile.NamedTemporaryFile(suffix=".png", delete=False) as tmp:
            cv2.imwrite(tmp.name, heatmap)
            heatmap_path = tmp.name
        images = [image_path, heatmap_path]
        if overlay != "none":
            with tempfile.NamedTemporaryFile(suffix=".png", delete=False) as tmp:
                cv2.imwrite(tmp.name, image_with_overlay)
                images.append(tmp.name)
        generate_pdf_report(images, "Texto de ejemplo", "Análisis de ejemplo", "AIDA de ejemplo")
        console.print("✅ [green]Reporte guardado como report.pdf[/green]")

    # Resumen final en tabla estilizada
    print_separator("Resumen Final")
    table = Table(title="📊 Resultados del Análisis", box=DOUBLE, style="cyan")
    table.add_column("🔑 Aspecto", justify="center", style="bold yellow")
    table.add_column("✨ Resultado", justify="center", style="bold green")
    table.add_row("Imagen", image_path)
    table.add_row("Overlay", overlay if overlay != "none" else "Ninguno")
    table.add_row("Reporte", "Sí" if report else "No")
    console.print(table)

    print_goodbye()

if __name__ == "__main__":
    app()
