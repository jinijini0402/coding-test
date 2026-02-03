from math import gcd
from functools import reduce
n=int(input())
d=[int(input()) for _ in range (n)]
distance=[0]*(n-1)
for i in range(n-1):
    distance[i]=d[i+1]-d[i]
g=reduce(gcd, distance)
ans=0
for i in distance:
    ans+=i//g-1
print(ans)