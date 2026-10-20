NOWEAVEFLAGS=-delay
LATEXFLAGS=-shell-escape

.PHONY: all
all: vetcyb-grading.pdf vetcyb-grading.sh
all: trnsfr-results.pdf trnsfr-results.sh

.INTERMEDIATE: vetcyb-grading.tex
vetcyb-grading.pdf: vetcyb-grading.tex
# The generic %: %.nw rule has no recipe for .sh (NOTANGLE.sh is unset)
# and the root chunks are named [[...]], so tangle explicitly.  A failed
# tangle must not leave a file behind that looks up to date.
TANGLE.sh=	notangle -R'[[$@]]' $(filter %.nw,$^) > $@ && chmod +x $@ \
		  || { ${RM} $@; false; }

vetcyb-grading.sh vetcyb-grading-test.sh: vetcyb-grading.sh.nw
	${TANGLE.sh}

vetcyb-grading.pdf: prompts.toml

GRADE_RESULTS=test-grade_reflections-err.txt

#vetcyb-grading.pdf: ${GRADE_RESULTS}
vetcyb-grading.pdf: ./instruction-qualitative.md ./submission-qualitative.md
vetcyb-grading.pdf: vetcyb-grading.sh

.PHONY: test
test: vetcyb-grading.sh vetcyb-grading-test.sh
	bash vetcyb-grading-test.sh

${GRADE_RESULTS}: test-grade-reflections.sh
	bash $<

test-grade-reflections.sh: vetcyb-grading.sh.nw vetcyb-grading.sh
	${TANGLE.sh}

.INTERMEDIATE: trnsfr-results.tex
trnsfr-results.pdf: trnsfr-results.nw
	${NOWEAVE.pdf}

trnsfr-results.sh: trnsfr-results.nw
	${TANGLE.sh}


.PHONY: clean
clean:
	${RM} vetcyb-grading.pdf vetcyb-grading.sh
	${RM} *.aux *.fdb_* *.fls *.log *.pdf *.tex
	${RM} test-grade-reflections.sh vetcyb-grading-test.sh
	${RM} test-grade_reflections.txt
	${RM} test-grade_reflections-err.txt
	${RM} trnsfr-results.pdf trnsfr-results.sh


INCLUDE_MAKEFILES=../../makefiles
include ${INCLUDE_MAKEFILES}/noweb.mk
include ${INCLUDE_MAKEFILES}/tex.mk
