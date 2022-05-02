default: all

all: p1 p2 p3 p4 p5

.PHONY: p1 p2 p3 p4 p5
p1:
	cd p1; pdflatex ms.tex; pdftoppm ms.pdf p1.png -png -r 200; convert p1.png-1.png -crop 1700x707+0+266 p1-cropped.png
p2:
	cd p2; pdflatex ms.tex; pdftoppm ms.pdf p2.png -png -r 200; convert p2.png-1.png -crop 1700x707+0+266 p2-cropped.png
p3:
	cd p3; pdflatex ms.tex; pdftoppm ms.pdf p3.png -png -r 200; convert p3.png-1.png -crop 1700x707+0+266 p3-cropped.png
p4:
	cd p4; pdflatex ms.tex; pdftoppm ms.pdf p4.png -png -r 200; convert p4.png-1.png -crop 1700x707+0+266 p4-cropped.png
p5:
	cd p5; pdflatex ms.tex; pdftoppm ms.pdf p5.png -png -r 200; convert p5.png-1.png -crop 1700x707+0+266 p5-cropped.png


