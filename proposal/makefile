LTC="pdflatex"
BTC="bibtex"

NAME="BoudreauxThesisProposal"
LTFLAGS="-jobname=$(NAME)"
BTFLAGS=""

SUNAME="BoudreauxThesisProposal_Summary"
SULTFLAGS="-jobname=$(SUNAME)"

TLNAME="TIMELINE"
TLFLAGS="-jobname=$(TLNAME)"

MANUSCRIPT_EXT="ms"
SUEXT="summary"

TIKZ_DIR="tikz"
SRC_DIR="src"
FIG_DIR="$(SRC_DIR)/Figures"

MANUSCRIPT_PATH=$(SRC_DIR)/$(MANUSCRIPT_EXT)
SUPATH=$(SRC_DIR)/$(SUEXT)

TLPATH="./src/timeline_wrtout.tex"

BUILD_DIR="build"
ASSET_FILES = $(shell find ./src/ -regex '.*\(tex\|bib\|pdf\)$')


default: draft

draft: veryclean ms summary link watermark timelineConvert clean

final: veryclean ms summary link timelineConvert clean

ms: ./src/$(ASSET_FILES)
	$(LTC) $(LTFLAGS) $(MANUSCRIPT_PATH).tex
	$(BTC) $(NAME)
	$(LTC) $(LTFLAGS) $(MANUSCRIPT_PATH).tex -o
	$(LTC) $(LTFLAGS) $(MANUSCRIPT_PATH).tex -o

watermark:
	pdftk $(NAME).pdf background misc/Stamp.pdf output $(NAME)_mark.pdf
	rm $(NAME).pdf
	mv $(NAME)_mark.pdf $(NAME).pdf

summary: ./src/summary.tex
	$(LTC) $(SULTFLAGS) $(SUPATH).tex

timelineFig: ./src/tikz/timeline_fig.tex ./src/timeline_wrtout.tex
	$(LTC) $(TLFLAGS) $(TLPATH)

timelineConvert: timelineFig
	pdftoppm -png -singlefile $(TLNAME).pdf $(TLNAME)
	mv $(TLNAME).png $(FIG_DIR)


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
	-rm $(TLNAME).aux
	-rm $(TLNAME).log
	-rm $(TLNAME).pdf

veryclean: clean
	-rm $(NAME).pdf
	-rm $(TLNAME).pdf
	-rm $(SUNAME).pdf
	-rm -r $(BUILD_DIR)


