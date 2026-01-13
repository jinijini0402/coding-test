import sys
input=sys.stdin.readline
from collections import Counter
n=int(input())
d=[int(input()) for _ in range(n)]
d.sort()
avr=sum(d)/n
if avr>=0:
    print(int(avr+0.5))
else:
    print(int(avr-0.5))
print(d[n//2])
c=Counter(d)
freq=max(c.values())
modes=[x for x in c if c[x]==freq]
modes.sort()
print(modes[1] if len(modes)>1 else modes[0])
print(d[-1]-d[0])