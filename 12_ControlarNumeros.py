import os
import re

def encontrar_lineas_con_condicion_en_archivo(ruta_archivo):
    nombre_archivo = os.path.basename(ruta_archivo)  # Extrae solo el nombre del archivo
    lineas_encontradas = []  # Almacenar las líneas encontradas con coincidencias

    try:
        with open(ruta_archivo, 'r', encoding='utf-8') as archivo:
            for numero_linea, linea in enumerate(archivo, start=1):
                # Buscar la secuencia en la línea usando la expresión regular
                if re.search(r"\b\d{1,3}([. ][0-9]{3}|[. ][0-9]{2}[. ][0-9]| [0-9]{3})\b|\b[0-9]{3}([. ][0-9]{3})\b", linea):
                    lineas_encontradas.append(f"Línea {numero_linea}")

    except FileNotFoundError:
        print(f"No se pudo encontrar el archivo: {nombre_archivo}")
    except Exception as e:
        print(f"Error al leer el archivo {nombre_archivo}: {e}")

    return lineas_encontradas

def encontrar_lineas_con_condicion_en_directorio(directorio):
    coincidencias_encontradas = False  # Rastrea si se encuentran coincidencias

    for root, dirs, files in os.walk(directorio):
        for file in files:
            if file.endswith(".tex"):
                ruta_archivo = os.path.join(root, file)
                lineas_encontradas = encontrar_lineas_con_condicion_en_archivo(ruta_archivo)

                if lineas_encontradas:
                    coincidencias_encontradas = True
                    print(f"\nArchivo: {os.path.basename(ruta_archivo)}")
                    for linea in lineas_encontradas:
                        print(linea)

    # Si no se encontraron coincidencias en ningún archivo
    if not coincidencias_encontradas:
        print("No se encontraron líneas que cumplan la condición en ningún archivo.")

if __name__ == "__main__":
    directorio_actual = os.getcwd()  # Usa el directorio actual o especifica otro si lo prefieres
    encontrar_lineas_con_condicion_en_directorio(directorio_actual)
