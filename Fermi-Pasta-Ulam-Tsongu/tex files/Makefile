PDF = fput-Lee-2021

all:	clean ${PDF}

${PDF}:	main.tex
	ln -sf ../../bib/{*.bib,*.bst} .
	latexmk -pdf -jobname=$@ main

clean		:
		rm -f *.aux *.bbl *.blg *.dvi *.log *.ps *.fdb_latexmk *.fls *.bib *.png *-converted-to.pdf *.eps *eps-converted-to.pdf *.bst *.pdf *.png *.out *.fls
