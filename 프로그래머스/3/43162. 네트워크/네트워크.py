def solution(n, computers):
    visited=[False]*n
    ans=0
    def dfs(idx):
        for i in range (n):
            if not visited[i] and computers[idx][i]==1:
                visited[i]=True
                dfs(i)
    for i in range (n):
        if not visited[i]:
            dfs(i)
            ans+=1
    return ans