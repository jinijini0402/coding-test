import sys
input=sys.stdin.readline
n=int(input())
d=[int(input()) for _ in range (n)]
d.sort()
if n==0:
    print(0)
else:
    idx=int(n*0.15+0.5)
    print(int(sum(d[idx:n-idx])/(n-2*idx)+0.5))