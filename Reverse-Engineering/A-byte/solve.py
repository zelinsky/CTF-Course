import codecs

m='69726275677a7631765e7831745e6a6f31765e65355e7640325e39693363403133387c'

ans=''
for i in range(len(m)//2):
    mm=int(m[i*2:i*2+2],16)^1
    ans+= hex(mm)[2:]
print(codecs.decode(ans,'hex'))
