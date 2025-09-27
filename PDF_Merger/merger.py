#This program is written to merge the pdf using os module and pypdf module in python.

from PyPDF2 import PdfWriter
import os

#Define output directory and name
output_dir = "D:\Python-Programs\Python-Programs\PDF_Merger"
output_filename = "merged-pdf.pdf"

#Join the directory and file (full_path)
output_path = os.path.join(output_dir, output_filename)

#Check if the directory exists or not
if not os.path.exists(output_dir):
    os.makedirs(output_dir)

#PDF writer
merger = PdfWriter()

#List the files in directory and merge only those with extension ".pdf"
files = [file for file in os.listdir() if file.endswith(".pdf")] 
for pdf in files:
    merger.append(pdf)


merger.write(output_path)
merger.close()

#Print the success
print(f"Successfully merged the PDF into: {output_path}")