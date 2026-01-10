n=int(input())
d=list(map(int,input().split()))
need=list(map(int,input().split()))
c=0
for i in d:
    c+=(i+need[0]-1)//need[0]
print(c)
print(str(n//need[1])+' '+str(n%need[1]))
