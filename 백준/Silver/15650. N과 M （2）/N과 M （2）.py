a,b=map(int,input().split())
stack=[]
def dfs(cur):
    if len(stack)==b:
        print(' '.join(map(str,stack)))
        return
    for i in range(cur,a+1):
        stack.append(i)
        dfs(i+1)
        stack.pop()
dfs(1)       