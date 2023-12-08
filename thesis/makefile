LTC="pdflatex"
BTC="bibtex"
NAME="Thesis"
TFLAGS="-jobname=$(NAME)"
SRC_DIR="."
MAIN_SRC="ms.tex"

ASSET_FILES = $(shell find ./src/ -regex '.*\(tex\|pdf\)$')

default: all

all: pdf

pdf: ./src/$(ASSET_FILE)
	cd src && $(LTC) $(TFLAGS) $(SRC_DIR)/$(MAIN_SRC)
	-cd src && $(BTC) $(NAME)
	cd src && $(LTC) $(TFLAGS) $(SRC_DIR)/$(MAIN_SRC)
	cd src && $(LTC) $(TFLAGS) $(SRC_DIR)/$(MAIN_SRC)
	cp src/$(NAME).pdf .
clean:
	-rm $(NAME).blg
	-rm $(NAME).bbl
	-rm $(NAME).aux
	-rm $(NAME).log
