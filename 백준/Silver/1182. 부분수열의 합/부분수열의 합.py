from itertools import combinations
N,S=map(int,input().split())
d=list(map(int,input().split()))
ans=0
for i in range(1,N+1):
    for j in combinations(d,i):
        if sum(j)==S:
            ans+=1
print(ans)