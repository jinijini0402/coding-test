n=int(input())
d=[int(input()) for _ in range (n)]
res=[]
ans=[]
idx=0
for i in range(1,n+1):
    res.append(i)
    ans.append('+')
    while res and idx<n and res[-1]==d[idx]:
        res.pop()
        ans.append('-')
        idx+=1
if idx !=n:
    print('NO')
else:
    for i in ans:
        print(i)