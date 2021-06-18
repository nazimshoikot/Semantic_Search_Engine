from PyPDF2 import PdfFileReader, PdfFileWriter

pdf_file_path = 'doc.pdf'
file_base_name = pdf_file_path.replace('.pdf', '')

#pass pdf through instance of PdfFileReader
pdf = PdfFileReader(pdf_file_path)

#enter page numbers you want to extract HERE 
page_range = [0,2]

#generate new instance of pdfFileWriter
pdfWriter = PdfFileWriter()


#create new pdf file with the desired page numbers
pages = [] 
for i in range(page_range[0], page_range[1]): 
    pages.append(i)

for page_num in pages:
    pdfWriter.addPage(pdf.getPage(page_num))

#Give name to file here
with open('{0}_subset.pdf'.format(file_base_name), 'wb') as f:
    pdfWriter.write(f)
    f.close()