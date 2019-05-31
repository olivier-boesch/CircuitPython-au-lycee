#!/usr/bin/python3
# convert b/w bitmap image to bin (1bit/px image)
from PIL import Image

img = Image.open('logo.bmp')
pixels = list(img.getdata())
c = 0
f = open('logo.bin', 'wb')
for i in range(len(pixels)):
    if pixels[i] == 255:
        c |= 1 << (i % 8)
    if ((i + 1) % 8) == 0:
        f.write(c.to_bytes(1, byteorder='little'))
        c = 0
f.close()
