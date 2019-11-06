#!/usr/bin/python3
# convert b/w bitmap image to hex string (1bit/px image)
import argparse
from PIL import Image
# parsing arguments
parser = argparse.ArgumentParser(description="Convert a bitmap icon 8x8px to a hexadecimal string (1bit/px) line by line")
parser.add_argument("imagefile", help="1bit/px bitmap image file")
args = parser.parse_args()
# convert image
img = Image.open(args.imagefile)
pixels = list(img.getdata())
c = 0  # varible to store one byte
s = ''
for i in range(len(pixels)):
    # gather bits in one byte
    if pixels[i] == 255:
        c |= 1 << (i % 8)
    # once a byte is complete, append to string and set to 0
    if ((i + 1) % 8) == 0:
        s += c.to_bytes(1, byteorder='little').hex()
        c = 0
print("\'" + args.imagefile.replace('.bmp','') + "\': ", "\'" + s + "\'")
