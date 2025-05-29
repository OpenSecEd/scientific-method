.PHONY: all
all: notes.pdf slides.pdf

LATEXFLAGS+=	-shell-escape

SRC+=		preamble.tex
SRC+=		abstract.tex contents.tex

EXT_SRC+=	objectives.tex

notes.pdf: notes.tex
notes.pdf: ${SRC} ${EXT_SRC}

slides.pdf: slides.tex
slides.pdf: ${SRC} ${EXT_SRC}

objectives.tex: ../00-intro/objectives.tex

${EXT_SRC}:
	${LN} $< $@


.PHONY: clean
clean:
	${RM} notes.pdf slides.pdf
	${RM} ${EXT_SRC}


INCLUDE_MAKEFILES=../../makefiles
include ${INCLUDE_MAKEFILES}/tex.mk
