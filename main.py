from PIL import Image
from random import randint

char = 0

image = Image.new('1', (2, 4))
for y in range(image.height):
    for x in range(image.width):
        if(randint(0, 1) > 0):
            image.putpixel((x, y), 1)
image.save('test.bmp')
imagelist = list(image.getdata())
print(imagelist)

arrange = [7, 6, 5, 3, 1, 4, 2, 0]

for i in arrange:
    char = char << 1
    char = char | imagelist[i]

print(chr(0x2800 + char))