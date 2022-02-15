LTC="pdflatex"
BTC="bibtex"

NAME="BoudreauxThesisProposal"
LTFLAGS="--jobname=$(NAME)"
BTFLAGS=""

MANUSCRIPT_EXT="ms.tex"

SRC_DIR="src"
FIG_DIR="figures"

MANUSCRIPT_PATH=$(SRC_DIR)/$(MANUSCRIPT_EXT)


BUILD_DIR="build"


default: all clean

all: ms move

ms: src/$(MANUSCRIPT_EXT).tex src/$(MANUSCRIPT_EXT).bib
	$(LTC) $(LTFLAGS) $(MANUSCRIPT_PATH)
	$(BTC) $(BTFLAGS) $(NAME)
	$(LTC) $(LTFLAGS) $(MANUSCRIPT_PATH) -o
	$(LTC) $(LTFLAGS) $(MANUSCRIPT_PATH) -o

move: | $(BUILD_DIR)
	mv $(NAME).pdf $(BUILD_DIR)

$(BUILD_DIR):
	mkdir -p $(BUILD_DIR)

.PHONY: clean veryclean

clean:
	rm *.bbl
	rm *.blg
	rm *.aux
	rm *.log

veryclean: clean
	rm *.pdf
	rm -r $(BUILD_DIR)


