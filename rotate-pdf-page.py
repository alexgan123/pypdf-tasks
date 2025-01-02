import argparse

from pypdf import PdfReader, PdfWriter

parser = argparse.ArgumentParser("Rotate PDF page")
parser.add_argument("file_name", type=str)
parser.add_argument("page_number", type=int)
parser.add_argument("rotate_count", type=int, help="Number of times to rotate the page clockwise")

args = parser.parse_args()

full_file_name = str(args.file_name)
extension = full_file_name[full_file_name.rfind('.'):]
output_file_name = full_file_name[:full_file_name.rfind('.')]

if (extension.lower() != ".pdf"):
    raise ValueError("File type must be pdf")


reader = PdfReader(args.file_name)
writer = PdfWriter(clone_from=reader)

writer.pages[args.page_number - 1].rotate(90 * args.rotate_count)

with open(str(args.file_name), "wb") as fp:
    writer.write(fp)

print(args.file_name + " page " + str(args.page_number) + " - rotated " + str(90 * args.rotate_count) + " degrees clockwise")