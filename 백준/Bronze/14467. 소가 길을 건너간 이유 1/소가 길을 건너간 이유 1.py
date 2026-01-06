n=int(input())
d=[list(map(int,input().split())) for _ in range (n)]
dic=dict()
ans=0
for a,b in d:
    if a not in dic:
        dic[a]=b
    elif dic[a]!=b:
        ans+=1
        dic[a]=b
print(ans)