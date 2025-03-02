"""
generar_documentacion.py

Este script genera documentación automática para módulos de la aplicación utilizando pdoc.

Funcionalidad:
- Lista los módulos disponibles en el directorio `app` (excluyendo `__pycache__`).
- Solicita al usuario seleccionar un módulo para documentar.
- Genera la documentación en formato HTML utilizando pdoc.
- Almacena la documentación generada en la carpeta `docs/<nombre_modulo>`.

Requisitos previos:
- Tener instalado `pdoc`. Si no lo tienes, instálalo con:
    pip install pdoc
- Mover este archivo a la raiz del proyecto.

Detalles de implementación:
- Se utiliza `Path` de `pathlib` para manejar rutas de manera compatible con diferentes sistemas operativos.
- Se filtran las carpetas para excluir `__pycache__`.
- Se maneja la selección del usuario con validación de entrada.
- La documentación se guarda en una carpeta específica dentro de `docs/`.

Uso:
    python generar_documentacion.py

Atributos:
- BASE_DIR (Path): Directorio base donde se encuentra el archivo actual.
- modulos (list): Lista de nombres de módulos disponibles en `app`.
- seleccion (str): Entrada del usuario para seleccionar el módulo.
- modulo_seleccionado (str): Nombre del módulo seleccionado.
- output_dir (Path): Ruta de salida para la documentación generada.
"""


import os
import pdoc
from pathlib import Path

BASE_DIR = Path(__file__).resolve().parent

modulos = [f.name for f in (BASE_DIR / "app").iterdir() if f.is_dir() and f.name != '__pycache__']

print("Módulos disponibles para documentar:")
for idx, modulo in enumerate(modulos, start=1):
    print(f"{idx}. {modulo}")

seleccion = input("Seleccione el número del módulo a documentar: ")

try:
    modulo_seleccionado = modulos[int(seleccion) - 1]
except (IndexError, ValueError):
    print("Selección inválida.")
    exit(1)

# Generar la documentación
output_dir = Path(f"docs/{modulo_seleccionado}")
pdoc.pdoc(
    f"app.{modulo_seleccionado}",
    output_directory=output_dir
)

print(f"Documentación generada en: {output_dir.resolve()}")
