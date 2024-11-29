import os
import re

def buscar_comas_y_puntos_en_archivo(ruta_archivo):
    nombre_archivo = os.path.basename(ruta_archivo)  # Obtener solo el nombre del archivo
    coincidencias = []

    try:
        with open(ruta_archivo, 'r', encoding='utf-8') as f:
            lineas = f.readlines()

        # Iterar sobre cada línea del archivo
        for num_linea, linea in enumerate(lineas, start=1):
            # Buscar comas o puntos y comas con caracteres diferentes de espacios a ambos lados,
            # excluyendo casos con arroba o \footnote a la derecha
            matches = re.finditer(r'[^\s],(?!@|\\footnote)[^\s]|[^\s];(?!@|\\footnote)[^\s]', linea)
            for match in matches:
                # Guardar el número de línea y el texto de la coincidencia
                coincidencias.append((num_linea, match.group()))

    except FileNotFoundError:
        print(f"No se pudo encontrar el archivo {ruta_archivo}")
    except Exception as e:
        print(f"Error procesando el archivo {nombre_archivo}: {e}")

    # Mostrar resultados si se encontraron coincidencias
    if coincidencias:
        print(f"\nArchivo: {ruta_archivo}")
        print("Coincidencias encontradas:")
        for num_linea, coincidencia in coincidencias:
            print(f"Línea {num_linea}: '{coincidencia}'")
        return True  # Se encontraron coincidencias
    return False  # No se encontraron coincidencias

def buscar_comas_y_puntos_en_directorio(directorio):
    coincidencias_encontradas = False  # Variable para rastrear si se encuentran coincidencias en algún archivo

    for root, dirs, files in os.walk(directorio):
        for file in files:
            if file.endswith(".tex"):
                ruta_archivo = os.path.join(root, file)
                if buscar_comas_y_puntos_en_archivo(ruta_archivo):
                    coincidencias_encontradas = True  # Marcar como encontrado si hay coincidencias

    if not coincidencias_encontradas:
        print("No se encontraron coincidencias para los patrones de búsqueda.")

if __name__ == "__main__":
    directorio_actual = os.getcwd()  # Usa el directorio actual o especifica otro si lo prefieres
    buscar_comas_y_puntos_en_directorio(directorio_actual)
