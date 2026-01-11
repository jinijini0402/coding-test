a,b=map(int,input().split())
u=1
d=1
for i in range(1,b+1):
    u*=a
    a-=1
    d*=i
print(u//d)