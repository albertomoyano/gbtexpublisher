import re
import sys

def encontrar_palabras_repetidas(archivo):
    # Abrir el archivo y leer su contenido
    with open(archivo, 'r') as f:
        lineas = f.readlines()

    palabras_repetidas = []

    # Iterar sobre cada línea del archivo
    for num_linea, linea in enumerate(lineas, start=1):
        # Encontrar palabras repetidas continuas usando expresiones regulares
        matches = re.finditer(r'\b(\w+)\s+\1\b', linea)
        for match in matches:
            palabra = match.group(1)
            palabras_repetidas.append((num_linea, palabra))

    return palabras_repetidas

if __name__ == "__main__":
    if len(sys.argv) != 2:
        print("Uso: python script.py archivo")
        sys.exit(1)

    archivo = sys.argv[1]
    palabras_repetidas = encontrar_palabras_repetidas(archivo)

    if palabras_repetidas:
        print("Palabras repetidas encontradas:")
        for num_linea, palabra in palabras_repetidas:
            print(f"Línea {num_linea}: {palabra}")
    else:
        print("No se encontraron palabras repetidas continuas en el archivo.")
