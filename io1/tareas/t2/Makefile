SRC=t2

all:
#	dia malla.dia -e malla.png
	pdflatex $(SRC).tex
	pdflatex $(SRC).tex
	rm $(SRC).{log,aux}

clean:
	rm -fr $(SRC).{log,aux,pdf} *~

rar: all
	rar a Tarea2-IO1-maureirazamora.rar $(SRC).pdf modelo.ltx modeloAcelerado.ltx

x:
	xpdf $(SRC).pdf
o:
	okular $(SRC).pdf
e:
	evince $(SRC).pdf			 
