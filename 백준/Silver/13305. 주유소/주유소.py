n=int(input())
c=list(map(int,input().split()))
need=list(map(int,input().split()))
idx=0
ans=0
for i in range(n-1):
    if need[i]<need[idx]:
        idx=i
    ans+=need[idx]*c[i]
print(ans)