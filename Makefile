list := "list.txt"
pdfDir := "pdf"
main := "man_pdf_producer.py"

.PHONY: all clean

all:
	python3 $(main) $(list)

clean:
	rm -r ${pdfDir}/*
