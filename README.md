

````markdown
# VisualStrikeAI

![Python](https://img.shields.io/badge/Python-3.8%2B-blue)
![License](https://img.shields.io/badge/License-MIT-green)
![Version](https://img.shields.io/badge/Version-1.0.0-brightgreen)
![Contributions](https://img.shields.io/badge/Contributions-Welcome-orange)

> **VisualStrikeAI** es una herramienta avanzada para el análisis visual de imágenes, diseñada para optimizar composiciones publicitarias y decisiones de diseño a través de mapas de saliencia, overlays inteligentes y reportes automatizados.  
> Ideal para profesionales del marketing, diseño gráfico y UX/UI.

---

## ✨ Características principales

- 🔍 **Mapas de saliencia visual**: Detecta automáticamente las zonas que captan mayor atención en una imagen.
- 🧠 **Overlays de composición**: Añade guías visuales como la proporción áurea o la regla de los tercios.
- 📄 **Reportes profesionales**: Generación de PDFs con análisis, imágenes procesadas y texto personalizado (resumen, análisis, AIDA).
- ⚙️ **CLI interactiva con estilo**: Interfaz enriquecida con `rich` y `typer` para una experiencia moderna desde terminal.
- 🧩 **Arquitectura modular**: Facilita la extensión con nuevos algoritmos o funciones.

---

## 📚 Tabla de contenidos

- [Instalación](#instalación)
- [Uso](#uso)
- [Ejemplo](#ejemplo)
- [Estructura del proyecto](#estructura-del-proyecto)
- [Dependencias](#dependencias)
- [Contribución](#contribución)
- [Licencia](#licencia)
- [Contacto](#contacto)

---

## 🚀 Instalación

### 🔧 Prerrequisitos

- Python 3.8 o superior
- Git
- Recomendado: entorno virtual (`venv`, `virtualenv`, `pyenv`)

### 📥 Clonar el repositorio

```bash
git clone https://github.com/tu_usuario/VisualStrikeAI.git
cd VisualStrikeAI
````

### 🛠️ Crear entorno virtual

```bash
python -m venv VSI_env
source VSI_env/bin/activate  # Windows: VSI_env\Scripts\activate
```

### 📦 Instalar dependencias

```bash
pip install --upgrade pip
pip install -r requirements.txt
```

### 🐧 Dependencias para Arch Linux

```bash
sudo pacman -S libpng libjpeg-turbo
bash requirements_archlinux.sh
```

### ✅ Verificar instalación

```bash
python main.py --help
```

---

## ⚙️ Uso

### Comando básico

```bash
python main.py path/to/image.png --overlay golden
```

### Opciones disponibles

| Opción      | Descripción                                         | Valor por defecto |
| ----------- | --------------------------------------------------- | ----------------- |
| `--overlay` | Overlay de composición (`golden`, `thirds`, `none`) | `none`            |
| `--report`  | Genera un reporte en PDF (`True`, `False`)          | `False`           |
| `--help`    | Muestra la ayuda del comando                        |                   |

### Flujo interactivo

Si no se indican argumentos, se ejecuta un flujo asistido:

* Selección del overlay
* Confirmación de generación del PDF
* Entrada de texto para resumen, análisis y fórmula AIDA
* Visualización y generación del reporte

---

## 📸 Ejemplo

```bash
python main.py images/sample.png --overlay golden --report
```

### Salida esperada:

```text
📜 ¿Quieres un reporte en PDF? [y/N]: y
✍️ Ingresa un resumen general para el reporte:
"Análisis de una imagen publicitaria para evaluar impacto visual."
✍️ Ingresa el texto del análisis:
"El mapa de calor resalta áreas centrales de atención."
✍️ Ingresa el texto AIDA:
"Atención captada por el diseño; interés por colores vivos..."
```

* Se mostrarán imágenes procesadas
* Se generará `report.pdf` con contenido visual + textual

---

## 🧱 Estructura del proyecto

```
VisualStrikeAI/
├── app/
│   ├── analysis/           # Módulos para resumen, análisis, AIDA
│   ├── core/               # Lógica principal de saliencia y overlays
│   ├── models/             # Modelos de saliencia (clásicos o IA)
│   ├── ui/                 # Interfaz CLI y visualización
│   └── utils/              # Generación de reportes y utilidades
├── main.py                 # Punto de entrada del programa
├── requirements.txt        # Dependencias Python
├── requirements_archlinux.sh  # Instala libs en Arch
├── LICENSE
├── README.md
└── .gitignore
```

---

## 📦 Dependencias principales

| Librería                | Uso principal                     |
| ----------------------- | --------------------------------- |
| `opencv-contrib-python` | Procesamiento de imágenes         |
| `matplotlib`            | Visualización de datos e imágenes |
| `typer`                 | CLI moderna y tipada              |
| `rich`                  | Interfaz enriquecida en terminal  |
| `reportlab`             | Generación avanzada de PDF        |

> 📄 Ver `requirements.txt` para versiones específicas.

---

## 🤝 Contribución

¡Las contribuciones son bienvenidas!

1. Haz un fork del repositorio
2. Crea una rama (`feature/nueva-funcionalidad`)
3. Realiza tus cambios y haz commit
4. Push a tu fork y abre un Pull Request

```bash
git checkout -b feature/mi-mejora
git commit -m "Implementar nueva funcionalidad X"
git push origin feature/mi-mejora
```

🔒 Sigue el [Código de Conducta](CODE_OF_CONDUCT.md)

---

## 📜 Licencia

Distribuido bajo licencia MIT.
Consulta el archivo [LICENSE](LICENSE) para más detalles.

---

## 📬 Contacto

* 📧 [support@visualstrikeai.com](mailto:support@visualstrikeai.com)
* 🐛 [GitHub Issues](https://github.com/tu_usuario/VisualStrikeAI/issues)
* 🌐 Sitio web: *visualstrikeai.com* (próximamente)

---

**VisualStrikeAI** — Potenciando decisiones visuales con tecnología de vanguardia.
© 2025 VisualStrikeAI. Todos los derechos reservados.

```

