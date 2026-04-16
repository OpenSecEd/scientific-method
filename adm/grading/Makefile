NOWEAVEFLAGS=-delay
LATEXFLAGS=-shell-escape

.PHONY: all
all: vetcyb-grading.pdf vetcyb-grading.sh
all: trnsfr-results.pdf trnsfr-results.sh

.INTERMEDIATE: vetcyb-grading.tex
vetcyb-grading.pdf: vetcyb-grading.tex
vetcyb-grading.sh: vetcyb-grading.sh.nw

vetcyb-grading.pdf: prompts.toml

GRADE_RESULTS=test-grade_reflections-err.txt

#vetcyb-grading.pdf: ${GRADE_RESULTS}
vetcyb-grading.pdf: ./instruction-qualitative.md ./submission-qualitative.md
vetcyb-grading.pdf: vetcyb-grading.sh

${GRADE_RESULTS}: test-grade-reflections.sh
	bash $<

test-grade-reflections.sh: vetcyb-grading.sh.nw vetcyb-grading.sh
	${NOTANGLE.sh}

.INTERMEDIATE: trnsfr-results.tex
trnsfr-results.pdf: trnsfr-results.nw
	${NOWEAVE.pdf}

trnsfr-results.sh: trnsfr-results.nw
	${NOTANGLE.sh}
	chmod +x $@


.PHONY: clean
clean:
	${RM} vetcyb-grading.pdf vetcyb-grading.sh
	${RM} *.aux *.fdb_* *.fls *.log *.pdf *.tex
	${RM} test-grade-reflections.sh
	${RM} test-grade_reflections.txt
	${RM} test-grade_reflections-err.txt
	${RM} trnsfr-results.pdf trnsfr-results.sh


INCLUDE_MAKEFILES=../../makefiles
include ${INCLUDE_MAKEFILES}/noweb.mk
include ${INCLUDE_MAKEFILES}/tex.mk
