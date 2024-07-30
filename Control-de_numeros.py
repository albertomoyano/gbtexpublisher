import re
import sys

def encontrar_lineas_con_condicion(nombre_archivo):
    try:
        with open(nombre_archivo, 'r', encoding='utf-8') as archivo:
            lineas_encontradas = 0
            for numero_linea, linea in enumerate(archivo, start=1):
                # Buscar la secuencia en la línea
                if re.search(r"\b\d{1,3}([. ][0-9]{3}|[. ][0-9]{2}[. ][0-9]| [0-9]{3})\b|\b[0-9]{3}([. ][0-9]{3})\b", linea):
                    print(f"Línea {numero_linea}")
                    lineas_encontradas += 1

            if lineas_encontradas == 0:
                print("No se encontraron líneas que cumplan la condición.")
            else:
                print(f"Se encontraron {lineas_encontradas} línea(s) que cumplen la condición de búsqueda.")
    except FileNotFoundError:
        print(f"No se pudo encontrar el archivo: {nombre_archivo}")
    except Exception as e:
        print(f"Error al leer el archivo: {e}")

# Ejemplo de uso
if len(sys.argv) != 2:
    print("Uso: python encontrar_lineas.py <nombre_del_archivo>")
    sys.exit(1)

nombre_archivo = sys.argv[1]
encontrar_lineas_con_condicion(nombre_archivo)
