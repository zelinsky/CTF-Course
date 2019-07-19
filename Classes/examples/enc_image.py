from PIL import Image
from Crypto import Random
from Crypto.Cipher import AES
import os

im = Image.open('heckert_gnu.png')
image_bytes = im.tobytes()
image_mode = im.mode
image_size = im.size

ecb_key = os.urandom(16)
ecb = AES.new(ecb_key)
enc_bytes = ecb.encrypt(image_bytes)
Image.frombytes(image_mode, image_size, enc_bytes).save('ecb_image.png')

cbc_key = os.urandom(16)
iv = os.urandom(16)
cbc = AES.new(cbc_key, AES.MODE_CBC, iv)
enc_bytes = cbc.encrypt(image_bytes)
Image.frombytes(image_mode, image_size, enc_bytes).save('cbc_image.png')
