from pwn import *
import hashlib

r = remote('52.15.140.126', 7001) # Connect to challenge

# Level 1 - Compute SHA-1 hashes
for i in range(10): # Range determined by trial and error, run below loop until it fails
    print r.recvuntil('sha1(') # Recv up until word
    word = r.recvuntil(')')[:-1] # Recv word, trim ')'
    print 'word: {}'.format(word)
    myhash = hashlib.sha1(word).hexdigest() # Get hash
    print myhash
    r.recv() # Recv rest of server output
    r.sendline(myhash) # Send hash

# Level 2 - Compute SHA-256 hashes
for i in range(10):
    print r.recvuntil('sha256(') # Recv up until word
    word = r.recvuntil(')')[:-1] # Recv word, trim ')'
    print 'word: {}'.format(word)
    myhash = hashlib.sha256(word).hexdigest() # Get hash
    r.recv() # Recv rest of server output
    r.sendline(myhash) # Send hash

# Get list of dictionary words for Level 3
f = open('dictionary.txt', 'r')
words = [word.strip() for word in f]
f.close()

# Level 3 - Find dictionary words for given SHA-256 hexdigest
for i in range(10):
    print r.recvuntil('== ') # Recv until hexdigest
    digest = r.recvuntil('\n')[:-1] # Recv hexdigest, '\n'
    print 'digest: {}'.format(digest)
    for w in words: # For each word in our dictionary
        if hashlib.sha256(w).hexdigest() == digest: # Check if the hash of the word is equal to the hexdigest we recevied
            print w
            r.recv() # Recv rest of server output
            r.sendline(w) # Send word
            
# Generate all possible 4-letter strings (only lowercase letters) for Level 4
from string import ascii_lowercase
import itertools
words = [''.join(c) for c in itertools.product(ascii_lowercase, repeat=4)]

# Level 4 - Brute force 4-letter lowercase strings for given MD5 hash
for i in range(10):
    print r.recvuntil('== ') # Recv until hexdigest
    digest = r.recvuntil(',')[:-1] # Recv hexdigest
    print 'digest: {}'.format(digest)
    for w in words: # For each string in 4-letter list
        if hashlib.md5(w).hexdigest() == digest: # Check if the hash of the word is equal to the hexdigest we recevied
            print w
            r.recv() # Recv rest of server output
            r.sendline(w) # Send word

# Receive flag
print r.recv()

