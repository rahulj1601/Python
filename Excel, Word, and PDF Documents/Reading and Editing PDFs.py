import PyPDF2, os

pdfFile = open('meetingminutes1.pdf', 'rb') #read binary mode because PDFs are binary files
reader = PyPDF2.PdfFileReader(pdfFile)

print(reader.numPages) #number of pages is returned

page = reader.getPage(0)
print(page.extractText()) #gets the text in a string from page 0 indicated via above line

for pageNum in range(reader.numPages):
    print(reader.getPage(pageNum).extractText()) #iterates and prints all the text from the document


##############################################################################################################

pdf1File = open('meetingminutes1.pdf', 'rb')
pdf2File = open('meetingminutes2.pdf', 'rb')

reader1 = PyPDF2.PdfFileReader(pdf1File)
reader2 = PyPDF2.PdfFileReader(pdf2File)

writer = PyPDF2.PdfFileWriter()

for pageNum in range(reader1.numPages):
    page = reader1.getPage(pageNum) #looping through all pages in first pdf
    writer.addPage(page) #adding pages to writer document

for pageNum in range(reader2.numPages):
    page = reader2.getPage(pageNum) #looping through all pages in second pdf
    writer.addPage(page) #adding pages to writer document

outputFile = open('combinedminutes.pdf', 'wb') #write binary mode to create pdf file and save i
writer.write(outputFile)

outputFile.close()
pdf1File.close()
pdf2File.close()
