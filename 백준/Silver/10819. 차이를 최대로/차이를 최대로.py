import sys
from itertools import permutations
input=sys.stdin.readline
n=int(input())
a=list(map(int,input().split()))
best=0
for p in permutations(a):
    s=0
    for i in range(n-1):
        s+=abs(p[i]-p[i+1])
    if s>best:
        best=s
print(best)