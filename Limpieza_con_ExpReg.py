import sys
import re

def process_tex_file(filename):
    # Expresiones regulares equivalentes a las utilizadas en sed
    regex_patterns = [
        (r'\\colorbox{[^}]*}{([^}]*)}', r'\1'),
        (r'\\Calibri{([^}]*)}', ''),
        (r'\\textup{([^}]*)}', r'\1'),
        (r'\\textnormal{([^}]*)}', r'\1'),
        (r'\\textcolor{[^}]*}{([^}]*)}', r'\1'),
        (r'\\foreignlanguage{[^}]*}{([^}]*)}', r'\1'),
        (r'\\href{[^}]*}{([^}]*)}', r'\1')
    ]

    # Leer el contenido del archivo
    with open(filename, 'r') as file:
        content = file.read()

    # Aplicar las sustituciones
    for pattern, replacement in regex_patterns:
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
