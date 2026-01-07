n=int(input())
d=[list(map(int,input().split())) for _ in range (n)]
d.sort(key=lambda x:(x[1],x[0]))
ans=0
end=0
for s,e in d:
    if s>=end:
        ans+=1
        end=e
print(ans)