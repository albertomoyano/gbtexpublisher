def analizar_coherencia_preguntas(filename):
    apertura_pregunta = "¿"
    cierre_pregunta = "?"

    try:
        with open(filename, "r", encoding="utf-8") as file:
            lines_without_match = []

            for line_number, line in enumerate(file, start=1):
                stack = []

                for char in line:
                    symbol = char

                    if symbol == apertura_pregunta:
                        stack.append(apertura_pregunta)
                    elif symbol == cierre_pregunta:
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
import sys

if len(sys.argv) != 2:
    print("Uso: python analizar_coherencia_preguntas.py <nombre_del_archivo>")
    sys.exit(1)

filename = sys.argv[1]
lines_without_match = analizar_coherencia_preguntas(filename)

print("Líneas sin coincidencias de apertura y cierre de preguntas:")
for line_number in lines_without_match:
    print(f"Línea {line_number}")
