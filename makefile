TEXFILES := $(wildcard ../*.tex) $(wildcard ../artcap/*.tex)
PDFS := $(TEXFILES:.tex=.pdf)

all: $(PDFS)

../%.pdf: ../%.tex
	latexmk -l -f --interaction=nonstopmode -pdflatex=lualatex -pdflua -output-directory=.. $<

