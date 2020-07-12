
import PyPDF2, os

os.chdir(r'C:\Users\erich\Desktop\Python')

# Open PDF in "Read Binary" mode and create File Object
pdfFileObject = open(r'BLK_FI_Template.pdf','rb')

# File Object can be read by PyPDF2 per below
reader = PyPDF2.PdfFileReader(pdfFileObject)
pages = reader.numPages   # return # of pages
samplePage = reader.getPage(0)   # return page content
samplePageText = samplePage.extractText()   # extract Text of page
print(str(pages) + '\n hi ' + str(samplePageText))

# Loop through and print all pages
for i in range(reader.numPages):
    print(str(reader.getPage(i).extractText()))
    
# Editting at page level using PyPDF
pdfFileObject2 = open(r'BLK_FI_Template2.pdf','rb')
reader2 = PyPDF2.PdfFileReader(pdfFileObject2)
writer = PyPDF2.PdfFileWriter()

for page in range(reader.numPages): # for each page in File OBject Reader
    page = reader.getPage(page) # call the page content 
    writer.addPage(page) # and add to the temporary file
for page in range(reader2.numPages):
    page2 = reader2.getPage(page)
    writer.addPage(page2)

# Saving the new amended PDF file
outputFile = open(r'BLK_FI_Combined.pdf','wb')
writer.write(outputFile)
outputFile.close()
