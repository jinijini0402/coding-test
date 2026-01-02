from collections import deque
def solution(maps):
    n=len(maps[0])
    m=len(maps)
    visited=[[False]*n for _ in range(m)]
    
    q=deque()
    q.append((0,0,1))
    visited[0][0]=True
    
    while q:
        x,y,dist=q.popleft()
        if (x,y)==(m-1,n-1):
            return dist
        for dx,dy in [(1,0),(-1,0),(0,1),(0,-1)]:
            nx,ny=x+dx,y+dy
            if 0<=nx<m and 0<=ny<n:
                if maps[nx][ny]==1 and not visited[nx][ny]:
                    visited[nx][ny]=True
                    q.append((nx,ny,dist+1))
    return -1