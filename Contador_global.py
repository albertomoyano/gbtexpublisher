import sys
import codecs

filename = sys.argv[1] if len(sys.argv) == 2 else None

if not filename:
    print("Uso: python contar_simbolos.py <nombre_del_archivo>")
    sys.exit(1)

try:
    with codecs.open(filename, "r", encoding="utf-8") as file:
        opening_symbols = {
            "{": 0, "[": 0, "(": 0,
            "¿": 0, "¡": 0
        }

        closing_symbols = {
            "}": 0, "]": 0, ")": 0,
            "?": 0, "!": 0
        }

        last_char_was_opening_bracket = False

        for line in file:
            for symbol in line:
                if last_char_was_opening_bracket and symbol == "!":
                    # Ignorar el símbolo '!' si está precedido por '['
                    pass
                else:
                    if symbol in opening_symbols:
                        opening_symbols[symbol] += 1
                        last_char_was_opening_bracket = symbol == "["
                    elif symbol in closing_symbols:
                        closing_symbols[symbol] += 1
                    last_char_was_opening_bracket = False  # Reiniciar el indicador

except FileNotFoundError:
    print("Error al abrir el archivo.")
    sys.exit(1)

# Imprimir los resultados
for symbol, count in opening_symbols.items():
    print(f"Llaves/Corchetes/Paréntesis/Signos {symbol} de apertura: {count}")

for symbol, count in closing_symbols.items():
    print(f"Llaves/Corchetes/Paréntesis/Signos {symbol} de cierre: {count}")
