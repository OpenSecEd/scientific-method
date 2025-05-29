LATEXFLAGS+=	-shell-escape

.PHONY: all
all: slides.pdf notes.pdf

SRC+=		preamble.tex
SRC+=		abstract.tex contents.tex
SRC+= 		bibliography.bib

notes.pdf: notes.tex
notes.pdf: ${SRC}

slides.pdf: slides.tex
slides.pdf: ${SRC}


.PHONY: clean
clean:
	${RM} notes.pdf slides.pdf


INCLUDE_MAKEFILES=../../makefiles
include ${INCLUDE_MAKEFILES}/tex.mk
