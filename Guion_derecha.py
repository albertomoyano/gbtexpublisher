import re
import sys

def find_lines_with_pattern(file_path):
    # La expresión regular busca cualquier carácter excepto '-' seguido de '-' y luego un espacio
    pattern = re.compile(r'[^-]-\s')
    try:
        with open(file_path, 'r') as file:
            for line_number, line in enumerate(file, start=1):
                if pattern.search(line):
                    print(line_number)
    except FileNotFoundError:
        print(f"El archivo {file_path} no se encontró.")
    except Exception as e:
        print(f"Ocurrió un error: {e}")

if __name__ == "__main__":
    if len(sys.argv) != 2:
        print("Uso: python script.py archivo.txt")
    else:
        archivo = sys.argv[1]
        find_lines_with_pattern(archivo)
