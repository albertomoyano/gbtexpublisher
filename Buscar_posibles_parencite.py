import re
import sys

def encontrar_texto_entre_parentesis(archivo):
    try:
        with open(archivo, 'r') as f:
            lineas = f.readlines()
            for num_linea, linea in enumerate(lineas, start=1):
                coincidencias = re.findall(r'\(([^()]*\d[^()]*)\)', linea)
                for coincidencia in coincidencias:
                    print(f"Número de línea {num_linea}: ({coincidencia})")
    except FileNotFoundError:
        print(f"No se pudo encontrar el archivo {archivo}")

if __name__ == "__main__":
    if len(sys.argv) != 2:
        print("Uso: python script.py archivo.tex")
        sys.exit(1)

    archivo = sys.argv[1]
    encontrar_texto_entre_parentesis(archivo)
