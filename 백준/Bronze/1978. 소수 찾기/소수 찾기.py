a=int(input())
b=list(map(int,input().split()))
ans=0
for i in b:
    if i<2:
        continue
    n=int(i**0.5)
    t=True
    for j in range(2,n+1):
        if i%j==0:
            t=False
            break
    if t: ans+=1
print(ans)