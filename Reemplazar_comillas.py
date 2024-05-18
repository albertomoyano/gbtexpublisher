import sys
import re

def process_tex_file(filename):
    regex_replacements = [
        (r'``', r'\\enquote{'),
        (r'«', r'\\enquote{'),
        (r'\"<', r'\\enquote{'),
        (r'\">', r'}'),
        (r"''", r'}'),
        (r'»', r'}'),
        (r' "', r' \\enquote{'),
        (r'"', r'}')
    ]

    # Leer el contenido del archivo
    with open(filename, 'r') as file:
        content = file.read()

    # Aplicar las sustituciones
    for pattern, replacement in regex_replacements:
        content = re.sub(pattern, replacement, content)

    # Escribir el contenido modificado de vuelta al archivo
    with open(filename, 'w') as file:
        file.write(content)

def main():
    if len(sys.argv) != 2:
        print("Uso: python script.py archivo.tex")
        sys.exit(1)

    filename = sys.argv[1]
    process_tex_file(filename)

if __name__ == "__main__":
    main()
