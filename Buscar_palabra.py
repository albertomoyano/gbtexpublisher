import os

def buscar_palabra_en_archivos(directorio, palabra):
    coincidencia_encontrada = False  # Variable para rastrear si se encuentra alguna coincidencia
    for root, dirs, files in os.walk(directorio):
        for file in files:
            if file.endswith(".tex"):
                ruta_archivo = os.path.join(root, file)
                try:
                    with open(ruta_archivo, 'r', encoding='utf-8') as f:
                        for num_linea, linea in enumerate(f, 1):
                            if palabra in linea:
                                print(f"Encontrada en: {ruta_archivo}, línea {num_linea}")
                                coincidencia_encontrada = True  # Marca como encontrado
                except Exception as e:
                    print(f"No se pudo leer el archivo {ruta_archivo}: {e}")

    if not coincidencia_encontrada:
        print("No se encontraron coincidencias para la búsqueda.")

if __name__ == "__main__":
    palabra = input("Introduce la palabra a buscar: ")

    directorio_actual = os.getcwd()
    buscar_palabra_en_archivos(directorio_actual, palabra)
