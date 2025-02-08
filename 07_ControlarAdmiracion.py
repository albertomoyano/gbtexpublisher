def analizar_coherencia_signos(filename):
    apertura_signo = "¡"
    cierre_signo = "!"

    try:
        with open(filename, "r", encoding="utf-8") as file:
            lines_without_match = []

            for line_number, line in enumerate(file, start=1):
                stack = []

                for char in line:
                    if char == apertura_signo:
                        stack.append(apertura_signo)
                    elif char == cierre_signo:
                        if stack and stack[-1] == apertura_signo:
                            stack.pop()
                        else:
                            lines_without_match.append(line_number)  # Solo se agrega el número de línea
                            break

                if stack:  # Si quedan elementos en la pila, entonces falta un cierre
                    lines_without_match.append(line_number)  # Solo se agrega el número de línea

    except FileNotFoundError:
        print("Error al abrir el archivo.")
        return []

    return lines_without_match

# Ejemplo de uso
import sys

if len(sys.argv) != 2:
    print("Uso: python analizar_coherencia_signos.py <nombre_del_archivo>")
    sys.exit(1)

filename = sys.argv[1]
lines_without_match = analizar_coherencia_signos(filename)

print("Líneas donde no hay coincidencia entre la apertura y el cierre de signos de admiración:")
for line_number in lines_without_match:  # Solo se itera sobre los números de línea
    print(f"Línea {line_number}")
