import os
import sys

def contar_simbolos_en_archivos_tex(directorio):
    # Inicializar los contadores globales
    opening_symbols = {
        "{": 0, "[": 0, "(": 0,
        "¿": 0, "¡": 0
    }
    closing_symbols = {
        "}": 0, "]": 0, ")": 0,
        "?": 0, "!": 0
    }

    for root, dirs, files in os.walk(directorio):
        for file in files:
            if file.endswith(".tex"):
                ruta_archivo = os.path.join(root, file)
                try:
                    with open(ruta_archivo, "r", encoding="utf-8") as f:
                        print(f"Procesando archivo: {ruta_archivo}")

                        last_char_was_opening_bracket = False

                        for line in f:
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
                    print(f"Error al abrir el archivo: {ruta_archivo}")
                except Exception as e:
                    print(f"Error procesando el archivo {ruta_archivo}: {e}")

    # Imprimir los resultados globales
    for symbol, count in opening_symbols.items():
        print(f"Llaves/Corchetes/Paréntesis/Signos {symbol} de apertura: {count}")

    for symbol, count in closing_symbols.items():
        print(f"Llaves/Corchetes/Paréntesis/Signos {symbol} de cierre: {count}")

if __name__ == "__main__":
    directorio_actual = os.getcwd()  # Usa el directorio actual, o puedes especificar otro si lo necesitas
    contar_simbolos_en_archivos_tex(directorio_actual)
