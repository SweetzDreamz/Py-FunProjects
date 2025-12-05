from rembg import remove
from PIL import Image

input_path = 'your_image.png'
output_path = 'your_image.png'

inp = Image.open(input_path)
out = remove(inp)
out.save(output_path)

#Pillow usually comes with support for common formats like JPEG, PNG, GIF, BMP, and TIFF.
#To convert images to RGB mode use rgb_img = img.convert("RGB")
