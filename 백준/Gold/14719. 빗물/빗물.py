r,c=map(int,input().split())
d=list(map(int,input().split()))
ans=0
for i in range (1,r+1):
    check=False
    t=0
    for j in range (c):
        if d[j]>=i:
            if check:
                ans+=t
                t=0
            else:
                check=True
        else:
            if check:
                t+=1
print(ans)