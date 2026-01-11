import sys
input=sys.stdin.readline
n=int(input())
d=[list(map(int,input().split())) for _ in range (n)]
d.sort(key=lambda x:(x[0],x[1]))
for a,b in d:
    print(str(a)+' '+str(b))