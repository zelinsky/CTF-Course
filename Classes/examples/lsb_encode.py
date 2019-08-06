from PIL import Image
from Crypto.Util.number import *
im = Image.open('hen.png')
values = list(im.getdata())
flag = "hello"
binary = bin(bytes_to_long(flag))[2:]
binary = (8-(len(binary) % 8))*'0' + binary
                
values = [v for t in values for v in t]
def encode(values, binary):
    i = 0
    new_values = []
    for v in values:
        b = bin(v)[:-1] + binary[i]
        new_values.append(int(b, 2))
        i += 1
        if i == len(binary):
            new_values.extend(values[i:])
            return new_values
        
new_values = encode(values, binary)
it = iter(new_values)
new_values = zip(it, it, it)
im2 = Image.new(im.mode, im.size)
im2.putdata(new_values)
im2.save('lsb_steg.png')
