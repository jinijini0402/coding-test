n=int(input())
d=[list(map(int,input().split())) for _ in range (n)]
cnt=[0]*n
for i in range(n):
    for j in range (n):
        if i==j:
            continue
        for k in range (5):
            if d[i][k]==d[j][k]:
                cnt[i]+=1
                break
m=max(cnt)
print(cnt.index(m)+1)