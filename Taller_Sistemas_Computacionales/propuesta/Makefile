SRCS=propuesta
all:
	pdflatex $(SRCS).tex
	BIBINPUTS=. bibtex $(SRCS)
	pdflatex $(SRCS).tex

clean:
	rm -f $(SRCS).{aux,bbl,blg,log,dvi,ps,out,snm,toc,nav} *~

distclean: clean
	rm -f $(SRCS).pdf

.PHONY: all clean distclean k

k:
	@echo "Opening $(SRCS).pdf with kpdf..."
	@kpdf $(SRCS).pdf &> /dev/null &
x:
	@echo "Opening $(SRCS).pdf with xpdf..."
	@xpdf $(SRCS).pdf &> /dev/null &
