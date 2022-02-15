LTC="pdflatex"
BTC="bibtex"

NAME="BoudreauxThesisProposal"
LTFLAGS="--jobname=$(NAME)"
BTFLAGS=""

MANUSCRIPT_EXT="ms"

SRC_DIR="src"
FIG_DIR="figures"

MANUSCRIPT_PATH=$(SRC_DIR)/$(MANUSCRIPT_EXT)


BUILD_DIR="build"
ASSET_FILES = $(shell find ./src/ -regex '.*\(tex\|bib\|pdf\)$')


default: all clean

all: ms move

ms: ./src/$(ASSET_FILES)
	$(LTC) $(LTFLAGS) $(MANUSCRIPT_PATH).tex
	- $(BTC) $(BTFLAGS) $(NAME)
	$(LTC) $(LTFLAGS) $(MANUSCRIPT_PATH).tex -o
	$(LTC) $(LTFLAGS) $(MANUSCRIPT_PATH).tex -o

move: | $(BUILD_DIR)
	mv $(NAME).pdf $(BUILD_DIR)

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


