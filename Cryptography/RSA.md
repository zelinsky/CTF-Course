### functions needed
```
def egcd(a,b):
	if a == 0:
		return b, 0, 1
	else:
		g,y,x=egcd(b%a,a)
		return(g, x-(b//a)*y, y)

def modinv(a,m):
	gcd,x,y = egcd(a,m)
	if gcd!=1:
		return none
	else:
		return x%m
```
### basics
-----
pick two strong primes, p and q.

multiply p and q and call the result N.

phi of a number is all of the numbers below that number. since N = (p)(q), phi(N) is (p-1)(q-1)

pick a prime (industry standard is 65337) and call that e.

check that gcd(e,p-1)=1 and gcd(e,q-1)=1

run your message through bytes_to_long() and call that m.

CT = m <sup>e</sup> % N

d = modinv(e,phi)

Plaintext = CT <sup>d</sup> % N
### attacks
---------
Small e is vulnerable to m <sup>e</sup> being smaller than N and you can just take the e root of m <sup>e</sup>

small e is also vulnerable to broadcast attacks where you multiply all the m <sup>e</sup> mod N together and all of the moduli together until m <sup>e</sup> is bigger than the moduli
