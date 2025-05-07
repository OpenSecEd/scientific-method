.PHONY: all
all: seminar-slides.pdf

LATEXFLAGS+=	-shell-escape

SRC+=		preamble.tex
SRC+=		abstract.tex seminar.tex

DEPENDS+=	objectives.tex

seminar-slides.pdf: seminar-slides.tex ${SRC} ${DEPENDS}

objectives.tex: ../00-intro/objectives.tex

${DEPENDS}:
	${LN} $< $@


.PHONY: clean
clean:
	${RM} seminar-slides.pdf
	${RM} ${DEPENDS}


INCLUDE_MAKEFILES=../../makefiles
include ${INCLUDE_MAKEFILES}/tex.mk
