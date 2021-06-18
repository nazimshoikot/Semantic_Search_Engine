try:
    from PIL import Image
except ImportError:
    import Image
import pytesseract
import os 

inpath = "./images/"
outpath = "./images_text/"

def ocr_core(filename):
    # This function will handle the core OCR processing of images.
  
    text = pytesseract.image_to_string(Image.open(os.path.join(inpath, filename)))  
    return text

# loop through a directory of images and perform OCR
# the file content will be written to text file of the same name

for file in os.listdir(inpath): 
    data = ocr_core(file)
    outfilename  = file.split('.', 1)[0]
    outfilename = outfilename+".txt"
    outfile = open(os.path.join(outpath, outfilename), "w")
    outfile.write(data)
    outfile.close()