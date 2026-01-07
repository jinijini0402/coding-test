a,b=map(int,input().split())
da=[input() for _ in range(a)]
db=[input() for _ in range(b)]
ans=0
for i in db:
    if i in da:
        ans+=1
print(ans)