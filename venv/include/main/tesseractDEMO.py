from PIL import Image
import pytesseract
#识别英语字母的pytesteract
image = Image.open( "../testImg/test.png" )
text = pytesseract.image_to_string(image)
print(text)