import os
import re

def encontrar_palabras_repetidas_en_archivo(ruta_archivo):
    nombre_archivo = os.path.basename(ruta_archivo)  # Obtener solo el nombre del archivo
    palabras_repetidas = []

    try:
        with open(ruta_archivo, 'r', encoding='utf-8') as f:
            lineas = f.readlines()

        # Iterar sobre cada línea del archivo
        for num_linea, linea in enumerate(lineas, start=1):
            # Encontrar palabras repetidas continuas usando expresiones regulares
            matches = re.finditer(r'\b(\w+)\s+\1\b', linea)
            for match in matches:
                palabra = match.group(1)
                palabras_repetidas.append((num_linea, palabra))

    except FileNotFoundError:
        print(f"No se pudo encontrar el archivo {ruta_archivo}")
    except Exception as e:
        print(f"Error procesando el archivo {nombre_archivo}: {e}")

    # Mostrar resultados si se encontraron palabras repetidas
    if palabras_repetidas:
        print(f"\nArchivo: {nombre_archivo}")
        print("Palabras repetidas encontradas:")
        for num_linea, palabra in palabras_repetidas:
            print(f"Línea {num_linea}: {palabra}")
        return True  # Se encontraron palabras repetidas
    return False  # No se encontraron palabras repetidas

def encontrar_palabras_repetidas_en_directorio(directorio):
    repeticiones_encontradas = False  # Variable para rastrear si se encuentran repeticiones en algún archivo

    for root, dirs, files in os.walk(directorio):
        for file in files:
            if file.endswith(".tex"):
                ruta_archivo = os.path.join(root, file)
                if encontrar_palabras_repetidas_en_archivo(ruta_archivo):
                    repeticiones_encontradas = True  # Marcar como encontrado si hay repeticiones

    if not repeticiones_encontradas:
        print("No se encontraron coincidencias para los patrones de búsqueda.")

if __name__ == "__main__":
    directorio_actual = os.getcwd()  # Usa el directorio actual o especifica otro si lo prefieres
    encontrar_palabras_repetidas_en_directorio(directorio_actual)
