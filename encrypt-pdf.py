import argparse

from pypdf import PdfReader, PdfWriter


parser = argparse.ArgumentParser("Encrypt PDF")
parser.add_argument("file_name", type=str)
parser.add_argument("password", type=str)
args = parser.parse_args()

if (str(args.file_name).lower().endswith(".pdf") == False):
    raise ValueError("File type must be pdf")


reader = PdfReader(args.file_name)
writer = PdfWriter(clone_from=reader)

# Add a password to the new PDF
writer.encrypt(args.password, algorithm="AES-256")

# Save the new PDF to a file
with open(str(args.file_name), "wb") as f:
    writer.write(f)

print("Encrypted " + args.file_name)