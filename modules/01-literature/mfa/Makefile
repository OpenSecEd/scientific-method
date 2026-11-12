.PHONY: all
all: mfa.pdf

SRC+=		preamble.tex abstract.tex contents.tex
SRC+=		mfa.bib
SRC+=		$(wildcard search/*.tex)

mfa.pdf: mfa.tex ${SRC}


.PHONY: clean
clean:
	${RM} mfa.pdf
	${RM} -R ltxobj


INCLUDE_MAKEFILES=../../../makefiles
include ${INCLUDE_MAKEFILES}/tex.mk
