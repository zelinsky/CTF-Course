### basics
-----
pick two primes, p and q.

phi of a number is all of the numbers below that number. since N = p*q, phi(N) is (p-1)*(q-1)

pick a prime (industry standard is 65337) and call that e.

check that gcd(e,p-1)=1 and gcd(e,q-1)=1

multiply p and q and call the result N.

run your message through bytes_to_long() and call that m.

raise m ^ e mod N. call that CT.

### attacks
---------
Small e is vulnerable to m^e being smaller than N and you can just take the e root of m^e

small e is also vulnerable to broadcast attacks where you multiply all the m^e mod N together and all of the moduli together until m^e is 
bigger than the moduli
