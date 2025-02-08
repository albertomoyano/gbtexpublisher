import os
import re

def buscar_patron_en_archivos(directorio):
    # Expresión regular para buscar '?' seguido de un espacio y una letra en minúscula
    patron = re.compile(r'\? [a-z]')
    resultados = []  # Almacenar los resultados donde haya coincidencias

    for root, dirs, files in os.walk(directorio):
        for file in files:
            if file.endswith(".tex"):
                ruta_archivo = os.path.join(root, file)
                nombre_archivo = os.path.basename(ruta_archivo)  # Extrae solo el nombre del archivo
                try:
                    with open(ruta_archivo, 'r', encoding='utf-8') as f:
                        for num_linea, linea in enumerate(f, 1):
                            if patron.search(linea):
                                resultados.append(f"Error encontrado en línea {num_linea} en archivo: {nombre_archivo}")
                except Exception as e:
                    resultados.append(f"No se pudo leer el archivo {nombre_archivo}: {e}")

    # Limpiar la consola en Linux
    os.system('clear')

    # Mostrar los resultados
    if resultados:
        for resultado in resultados:
            print(resultado)
    else:
        print("No se encontraron coincidencias para el patrón de búsqueda.")

if __name__ == "__main__":
    directorio_actual = os.getcwd()  # Usa el directorio actual
    buscar_patron_en_archivos(directorio_actual)
