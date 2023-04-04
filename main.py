import tkinter.filedialog
from PyPDF2 import PdfWriter
from pathlib import Path

if __name__ == '__main__':

    print("Pdf merger by Sanjeev")
    askopenfilenames = tkinter.filedialog.askopenfilenames()
    # print(askopenfilenames)

merger = PdfWriter()

for pdf in askopenfilenames:
    merger.append(pdf)

downloads_path = str(Path.home() / "Downloads")

newPdfName = input("enter name of new pdf :")
if newPdfName.endswith(".pdf"):
    newPdfName = str(downloads_path+newPdfName)
else:
    newPdfName = str(downloads_path+"/" + newPdfName+".pdf")

# print(newPdfName)
merger.write(newPdfName)
merger.close()