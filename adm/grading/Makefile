NOWEAVEFLAGS=-delay
LATEXFLAGS=-shell-escape

.PHONY: all
all: vetcyb-grading.pdf vetcyb-grading.sh

.INTERMEDIATE: vetcyb-grading.tex
vetcyb-grading.pdf: vetcyb-grading.tex
vetcyb-grading.sh: vetcyb-grading.sh.nw

vetcyb-grading.pdf: prompts.toml

GRADE_RESULTS=test-grade_reflections-err.txt

vetcyb-grading.pdf: ${GRADE_RESULTS}
vetcyb-grading.pdf: ./instruction-qualitative.md ./submission-qualitative.md

${GRADE_RESULTS}: test-grade-reflections.sh
	bash $<

test-grade-reflections.sh: vetcyb-grading.sh.nw vetcyb-grading.sh
	${NOTANGLE.sh}

.PHONY: clean
clean:
	${RM} vetcyb-grading.pdf vetcyb-grading.sh
	${RM} *.aux *.fdb_* *.fls *.log *.pdf *.tex
	${RM} test-grade-reflections.sh
	${RM} test-grade_reflections.txt
	${RM} test-grade_reflections-err.txt


INCLUDE_MAKEFILES=../../makefiles
include ${INCLUDE_MAKEFILES}/noweb.mk
include ${INCLUDE_MAKEFILES}/tex.mk
