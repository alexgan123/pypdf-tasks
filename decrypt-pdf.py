import argparse

from pypdf import PdfReader, PdfWriter

parser = argparse.ArgumentParser("Decrypt PDF")
parser.add_argument("file_name", type=str)
parser.add_argument("password", type=str)
args = parser.parse_args()

if (str(args.file_name).lower().endswith(".pdf") == False):
    raise ValueError("File type must be pdf")


reader = PdfReader(args.file_name)

if reader.is_encrypted:
    reader.decrypt(args.password)
else:
    raise RuntimeError("File is already decrypted")

writer = PdfWriter(clone_from=reader)

# Save the new PDF to a file
with open(str(args.file_name), "wb") as f:
    writer.write(f)

print("Decrypted " + args.file_name)