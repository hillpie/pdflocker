from PyPDF2 import PdfFileWriter, PdfFileReader
def secue_pdf(file, password):
  parser = PdfFileWriter()
  pdf = PdfFileReader(file)
  for page in range (pdf.numPages):
    parser.addPage(pdf.getPage(page))
  parser.encrypt(password)
  with open(f"encrypted_{file}", "wb") as f:
    parser.write(f)
    f.close()
  print(f"encrypted_{file} Created...")
if __name__ == "__main__":
  file = "Adobe Scan Nov 23, 2021.pdf"
  password = "willbuyteslastocks"
  secure_pdf(file, password)
