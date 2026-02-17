n=int(input())
d=list(map(int,input().split()))

stack=[]
ans=[0]*n

for i, h in enumerate(d):
    while stack and stack[-1][1]<h:
        stack.pop()
    if stack:
        ans[i]=stack[-1][0]+1
    else:
        ans[i]=0
    stack.append((i,h))

print(' '.join(map(str,ans)))