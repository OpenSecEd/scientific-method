# The margin citations reuse footnotes, which takes more passes to settle
# than latexmk's default of five.  Without this, the shared tex.mk keeps
# calling a latexmk that has given up.
$max_repeat = 25;
