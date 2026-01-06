n=int(input())
need=int(input())
d=list(map(int,input().split()))
d.sort()
ans=0
p1,p2=0,n-1
while p1<p2:
    s=d[p1]+d[p2]
    if s==need:
        ans+=1
        p1+=1
        p2-=1
    elif s<need:
        p1+=1
    else:
        p2-=1
print(ans)
            