import sys
input=sys.stdin.readline
from collections import Counter
N,M=map(int,input().split())
d=[]
for _ in range(N):
    w=input().strip()
    if len(w)>=M:
        d.append(w)
dic=Counter(d)
dic=sorted(dic.items(), key=lambda x: (-x[1],-len(x[0]),x[0]))
for a,b in dic:
    print(a)