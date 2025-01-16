import argparse
import os
from pypdf import PdfReader, PdfWriter

parser = argparse.ArgumentParser("Remove PDF pages")
parser.add_argument("file_name", type=str)
parser.add_argument("pages_to_remove", type=int, nargs="*")
args = parser.parse_args()

if len(args.pages_to_remove) < 1:
    raise RuntimeError("Input at least 1 page to remove")

if (str(args.file_name).lower().endswith(".pdf") == False):
    raise ValueError("File type must be pdf")


reader = PdfReader(args.file_name)
writer = PdfWriter()


for i in range(1, reader.get_num_pages() + 1):
    if i not in args.pages_to_remove:
        writer.add_page(reader.pages[i - 1])


base_name = args.file_name[:str(args.file_name).rfind(".")]
ext = ".pdf"
counter = 1
out_pdf_file_name = base_name + "-" + str(counter) + ext

while os.path.exists(out_pdf_file_name):
    counter += 1
    out_pdf_file_name = base_name + "-" + str(counter) + ext
    
with open(out_pdf_file_name, "wb") as fp:
    writer.write(fp)

print("Created " + out_pdf_file_name)