#!/usr/bin/python3
# convert b/w bitmap image to bin (1bit/px image)
import argparse
from PIL import Image

parser = argparse.ArgumentParser(description="Convert a bitmap logo 128x32px to a raw binary file (1bit/px)")
parser.add_argument("imagefile", help="1bit/px bitmap image file")
args = parser.parse_args()

img = Image.open(args.imagefile)
print("opening file \"",args.imagefile,"\"")
pixels = list(img.getdata())
c = 0  # varible to store one byte
f = open(args.imagefile.replace('.bmp','.bin'), 'wb')
print("converting image to bin")
for i in range(len(pixels)):
    # gather bits in one byte
    if pixels[i] == 255:
        c |= 1 << (i % 8)
    # once a byte is complete, write it and set it to 0
    if ((i + 1) % 8) == 0:
        f.write(c.to_bytes(1, byteorder='little'))
        c = 0
f.close()
print("done")
