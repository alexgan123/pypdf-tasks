import argparse

from pypdf import PdfReader


parser = argparse.ArgumentParser("Extract Images")
parser.add_argument("file_name", type=str)
parser.add_argument("page_number", type=int)
args = parser.parse_args()

if (str(args.file_name).lower().endswith(".pdf") == False):
    raise ValueError("File type must be pdf")


reader = PdfReader(args.file_name)

page = reader.pages[args.page_number - 1]

for count, image_file_object in enumerate(page.images):
    with open(
        str(args.file_name)[:str(args.file_name).rfind('.')]
        + "-page"
        + str(args.page_number)
        + "-"
        + str(count)
        + image_file_object.name,
        "wb",
    ) as fp:
        fp.write(image_file_object.data)
