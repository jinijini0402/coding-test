from collections import deque
R,C=map(int,input().split())
graph=[list(map(int,input().split())) for _ in range (R)]
visited=[[False]*C for _ in range (R)]
dx=[1,-1,0,0]
dy=[0,0,1,-1]
ans1=0
ans2=0
def bfs(sx,sy):
    q=deque()
    q.append((sx,sy))
    visited[sx][sy]=True
    cnt=1
    while q:
        x,y=q.popleft()
        for i in range(4):
            nx=x+dx[i]
            ny=y+dy[i]
            if 0<=nx<R and 0<=ny<C:
                if not visited[nx][ny] and graph[nx][ny]==1:
                    visited[nx][ny]=True
                    q.append((nx,ny))
                    cnt+=1
    return cnt
for i in range (R):
    for j in range (C):
        if not visited[i][j] and graph[i][j]==1:
            ans1+=1
            size=bfs(i,j)
            ans2=max(ans2,size)
print(ans1)
print(ans2)