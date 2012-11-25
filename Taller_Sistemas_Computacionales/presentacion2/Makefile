#Este es un make
SRCS=presentacion

all:
	@pdflatex $(SRCS).tex
	@pdflatex $(SRCS).tex
	@echo "moviendo PDF al directorio bin/ "
	@rm -rf *.{aux,log,dvi,ps,out,toc,nav,snm,vrb} src/*.aux

x:
	xpdf $(SRCS).pdf &> /dev/null

clean:
	@echo "limpiando..."
	@rm -rf *.{aux,log,dvi,ps,out,toc,nav,snm,vrb}
distclean: clean
	@ echo "borrando PDF..."
	@rm -rf *.pdf bin/*.pdf
