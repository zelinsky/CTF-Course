from PIL import Image
from Crypto.Util.number import *
im = Image.open('lsb_steg.png')
values = list(im.getdata())
values = [v for t in values for v in t]
binary = ''
for v in values:
    binary += bin(v)[-1]
i = int(binary, 2)
flag = long_to_bytes(i)
print flag
