import re
import argparse
from pathlib import Path

# Función para leer archivos .tex
def read(path):
    print(f"Archivo: {path.name}:")
    try:
        return path.read_text()
    except Exception as e:
        print(f"  Error al abrir {path.name}: {e}")
        return None

# Función para obtener la línea en la que se encuentra el error
def get_line(index, text):
    lines = text.splitlines()
    char_count = 0
    for i, line in enumerate(lines, start=1):
        char_count += len(line) + 1  # +1 for the newline character
        if index <= char_count:
            return i

# Función para revisar si hay errores en el emparejamiento de begin-end
def check(text):
    rx = re.compile(r'\\(begin|end)\{(.+?)\}')
    matches = list(rx.finditer(text))
    stack = []  # Pila para almacenar entornos
    errores = []  # Lista para almacenar mensajes de error

    for match in matches:
        tag, env = match.groups()
        ini, fin = match.span()
        line = f"  Línea {get_line(fin, text)}:"
        mark = text[ini:fin]

        if tag == "begin":
            stack.append((env, line, mark))  # Añadir el entorno a la pila
        else:
            if stack and stack[-1][0] == env:
                stack.pop()  # Si coincide el begin y end, eliminar de la pila
            else:
                errores.append(f"{line} Falta 'begin' para {mark}")

    while stack:
        env, line, mark = stack.pop()
        errores.append(f"{line} Falta 'end' para {mark}")

    if errores:
        for error in errores:
            print(error)
    else:
        print("No se encontraron errores.")

# Función para procesar todos los archivos .tex en el directorio
def procesar_archivos(directorio):
    archivos_tex = list(Path(directorio).rglob("*.tex"))  # Buscar archivos .tex en directorios y subdirectorios
    if not archivos_tex:
        print(f"No se encontraron archivos .tex en {directorio}")
        return

    for path in archivos_tex:
        text = read(path)
        if text:
            check(text)

# Función para procesar el archivo principal y también todos los archivos .tex en el directorio y subdirectorios
def procesar_proyecto(archivo):
    # Procesar el archivo principal
    text = read(archivo)
    if text:
        check(text)

    # Procesar todos los archivos en el directorio del archivo principal
    directorio = archivo.parent
    print(f"\nBuscando en otros archivos .tex en el directorio: {directorio}\n")
    procesar_archivos(directorio)

if __name__ == "__main__":
    cli = argparse.ArgumentParser()
    cli.add_argument("archivo", type=Path, help="Archivo .tex para analizar")
    args = cli.parse_args()

    if args.archivo.is_file() and args.archivo.suffix == '.tex':
        procesar_proyecto(args.archivo)
    else:
        print(f"{args.archivo} no es un archivo .tex válido.")
