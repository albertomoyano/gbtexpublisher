import re
import sys

def normalizar_puntos(text):
    regex_replacements = [
        (r'\\ldots', r'\\dots'),
        (r'\(\\ldots\)', r'(\\dots)'),
        (r'\({\\ldots}\)', r'(\\dots)'),
        (r'\[\\ldots\]', r'(\\dots)'),
        (r'\{\\ldots\}', r'\\dots'),
        (r'\[...\]', r'(\\dots)'),
        (r'\(...\)', r'(\\dots)'),
        (r'\\dots{}', r'\\dots'),
        (r'\(\\dots\\.\)', r'(\\dots)'),
        (r'\{\\dots\}', r'\\dots'),
        (r'\.\.\.', r'\\dots'),
        (r'\.\.', r'.')
    ]

    for pattern, replacement in regex_replacements:
        text = re.sub(pattern, replacement, text)

    return text

def process_latex_file(filename):
    with open(filename, 'r', encoding='utf-8') as file:
        content = file.read()

    processed_content = normalizar_puntos(content)

    with open(filename, 'w', encoding='utf-8') as file:
        file.write(processed_content)

if __name__ == "__main__":
    if len(sys.argv) != 2:
        print("Uso: python script.py archivo.tex")
        sys.exit(1)

    filename = sys.argv[1]
    process_latex_file(filename)
    print("Se ha procesado el archivo con éxito.")
