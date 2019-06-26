**Problem 0: hosted at http://ctf1.gel.webfactional.com**
```
from flask import Flask
from Crypto.Cipher import AES
import os

from secret import key6, flag6, key0, flag0

app = Flask(__name__)

#This server is running at http://ctf1.gel.webfactional.com

@app.route('/')
def index():
    return 'Usage: /p0/getflag or /p0/decryptblock/:hexdigest
    
@app.route('/p0/getflag')
def getflag():
    randomiv = os.urandom(16)
    cipher = AES.new(key0, AES.MODE_CBC, randomiv)
    assert(len(flag0) == 48)
    return randomiv.encode('hex') + cipher.encrypt(flag0).encode('hex')

@app.route('/p0/decryptblock/<hexdigest>')
def decrypt(hexdigest):
    cipher = AES.new(key0, AES.MODE_ECB)
    return cipher.decrypt(hexdigest.decode('hex')).encode('hex')
```
