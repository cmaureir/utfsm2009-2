SRCS=reporteTecnico

all:
	pdflatex $(SRCS).tex
	BIBINPUTS=. bibtex $(SRCS)
	pdflatex $(SRCS).tex
	pdflatex $(SRCS).tex

clean:
	rm -f $(SRCS).{aux,bbl,blg,log,dvi,ps,out,snm,toc,nav} *~

distclean: clean
	rm -f $(SRCS).pdf

.PHONY: all clean distclean k

x:
	xpdf $(SRCS).pdf
