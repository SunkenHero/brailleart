from PIL import Image, ImageChops
from time import time

start_time = time()

height = 20

color = (255, 255, 255) #default white

color = (255, 0, 95) #color for debian.png
#color = (0, 200, 255) #color for arch.png

with Image.open("debian.png", "r") as image:
    image = image.convert("L")
    #image = ImageChops.invert(image) #needed when using arch.png
    image = image.point(lambda x: 0 if x < 1 else 1, '1')
    scale_height = height * 4
    original_width, original_height = image.size
    aspect_ratio = original_width / original_height
    scale_width = int(scale_height * aspect_ratio)
    width = scale_width / 4
    image = image.resize((scale_width, scale_height))
    if image.size[0] % 2 == 1:
        image = Image.new("RGB", (13 + 1, 8), (0, 0, 0)).paste(image, (0, 0))

print(f"\x1b[38;2;{color[0]};{color[1]};{color[2]}m", end="")
for y in range(height):
    for x in range(int(width * 2)):
        char = 0
        croped = image.crop((x * 2, y * 4, x * 2 + 2, y * 4 + 4))
        imagelist = list(croped.getdata())

        for i in [7, 6, 5, 3, 1, 4, 2, 0]:
            char = char << 1 | imagelist[i]
        print(chr(0x2800 + char), end="")
    print("")
print("\x1b[0m", end="")
print(f"Time: {(time() - start_time) * 1000:.1f}ms")