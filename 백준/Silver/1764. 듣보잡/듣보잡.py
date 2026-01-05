a,b=map(int,input().split())
da=[input() for _ in range (a)]
db=set(input() for _ in range (b))
ans=[]
for i in da:
    if i in db:
        ans.append(i)
print(len(ans))
ans.sort()
for i in ans:
    print(i)