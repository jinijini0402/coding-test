import sys
from collections import Counter
input=sys.stdin.readline
a=int(input())
d1=list(map(int,input().split()))
b=int(input())
d2=list(map(int,input().split()))
c=Counter(d1)
ans=[]
for i in d2:
    if i in c:
        ans.append(c[i])
    else:
        ans.append(0)
print(' '.join(map(str,ans)))