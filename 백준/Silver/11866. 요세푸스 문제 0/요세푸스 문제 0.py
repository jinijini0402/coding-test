n,k=map(int,input().split())
d=[i for i in range (1,n+1)]
ans=[]
idx=k-1
while d:
    ans.append(d.pop(idx))
    if d:
        idx=(idx+k-1)%len(d)
print("<"+', '.join(map(str,ans))+">")