PDF = GA-Lee-2021

all:	clean ${PDF}

${PDF}:	main.tex
	ln -sf ../../bib/{*.bib,*.bst} .
	latexmk -pdf -jobname=$@ main
	-mv main.pdf GA-Lee-2021.pdf

clean		:
		rm -f *.aux *.bbl *.blg *.dvi *.log *.ps *.fdb_latexmk *.fls *.bib *.png *-converted-to.pdf *.eps *eps-converted-to.pdf *.bst  *.png *.out *.fls
