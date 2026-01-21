l,k=map(int,input().split())
d=[i for i in range (1,l+1)]
ans=[]
idx=0
while d:
    idx+=k-1
    idx%=l
    ans.append(d.pop(idx))
    l-=1
print('<'+', '.join(map(str,ans))+'>')