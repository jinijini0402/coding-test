from collections import deque
n=int(input())
d=[list(input().strip()) for _ in range (n)]
dx=[1,-1,0,0]
dy=[0,0,1,-1]
def bfs(sx,sy,visited,d):
    q=deque()
    q.append((sx,sy))
    visited[sx][sy]=True
    while q:
        x,y=q.popleft()
        for i in range(4):
            nx=x+dx[i]
            ny=y+dy[i]
            if nx<0 or nx>=n or ny<0 or ny>=n:
                continue
            if visited[nx][ny]:
                continue
            if d[nx][ny]!=d[x][y]:
                continue
            q.append((nx,ny))
            visited[nx][ny]=True
second=[row[:] for row in d]
for i in range (n):
    for j in range(n):
        if second[i][j]=='G':
            second[i][j]='R'
visited=[[False]*n for _ in range (n)]
cnt=0
for i in range(n):
    for j in range(n):
        if not visited[i][j]:
            bfs(i,j,visited,d)
            cnt+=1
print(cnt,end=' ')
visited=[[False]*n for _ in range (n)]
cnt=0
for i in range(n):
    for j in range(n):
        if not visited[i][j]:
            bfs(i,j,visited,second)
            cnt+=1
print(cnt)