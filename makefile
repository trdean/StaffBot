scatter:	
	python ScatterBot.py > scatter.tex; pdflatex scatter.tex

vs:
	open scatter.pdf

flow:
	python FlowBot.py > flow.tex; pdflatex flow.tex

vf:
	open flow.pdf

clean:
	rm -f *.tex *.pyc *.aux *.bbl *.blg *.log *.pdf *.dvi
