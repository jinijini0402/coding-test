from collections import deque
n=int(input())
d=[list(map(int,input().split())) for _ in range (n)]
dx=[1,-1,0,0]
dy=[0,0,1,-1]
count=[]
def bfs(sx,sy,h,visited):
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
            if d[nx][ny]<=h:
                continue
            q.append((nx,ny))
            visited[nx][ny]=True
mx=max(map(max,d))
for h in range (0,mx):
    visited=[[False]*n for _ in range (n)]
    cnt=0
    for i in range (n):
        for j in range (n):
            if d[i][j]>h and not visited[i][j]:
                bfs(i,j,h,visited)
                cnt+=1
    count.append(cnt)
print(max(count))