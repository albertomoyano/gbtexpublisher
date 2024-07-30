import re
import sys

def ortotipografia(text):
    replacements = {
        "\\emph{Ibídem}": "Ibídem",
        "\\emph{Ibídem,}": "Ibídem,",
        "\\emph{Ibíd}": "Ibíd",
        "\\emph{Ibíd,}": "Ibíd,",
        "{[}": "[",
        "{]}": "]",
        "\\emph{: ": ": \\emph{",
        "\\emph{, ": ", \\emph{",
        "\\emph{; ": "; \\emph{",
        "\\emph{. ": ". \\emph{",
        "\\emph{ ": " \\emph{",
        "---": "--",
        "’": "'",
        "´": "'",
        ",}": "},",
        ";}": "};",
        " \\footnote{": "\\footnote{",
        "\\emph{.}": ".",
        "\\textbf{.}": ".",
        "\\textit{.}": ".",
        "\\textsuperscript{.}": ".",
        "\\emph{,}": ",",
        "\\textbf{,}": ",",
        "\\textit{,}": ",",
        "\\textsuperscript{,}": ",",
        "\\emph{;}": ";",
        "\\textbf{;}": ";",
        "\\textit{;}": ";",
        "\\textsuperscript{;}": ";",
        "\\textit{": "\\emph{",
        "iglo X": "iglo~X",
        "éculo X": "éculo~X",
        "\\uline{.}": "."
     }

    pattern = "|".join(re.escape(key) for key in replacements.keys())
    regex = re.compile(pattern)

    def replace(match):
        return replacements[match.group(0)]

    return regex.sub(replace, text)

def process_latex_file(filename):
    with open(filename, 'r', encoding='utf-8') as file:
        content = file.read()

    processed_content = ortotipografia(content)

    with open(filename, 'w', encoding='utf-8') as file:
        file.write(processed_content)

if __name__ == "__main__":
    if len(sys.argv) != 2:
        print("Uso: python script.py archivo.tex")
        sys.exit(1)

    filename = sys.argv[1]
    process_latex_file(filename)
    print("Se ha procesado el archivo con éxito.")
