import argparse

from pypdf import PdfReader


parser = argparse.ArgumentParser("Extract Images")
parser.add_argument("file_name", type=str)
parser.add_argument("page_number", type=int)
args = parser.parse_args()

full_file_name = str(args.file_name)
extension = full_file_name[full_file_name.rfind('.'):]
output_file_name = full_file_name[:full_file_name.rfind('.')]

if (extension != ".pdf"):
    raise TypeError("File type must be pdf")


reader = PdfReader(args.file_name)

page = reader.pages[args.page_number - 1]

for count, image_file_object in enumerate(page.images):
    with open(
        output_file_name
        + "-page"
        + str(args.page_number)
        + "-"
        + str(count)
        + image_file_object.name,
        "wb",
    ) as fp:
        fp.write(image_file_object.data)
