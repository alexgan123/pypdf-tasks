import argparse
from pypdf import PdfReader

parser = argparse.ArgumentParser("Extract PDF text")
parser.add_argument("file_name", type=str)
parser.add_argument("page_number", type=int)
args = parser.parse_args()

if str(args.file_name).lower().endswith(".pdf") == False:
    raise ValueError("File type must be pdf")


reader = PdfReader(args.file_name)
page = reader.pages[args.page_number - 1]
with open("extracted-text.txt", "w", encoding="utf-8") as f:
    f.write(page.extract_text())

print("Extracted text of page " + str(args.page_number) + " of " + args.file_name)
