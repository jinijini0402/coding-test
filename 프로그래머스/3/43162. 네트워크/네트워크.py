def solution(n, computers):
    visited=[False]*n
    ans=0
    def dfs(i):
        visited[i]=True
        for j in range(n):
            if computers[i][j]==1 and not visited[j]:
                dfs(j)
    for i in range(n):
        if not visited[i]:
            dfs(i)
            ans+=1
    return ans