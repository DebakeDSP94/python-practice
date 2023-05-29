import PyPDF4
import re
import os

os.chdir('/home/stuart/Documents/automate_online_materials')
pdfFileObj = open('meetingminutes1.pdf', 'rb')  # read binary
pdfReader = PyPDF4.PdfFileReader(pdfFileObj)  # create reader object
num = pdfReader.numPages  # get number of pages
print(num)
pageObj = pdfReader.getPage(0)  # get page object
pageObj.extractText()  # extract text from page object
print(pageObj.extractText())

with open('meetingminutes1.pdf', 'rb') as pdfFileObj:  # read binary
    pdfReader = PyPDF4.PdfFileReader(pdfFileObj)  # create reader object
    pageObj = pdfReader.getPage(0)
    print(pageObj.extractText())
    for pageNum in range(pdfReader.numPages):
        print(pdfReader.getPage(pageNum).extractText())

pdf2File = open('meetingminutes2.pdf', 'rb')
pdf2Reader = PyPDF4.PdfFileReader(pdf2File)
writer = PyPDF4.PdfFileWriter()
for pageNum in range(pdfReader.numPages):
    pageObj = pdfReader.getPage(pageNum)
    writer.addPage(pageObj)
for pageNum in range(pdf2Reader.numPages):
    pageObj = pdf2Reader.getPage(pageNum)
    writer.addPage(pageObj)
outputFile = open('combinedminutes.pdf', 'wb')
writer.write(outputFile)
outputFile.close()
pdfFileObj.close()
pdf2File.close()
