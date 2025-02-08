import os
import re

def buscar_patron_en_archivos(directorio):
    # Expresión regular para buscar 'siglo' (sin importar mayúsculas/minúsculas) seguido de un espacio y un número romano
    patron_siglo_x = re.compile(r'\bsiglo [IVXLCDM]+\b', re.IGNORECASE)
    # Expresión regular para buscar ' y ' seguido de un número romano o letra mayúscula
    patron_y_x = re.compile(r' y \b[IVXLCDM]+\b')

    coincidencia_encontrada = False  # Variable para rastrear si se encuentra alguna coincidencia

    for root, dirs, files in os.walk(directorio):
        for file in files:
            if file.endswith(".tex"):
                ruta_archivo = os.path.join(root, file)
                try:
                    with open(ruta_archivo, 'r', encoding='utf-8') as f:
                        for num_linea, linea in enumerate(f, 1):
                            # Busca coincidencias con los dos patrones
                            if patron_siglo_x.search(linea):
                                print(f"Coincidencia 'siglo X' en: {ruta_archivo}, línea {num_linea}")
                                coincidencia_encontrada = True  # Marca como encontrado
                            if patron_y_x.search(linea):
                                print(f"Coincidencia ' y X' en: {ruta_archivo}, línea {num_linea}")
                                coincidencia_encontrada = True  # Marca como encontrado
                except Exception as e:
                    print(f"No se pudo leer el archivo {ruta_archivo}: {e}")

    if not coincidencia_encontrada:
        print("No se encontraron coincidencias para los patrones de búsqueda.")

if __name__ == "__main__":
    directorio_actual = os.getcwd()  # Usa el directorio actual
    buscar_patron_en_archivos(directorio_actual)
