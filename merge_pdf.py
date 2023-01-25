from PyPDF2 import PdfMerger

pdfs = ['HW1\PDFSolutions\Q1.26.pdf','HW1\PDFSolutions\Q2A-2.pdf','HW1\PDFSolutions\Q3.21.pdf','HW1\PDFSolutions\Q2A-3.pdf','HW1\PDFSolutions\Q4.007.pdf','HW1\PDFSolutions\Q4.75.pdf','HW1\PDFSolutions\Q4.009.pdf','HW1\PDFSolutions\Q6.77.pdf','HW1\PDFSolutions\Q6.145.pdf','HW1\PDFSolutions\Q6.007.pdf']

merger = PdfMerger()

for pdf in pdfs:
    merger.append(pdf)

merger.write("solutions.pdf")
merger.close()