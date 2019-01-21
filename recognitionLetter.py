import cv2
import numpy as np
import pytesseract
from PIL import Image

# Path of working folder on Disk
src_path = "C:/Users/Basak/Desktop/TEZ/imageprocessing/"
pytesseract.pytesseract.tesseract_cmd = r'C:\Program Files (x86)\Tesseract-OCR\tesseract'



# Recognize text with tesseract for python
result = pytesseract.image_to_string(Image.open(src_path + "91.png"),config='--psm 10')

# Remove template file
#os.remove(temp)



print ('--- Start recognize text from image ---')
print (result)

print ("------ Done -------")
