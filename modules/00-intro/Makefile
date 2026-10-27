LATEXFLAGS+=	-shell-escape

.PHONY: all
all: slides.pdf notes.pdf

SRC+=		preamble.tex
SRC+=		abstract.tex contents.tex
SRC+= 		bibliography.bib

notes.pdf: notes.tex
notes.pdf: ${SRC}

slides.pdf: slides.tex
slides.pdf: ${SRC} about-you.tex

# The About you slides, from this round's survey (counts and an llm summary
# of the interests; no answers or names).  Regenerate with make -B.
COURSE?=	vetcyb26h
CANVAS_PY?=	$(shell head -1 "$$(readlink -f "$$(command -v canvaslms)")" \
		  | sed 's/^\#!//')
about-you.tex: about-you.py
	${CANVAS_PY} -I $< '^${COURSE}$$' > $@ || { ${RM} $@; false; }


.PHONY: clean
clean:
	${RM} notes.pdf slides.pdf about-you.tex


INCLUDE_MAKEFILES=../../makefiles
include ${INCLUDE_MAKEFILES}/tex.mk
