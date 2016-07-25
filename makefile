TARGET = StaffBot

all: $(TARGET)

$(TARGET): 
	python $(TARGET).py >$(TARGET).tex;pdflatex $(TARGET).tex

view:
	open $(TARGET).pdf

clean:
	rm -f *.tex *.pyc *.aux *.bbl *.blg *.log *.pdf *.dvi
