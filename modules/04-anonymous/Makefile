.PHONY: all
all: notes.pdf slides.pdf

LATEXFLAGS+=	-shell-escape

SRC+=		preamble.tex
SRC+=		abstract.tex contents.tex

DEPENDS+=	objectives.tex

notes.pdf: notes.tex
notes.pdf: ${SRC} ${DEPENDS} ${FIGS}

slides.pdf: slides.tex
slides.pdf: ${SRC} ${DEPENDS} ${FIGS}

objectives.tex: ../00-intro/objectives.tex

${DEPENDS}:
	${LN} $< $@


.PHONY: clean
clean:
	${RM} notes.pdf slides.pdf
	${RM} ${DEPENDS}
	${MAKE} -C fig clean


INCLUDE_MAKEFILES=../../makefiles
include ${INCLUDE_MAKEFILES}/tex.mk
