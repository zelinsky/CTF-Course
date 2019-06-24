# Intro to CTF's
Capture the flag as it pertains to our course is much different than the traditional capture the flag you may have played as a kid. In our CTF's, there is a flag hidden somewhere in a server, file, or website. You must use skills learned such as Forensics, Cryptography, Binary-Exploitation, and basic Linux to solve these "problems" to reveal the flag.
Most of the time, flags look like this format:
```
flag{l33t_sp34k-h3r3}
```
Certain categories of CTF's include:
- Cryptography
  - RSA Encryption
- Forensics
  - Steganography
  - Network Traffic
  - Grep
- Binary Exploitation
- Web Exploitation
- Reverse Engineering

### Cryptography Overview
Cryptography is when you take the flag in plaintext and jumble the text in a way that no longer can be understood by someone who intercepts the message, but is performed in an algorithmic way that can be undone by the intended reciever.

Classic Examples of Cryptography are the caesar cipher, rot-13, and the vigenere cipher.
```
synt{lBh_qVq_vG!}
```

#### RSA
RSA is a math based Encryption using prime numbers, exponentials, and modular arithmetic.
Try to decrypt this flag. 

```
e = 65537
p = 307
q = 487
N = 149509
d = 48833
ct = 141654L
```

### Forensics
Forensics includes finding files in linux servers, finding flags in corrupted files, or finding flags in pictures (Steganography)
### Binary Exploitation
Binary Exploitation is making a program do something that it's not meant to do.
### Web
Web CTF's inculde server traversal via a website, or being able to search manually for the flag via a multitude of tools.
### Reverse Engineeering
cbtnuggets.com: "Sometimes the flag will be a string hidden inside the application code. Depending on the challenge type and level of difficulty the task, you might need to use reverse engineering.

Reverse engineering challenges require an intimate knowledge debugger and disassembler software. The goal: Take a compiled binary, rip it apart, and find out how it works.

You will want to be familiar with how the application uses control flow, loops, and conditionals so that you can figure out how to bend the program to your will, and then hopefully capture the flag."



