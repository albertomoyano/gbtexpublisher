import os
import re

def buscar_ligaduras_en_archivos(directorio):
    # Lista de ligaduras comunes como un solo carácter
    ligaduras = {
        'ﬁ': 'fi',
        'ﬂ': 'fl',
        'ﬃ': 'ffi',
        'ﬄ': 'ffl',
        'ﬀ': 'ff',
        'ﬅ': 'st',
        'ﬆ': 'ſt',
        'æ': 'ae',
        'œ': 'oe',
        'Ĳ': 'IJ',
        'ĳ': 'ij',
        'ǽ': 'ae',
        'Œ': 'OE'
    }

    # Expresión regular que busca cualquier carácter de ligadura
    patron_ligaduras = re.compile(r'[ﬁﬂﬃﬄﬀﬅﬆæœĲĳǽŒ]')

    coincidencia_encontrada = False  # Variable para rastrear si se encuentra alguna coincidencia

    for root, dirs, files in os.walk(directorio):
        for file in files:
            if file.endswith(".tex"):
                ruta_archivo = os.path.join(root, file)
                try:
                    with open(ruta_archivo, 'r', encoding='utf-8') as f:
                        for num_linea, linea in enumerate(f, 1):
                            if patron_ligaduras.search(linea):
                                # Identificar ligaduras específicas
                                ligaduras_encontradas = [lig for lig in ligaduras if lig in linea]
                                for lig in ligaduras_encontradas:
                                    print(f"Ligadura '{ligaduras[lig]}' encontrada en: {ruta_archivo}, línea {num_linea}")
                                coincidencia_encontrada = True  # Marca como encontrado
                except Exception as e:
                    print(f"No se pudo leer el archivo {ruta_archivo}: {e}")

    if not coincidencia_encontrada:
        print("No se encontraron ligaduras.")

if __name__ == "__main__":
    directorio_actual = os.getcwd()  # Usa el directorio actual
    buscar_ligaduras_en_archivos(directorio_actual)
