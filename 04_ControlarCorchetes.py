import re
import sys

def analizar_coherencia_corchetes(filename):
    apertura_corchete = "["
    cierre_corchete = "]"

    try:
        with open(filename, "r", encoding="utf-8") as file:
            lines_without_match = []

            for line_number, line in enumerate(file, start=1):
                stack = []

                for char in line:
                    symbol = char

                    if symbol == apertura_corchete:
                        stack.append(apertura_corchete)
                    elif symbol == cierre_corchete:
                        if stack:
                            stack.pop()
                        else:
                            lines_without_match.append(line_number)
                            break

                if stack:
                    lines_without_match.append(line_number)

    except FileNotFoundError:
        print("Error al abrir el archivo.")
        return []

    return lines_without_match

# Ejemplo de uso
if len(sys.argv) != 2:
    print("Uso: python analizar_coherencia_corchetes.py <nombre_del_archivo>")
    sys.exit(1)

filename = sys.argv[1]
lines_without_match = analizar_coherencia_corchetes(filename)

print("Líneas sin coincidencias de apertura y cierre de corchetes:")
for line_number in lines_without_match:
    print(f"Línea {line_number}")
