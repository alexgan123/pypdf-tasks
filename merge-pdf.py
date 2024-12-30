import argparse

from pypdf import PdfWriter

parser = argparse.ArgumentParser("Merge PDF")
parser.add_argument("pdf_files", nargs="*")
args = parser.parse_args()

for pdf in args.pdf_files:
    full_file_name = str(pdf)
    extension = pdf[pdf.rfind('.'):]
    output_file_name = pdf[:pdf.rfind('.')]

    if (extension != ".pdf"):
        raise TypeError("File types must all be pdf")


merger = PdfWriter()

for pdf in args.pdf_files:
    merger.append(pdf)

merger.write("merged-pdf.pdf")
merger.close()