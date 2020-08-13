from PyPDF2 import PdfFileMerger
from docx2pdf import convert
import glob

def PDFmerge(pdfs):
    merger = PdfFileMerger()

    for pdf in pdfs:
        merger.append(open(pdf, 'rb'))

    with open('C:\\Users\\Tzachi\\Desktop\\Cyber Course\\New folder\\CyberCourse.pdf', 'wb') as output:
        merger.write(output)

def main():
    convert("C:\\Users\\Tzachi\\Desktop\\Cyber Course\\New folder\\")
    pdfs = glob.glob("C:\\Users\\Tzachi\\Desktop\\Cyber Course\\New folder\\*.pdf")

    PDFmerge(pdfs=pdfs)
if __name__ == "__main__":
    main()