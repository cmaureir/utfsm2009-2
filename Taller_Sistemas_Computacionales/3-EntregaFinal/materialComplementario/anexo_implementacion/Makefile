SRCS=anexo

all:
	pdflatex $(SRCS).tex
	pdflatex $(SRCS).tex

clean:
	rm -f $(SRCS).{aux,bbl,blg,log,dvi,ps,out,snm,toc,nav} *~

distclean: clean
	rm -f $(SRCS).pdf

.PHONY: all clean distclean k
