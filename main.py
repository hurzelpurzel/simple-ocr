from pdf2image import convert_from_path
from PIL import Image
import pytesseract
import sys


def readImage(filename):
    print(pytesseract.image_to_string(Image.open(filename)))

def readPdf(filename):
   #pdf to image
   pages = convert_from_path(filename,500)
   for count, page in enumerate(pages):
     page.save(f'/tmp//out{count}.jpg', 'JPEG')
     readImage(f'/tmp/out{count}.jpg')



def main():
    args = sys.argv[1:]
    if len(args) == 1:
      filename = args[0]
      if filename.endswith('.pdf'):   
        readPdf(filename)
      else:
        readImage(filename)
    else:
        print ("Please provide a filename")
    

if __name__ == "__main__":
    main()
