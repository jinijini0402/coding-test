from collections import deque
n=int(input())
d=[list(map(int,input().strip())) for _ in range(n)]
dx=[1,-1,0,0]
dy=[0,0,1,-1]
visited=[[False]*n for _ in range (n)]
size=[]
def bfs(sx,sy):
    q=deque()
    q.append((sx,sy))
    visited[sx][sy]=True
    cnt=1
    while q:
        x,y=q.popleft()
        for k in range (4):
            nx=x+dx[k]
            ny=y+dy[k]
            if nx<0 or nx>=n or ny<0 or ny>=n:
                continue
            if visited[nx][ny]:
                continue
            if d[nx][ny]==0:
                continue
            visited[nx][ny]=True
            q.append((nx,ny))
            cnt+=1
    return cnt
for i in range(n):
    for j in range(n):
        if d[i][j]==1 and not visited[i][j]:
            size.append(bfs(i,j))
size.sort()
print(len(size))
for i in size:
    print(i)