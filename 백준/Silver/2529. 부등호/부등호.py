import sys
input=sys.stdin.readline
n=int(input())
d=list(input().split())
visited=[False]*10
ans=[]
def check(a,b,s):
    if s=='<':
        return a<b
    else:
        return a>b
def dfs(depth,path):
    if depth==n+1:
        ans.append(''.join(map(str,path)))
        return
    for i in range(10):
        if not visited[i]:
            if depth==0 or check(path[-1],i,d[depth-1]):
                visited[i]=True
                dfs(depth+1,path+[i])
                visited[i]=False
dfs(0,[])
ans.sort()
print(ans[-1])
print(ans[0])