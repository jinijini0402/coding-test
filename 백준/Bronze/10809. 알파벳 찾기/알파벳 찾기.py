a=input()
ans=[-1]*26
for i in range(len(a)):
    idx=ord(a[i])-ord('a')
    if ans[idx]==-1:
        ans[idx]=i
for i in ans:
    print(i,end=' ')