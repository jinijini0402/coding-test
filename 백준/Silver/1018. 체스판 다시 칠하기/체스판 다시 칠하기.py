N,M=map(int,input().split())
d=[input().strip() for _ in range(N)]
ans=64
for i in range(N-7):
    for j in range(M-7):
        one,two=0,0
        for r in range(8):
            for c in range(8):
                cur=d[i+r][j+c]
                w='W' if (r+c)%2==0 else 'B'
                b='B' if (r+c)%2==0 else 'W'
                if cur!=w: one+=1
                if cur!=b: two+=1
        ans=min(one,two,ans)
print(ans)