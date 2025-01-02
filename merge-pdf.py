import argparse
import os
from pypdf import PdfWriter

parser = argparse.ArgumentParser("Merge PDF")
parser.add_argument("pdf_files", type=str, nargs="*")
args = parser.parse_args()

if len(args.pdf_files) < 2:
    raise RuntimeError("Input at least 2 pdf files")

for pdf in args.pdf_files:
    full_file_name = str(pdf)
    extension = pdf[pdf.rfind('.'):]
    output_file_name = pdf[:pdf.rfind('.')]

    if (extension.lower() != ".pdf"):
        raise ValueError("File types must all be pdf")


merger = PdfWriter()

for pdf in args.pdf_files:
    merger.append(pdf)

base_name = "merged"
ext = ".pdf"
merged_pdf_file_name = base_name + ext
counter = 1

while os.path.exists(merged_pdf_file_name):
    merged_pdf_file_name = base_name + "-" + str(counter) + ext
    counter += 1
    
merger.write(merged_pdf_file_name)
merger.close()

print("Created " + merged_pdf_file_name)