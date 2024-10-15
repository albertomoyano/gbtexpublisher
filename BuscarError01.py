import os
import re

def buscar_patron_en_archivos(directorio):
    # Expresión regular para buscar '?' seguido de un espacio y una letra en minúscula
    patron = re.compile(r'\? [a-z]')
    coincidencia_encontrada = False  # Variable para rastrear si se encuentra alguna coincidencia

    for root, dirs, files in os.walk(directorio):
        for file in files:
            if file.endswith(".tex"):
                ruta_archivo = os.path.join(root, file)
                try:
                    with open(ruta_archivo, 'r', encoding='utf-8') as f:
                        for num_linea, linea in enumerate(f, 1):
                            if patron.search(linea):
                                print(f"Error encontrado en: {ruta_archivo}, línea {num_linea}")
                                coincidencia_encontrada = True  # Marca como encontrado
                except Exception as e:
                    print(f"No se pudo leer el archivo {ruta_archivo}: {e}")

    if not coincidencia_encontrada:
        print("No se encontraron coincidencias para el patrón.")

if __name__ == "__main__":
    directorio_actual = os.getcwd()  # Usa el directorio actual
    buscar_patron_en_archivos(directorio_actual)
