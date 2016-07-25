TARGET = StaffBot

all: $(TARGET)

$(TARGET): $(TARGET).tex

view:
	open $(TARGET).pdf

clean:
	rm -f *.tex *.pyc *.aux *.bbl *.blg *.log *.pdf *.dvi
