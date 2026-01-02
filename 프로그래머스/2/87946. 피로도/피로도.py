def solution(k, dungeons):
    l=len(dungeons)
    visited=[False]*l
    ans=0
    def dfs(fatigue,cnt):
        nonlocal ans
        if cnt>ans:
            ans=cnt
        for i in range(l):
            need,cost=dungeons[i]
            if not visited[i] and fatigue>=need:
                visited[i]=True
                dfs(fatigue-cost,cnt+1)
                visited[i]=False
    dfs(k,0)
    return ans