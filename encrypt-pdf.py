import argparse

from pypdf import PdfReader, PdfWriter


parser = argparse.ArgumentParser("Encrypt PDF")
parser.add_argument("file_name", type=str)
parser.add_argument("password", type=str)
args = parser.parse_args()

full_file_name = str(args.file_name)
extension = full_file_name[full_file_name.rfind('.'):]
output_file_name = full_file_name[:full_file_name.rfind('.')]

if (extension != ".pdf"):
    raise TypeError("File type must be pdf")


reader = PdfReader(args.file_name)
writer = PdfWriter(clone_from=reader)

# Add a password to the new PDF
writer.encrypt(args.password, algorithm="AES-256")

# Save the new PDF to a file
with open(output_file_name + "-p" + extension, "wb") as f:
    writer.write(f)