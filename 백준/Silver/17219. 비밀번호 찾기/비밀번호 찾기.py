import sys
input=sys.stdin.readline
a,b=map(int,input().split())
d=dict(input().split() for _ in range (a))
for _ in range (b):
    find=input().strip()
    print(d[find])