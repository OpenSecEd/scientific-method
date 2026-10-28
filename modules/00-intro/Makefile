LATEXFLAGS+=	-shell-escape

# The Mentipy polls run in PythonTeX, which must import mentipy from the deck's
# own venv (made here, never by hand).  The shared tex.mk has no working
# PythonTeX step for this layout (output in ltxobj/, \setpythontexoutputdir{.}),
# so the PDF rule below compiles, runs PythonTeX in ltxobj/ and compiles again.
MENTIPY_VENV=	$(CURDIR)/.venv
PYTHONTEXFLAGS=	--interpreter python:${MENTIPY_VENV}/bin/python3 --rerun=always

${MENTIPY_VENV}/bin/python3:
	mentipy init --venv ${MENTIPY_VENV}

MENTIPY_VERSION=	0.14
MENTIPY_STAMP=	${MENTIPY_VENV}/mentipy-${MENTIPY_VERSION}

# Order-only: the venv must exist, but its timestamp must not trigger an
# upgrade.  The PythonTeX output goes with the upgrade.
${MENTIPY_STAMP}: | ${MENTIPY_VENV}/bin/python3
	${MENTIPY_VENV}/bin/python3 -m pip install 'mentipy>=${MENTIPY_VERSION}'
	${RM} ${TEX_OUTDIR}/*.pytxmcr
	touch $@

notes.pdf slides.pdf: ${MENTIPY_STAMP}
# mentipy serve rewrites the QR sidecars; the PDFs must follow them.
notes.pdf slides.pdf: $(wildcard mentipy-obj/Q-*.pdf_tex)

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


# The last latexmk needs -g: it does not see the new PythonTeX output as a
# change.
slides.pdf notes.pdf: %.pdf: %.tex
	${PDFLATEX} ${LATEXFLAGS} -output-directory=${TEX_OUTDIR} $<
	cd ${TEX_OUTDIR} && pythontex ${PYTHONTEXFLAGS} $*
	${PDFLATEX} -g ${LATEXFLAGS} -output-directory=${TEX_OUTDIR} $<
	-${LN} ${TEX_OUTDIR}/$@ $@

.PHONY: clean
clean:
	${RM} notes.pdf slides.pdf about-you.tex
	${RM} -R mentipy-obj


INCLUDE_MAKEFILES=../../makefiles
include ${INCLUDE_MAKEFILES}/tex.mk
