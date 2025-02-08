import os
import re

def encontrar_texto_entre_parentesis_en_archivo(ruta_archivo):
    nombre_archivo = os.path.basename(ruta_archivo)  # Obtener solo el nombre del archivo

    try:
        with open(ruta_archivo, 'r', encoding='utf-8') as f:
            lineas = f.readlines()
            print(f"\nArchivo: {nombre_archivo}")  # Imprimir el nombre del archivo
            for num_linea, linea in enumerate(lineas, start=1):
                coincidencias = re.findall(r'\(([^()]*\d[^()]*)\)', linea)
                for coincidencia in coincidencias:
                    print(f"Número de línea {num_linea}: ({coincidencia})")
    except FileNotFoundError:
        print(f"No se pudo encontrar el archivo {ruta_archivo}")
    except Exception as e:
        print(f"Error procesando el archivo {nombre_archivo}: {e}")

def encontrar_texto_entre_parentesis_en_directorio(directorio):
    for root, dirs, files in os.walk(directorio):
        for file in files:
            if file.endswith(".tex"):
                ruta_archivo = os.path.join(root, file)
                encontrar_texto_entre_parentesis_en_archivo(ruta_archivo)

if __name__ == "__main__":
    directorio_actual = os.getcwd()  # Usa el directorio actual o especifica otro si lo prefieres
    encontrar_texto_entre_parentesis_en_directorio(directorio_actual)
