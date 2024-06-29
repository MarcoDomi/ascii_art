from PIL import Image
from PIL import ImageOps

def create_ascii_image(img, f):
    width, height = img.size

    for i in range(height):
        for j in range(width):
            pixel_value = img.getpixel((j, i))
            if pixel_value in range(50):
                f.write("*")
            elif pixel_value in range(50, 100):
                f.write("#")
            elif pixel_value in range(100, 150):
                f.write("$")
            elif pixel_value in range(150, 200):
                f.write("%")
            elif pixel_value in range(200, 255):
                f.write("@")
        f.write('\n')


im = Image.open('monalisa.jpg')
size = im.size

gray_im = ImageOps.grayscale(im)

f = open("ascii_image.txt", 'w')
create_ascii_image(gray_im, f)
im.close()
f.close()
