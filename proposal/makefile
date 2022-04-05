LTC="pdflatex"
BTC="bibtex"

NAME="BoudreauxThesisProposal"
LTFLAGS="-jobname=$(NAME)"
BTFLAGS=""

MANUSCRIPT_EXT="ms"

SRC_DIR="src"
FIG_DIR="figures"

MANUSCRIPT_PATH=$(SRC_DIR)/$(MANUSCRIPT_EXT)


BUILD_DIR="build"
ASSET_FILES = $(shell find ./src/ -regex '.*\(tex\|bib\|pdf\)$')


default: veryclean all clean

all: ms link

ms: ./src/$(ASSET_FILES)
	$(LTC) $(LTFLAGS) $(MANUSCRIPT_PATH).tex
	$(BTC) $(NAME)
	$(LTC) $(LTFLAGS) $(MANUSCRIPT_PATH).tex -o
	$(LTC) $(LTFLAGS) $(MANUSCRIPT_PATH).tex -o

move: | $(BUILD_DIR)
	mv -f $(NAME).pdf $(BUILD_DIR)
	mv -f *.aux $(BUILD_DIR)
	mv -f *.bbl $(BUILD_DIR)
	mv -f *.blg $(BUILD_DIR)
	mv -f *.log $(BUILD_DIR)

link: move
	ln -s $(BUILD_DIR)/$(NAME).pdf .

$(BUILD_DIR):
	mkdir -p $(BUILD_DIR)

.PHONY: clean veryclean

clean:
	-rm $(NAME).bbl
	-rm $(NAME).blg
	-rm $(NAME).aux
	-rm $(NAME).log

veryclean: clean
	rm $(NAME).pdf
	rm -r $(BUILD_DIR)


