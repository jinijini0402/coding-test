n=int(input())
d=[list(map(int,input().split())) for _ in range (n)]
res=[0]*n
for i in range(n):
    for j in range(n):
        if i==j:
            continue
        for a in range(5):
            if d[i][a]==d[j][a]:
                res[i]+=1
                break
print(res.index(max(res))+1)