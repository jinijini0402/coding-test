s=input().upper()
d=list(set(s))
ans=[]
for i in d:
    ans.append(s.count(i))
m=max(ans)
cnt=0
for i in ans:
    if i==m:
        cnt+=1
if cnt>1:
    print('?')
else:
    print(d[ans.index(m)])