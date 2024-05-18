import sys
import re

def reemplazar_texto_en_archivo(archivo):
    # Abrir el archivo en modo lectura y escritura
    with open(archivo, 'r+') as file:
        contenido = file.read()
        # Aplicar el reemplazo utilizando expresiones regulares
        contenido_modificado = re.sub(r'--(.*?)--', r' \\ \\ldash{\1}\\rdash \\ ', contenido)
        # Regresamos al principio del archivo y truncamos su contenido
        file.seek(0)
        file.truncate()
        # Escribir el contenido modificado en el archivo
        file.write(contenido_modificado)

if __name__ == "__main__":
    if len(sys.argv) != 2:
        print("Uso: python script.py <nombre del archivo con extension>")
        sys.exit(1)

    archivo_entrada = sys.argv[1]

    reemplazar_texto_en_archivo(archivo_entrada)
    print("Reemplazo completado en el archivo:", archivo_entrada)
