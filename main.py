import easyocr

image_path = 'image.jpeg'

reader = easyocr.Reader(['en'], gpu = False)
result = reader.readtext(image_path)
print(result)
