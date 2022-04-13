LTC="pdflatex"
BTC="bibtex"

NAME="BoudreauxThesisProposal"
LTFLAGS="-jobname=$(NAME)"
BTFLAGS=""

SUNAME="BoudreauxThesisProposal_Summary"
SULTFLAGS="-jobname=$(SUNAME)"

MANUSCRIPT_EXT="ms"
SUEXT="summary"

SRC_DIR="src"
FIG_DIR="figures"

MANUSCRIPT_PATH=$(SRC_DIR)/$(MANUSCRIPT_EXT)
SUPATH=$(SRC_DIR)/$(SUEXT)

BUILD_DIR="build"
ASSET_FILES = $(shell find ./src/ -regex '.*\(tex\|bib\|pdf\)$')


default: veryclean all clean

all: ms summary link

ms: ./src/$(ASSET_FILES)
	$(LTC) $(LTFLAGS) $(MANUSCRIPT_PATH).tex
	$(BTC) $(NAME)
	$(LTC) $(LTFLAGS) $(MANUSCRIPT_PATH).tex -o
	$(LTC) $(LTFLAGS) $(MANUSCRIPT_PATH).tex -o

summary: ./src/summary.tex
	$(LTC) $(SULTFLAGS) $(SUPATH).tex

move: | $(BUILD_DIR)
	mv -f $(NAME).pdf $(BUILD_DIR)
	mv -f $(SUNAME).pdf $(BUILD_DIR)
	mv -f *.aux $(BUILD_DIR)
	mv -f *.bbl $(BUILD_DIR)
	mv -f *.blg $(BUILD_DIR)
	mv -f *.log $(BUILD_DIR)

link: move
	ln -s $(BUILD_DIR)/$(NAME).pdf .
	ln -s $(BUILD_DIR)/$(SUNAME).pdf .

$(BUILD_DIR):
	mkdir -p $(BUILD_DIR)

.PHONY: clean veryclean

clean:
	-rm $(NAME).bbl
	-rm $(NAME).blg
	-rm $(NAME).aux
	-rm $(NAME).log
	-rm $(SUNAME).bbl
	-rm $(SUNAME).blg
	-rm $(SUNAME).aux
	-rm $(SUNAME).log

veryclean: clean
	-rm $(NAME).pdf
	-rm $(SUNAME).pdf
	-rm -r $(BUILD_DIR)


