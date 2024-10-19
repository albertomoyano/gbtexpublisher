import sys
import re

def verificar_expresion_archivo(archivo):
    with open(archivo, 'r') as f:
        lineas = f.readlines()

    errores = []
    for num_linea, linea in enumerate(lineas, start=1):
        if re.search(r'[^[\(\{\s]\\(?:emph|textbf|url|textit|href){', linea):
            errores.append(num_linea)

    return errores

if __name__ == "__main__":
    if len(sys.argv) != 2:
        print("Uso: python script.py nombredearchivo.tex")
        sys.exit(1)

    archivo = sys.argv[1]
    lineas_con_errores = verificar_expresion_archivo(archivo)

    if lineas_con_errores:
        print("Se encontraron errores en las siguientes líneas:")
        for linea in lineas_con_errores:
            print(linea)
    else:
        print("No se encontraron errores.")
