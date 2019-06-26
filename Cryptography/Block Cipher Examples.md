
```
from flask import Flask
from Crypto.Cipher import AES
import os

from secret import key6, flag6, key0, flag0

app = Flask(__name__)

#This server is running at http://ctf1.gel.webfactional.com

def read_cookie(cookie):
    #format: '{key1:value1,key2:value2}'
    answer={}
    for pair in cookie[1:-1].split(','):
        temp = pair.split(':')
        answer[temp[0]] = temp[1]
    return answer

@app.route('/')
def index():
    return 'Usage: /p0/getflag or /p0/decryptblock/:hexdigest OR /p6/cookie or p6/login/:hexdigest/:iv'

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

@app.route('/p6/cookie')
def getcookie():
    cookie='{nm:guest,flg:0}'
    randomiv = os.urandom(16)
    cipher = AES.new(key6, AES.MODE_CBC, randomiv)
    return randomiv.encode('hex') + cipher.encrypt(cookie).encode('hex')

@app.route('/p6/login/<hexdigest>/<iv>')
def checkcookie(hexdigest, iv):
    cipher = AES.new(key6, AES.MODE_CBC, iv.decode('hex'))
    rawcookie=cipher.decrypt(hexdigest.decode('hex'))
    cookie = read_cookie(rawcookie)
    if cookie['nm'] == 'admin' and cookie['flg'] == '1':
        return flag6
    else:
        return "Sorry, the flag must be read by the admin"
```
