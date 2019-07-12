# Hashing

### What's a Hash?
Play around for a bit with [this program](https://codepen.io/AndyNovo/pen/qqdLdG) to determine the properties of a hash function.

So you can probably tell now that a hash function is a deterministic "scrambler" of some input. You pass in an arbitrary length input, and you get fixed-length output (the hash) that you cannot determine the input from. Everytime you run the same hash function n the same input, you get the same output.

Here are a few more proprties of a good hash function:
* Hash functions do not use a key. A key is a secret bit of information which let's you decrypt some encrypted message. In the case of hash functions it should be pretty much impossible to "decrypt"/"reverse" a hash.
* Crytographic hash functions should be hard to invert. That is, given h(s) but not s, it should be computationally expensive to find s.
* Hash functions should be fast to compute.
* Given an input and the hash of that input, it should be hard to compute a second message which hashes to the same value. That is, given x1,h(x1) it should be hard to compute x2 such that h(x1)==h(x2).
* It should be hard to find any two inputs that hash to the same thing.


### What Are Hashes Used For?
* Digital signatures
* Checksums
* Message Authentication Codes (MACs)
* Password storage


### Common Hash Functions
* MD5 & SHA-1 - **WEAK**
  * Vulnerable to collisions
  * Vulnerable to length extension attacks
* SHA-2
  * Vulnerable to length extension attacks
* SHA-3

### Vulnerabilities
#### Collisions
Collisions happen when two different pieces of data hash to the same value.

Why is this bad?

#### Length Extension Attacks
Before we get into this attack, you should understand the concept of a Message Authenication Code, or a MAC. MACs are sort of like hashes with keys. There is a secret key that both the sender and recevier know. For some message, the sender generates a MAC using a hash function and the key. The receiver can then verify that the message is unaltered and came from the sender by generating a MAC for the received message using the same hash function and key. If the two MACs are the same, the message is verified.

Now let's look at a MAC scheme that is vulnerable to a legnth extension attack:
* MAC = H(k+m) _i.e. take the **H**ash of the **m**essage prepended with our **k**ey_

We can easily forge signatures with this scheme using programs like [HashPump](https://github.com/bwall/HashPump) or [hlextend](https://github.com/stephenbradshaw/hlextend).
