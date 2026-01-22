d=[list(input()) for _ in range (5)]
ans=''
while any(d):
    for i in range(5):
        if d[i]:
            ans+=d[i].pop(0)
print(ans)