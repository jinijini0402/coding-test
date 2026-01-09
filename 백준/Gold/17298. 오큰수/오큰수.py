n=int(input())
d=list(map(int,input().split()))
ans=[-1]*n
stack=[]
for i in range(n):
    if not stack:
        stack.append(i)
    else:
        while True:
            if not stack or d[stack[-1]]>=d[i]:
                break
            else:
                ans[stack.pop()]=d[i]
        stack.append(i)
print(' '.join(map(str,ans)))