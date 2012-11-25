SRC=t3

all:
#	dia malla.dia -e malla.png
	pdflatex $(SRC).tex
	pdflatex $(SRC).tex
	rm $(SRC).{log,aux}

clean:
	rm -fr $(SRC).{log,aux,pdf} *~

tar: all
	tar -zcvf Tarea3-IO1-maureirazamora.tar.gz $(SRC).pdf modelo*.ltx 
rar: all
	rar a Tarea3-IO1-maureirazamora.rar $(SRC).pdf modelo*.ltx 
x:
	xpdf $(SRC).pdf
o:
	okular $(SRC).pdf
e:
	evince $(SRC).pdf			 
