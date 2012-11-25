SRC=t1

all:
	latex $(SRC).tex
	latex $(SRC).tex
	dvipdf $(SRC).dvi
	rm $(SRC).{log,aux}

clean:
	rm -fr $(SRC).{log,aux,pdf,dvi} *~

tar: all
	tar -cvf Tarea1-IO1-maureirazamora.tar.gz $(SRC).pdf modelo.ltx

x:
	xpdf $(SRC).pdf
o:
	okular $(SRC).pdf
e:
	evince $(SRC).pdf
