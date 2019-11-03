from PIL import Image 
import PIL.ImageGrab
from PIL import ImageGrab
import numpy as np
import cv2


i = Image.open('Stego.png')
iar = np.asarray(i)

def get_pixel_colour(i_x, i_y):	
	return PIL.ImageGrab.grab().load()[i_x, i_y]
 
#print("color :" , get_pixel_colour(0, 0))

img = ImageGrab.grab()
pixels = img.load()
width, height = img.size

print("size ", img.size)
print("size" , i.size)


colorred = 255


# this code seems to not work!!! 
#for i in range(width):
#    for j in range(height):        
#        if pixels[j,i] == (255,0,0,255):
#            print(pixels[j,i])

extracted_bin = []
with Image.open("Stego.png") as img:
    width, height = img.size
    
    for x in range(0, width):
        for y in range(0, height):
            pixel = list(img.getpixel((x, y)))
            for n in range(0,3):
                extracted_bin.append(pixel[n]&1)

data = "".join([str(x) for x in extracted_bin])


def bits2a(b):
    return ''.join(chr(int(''.join(x), 2)) for x in zip(*[iter(b)]*8))

print(bits2a(data))
