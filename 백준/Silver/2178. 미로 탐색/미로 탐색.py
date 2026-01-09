import sys
input=sys.stdin.readline
from collections import deque
r,c=map(int, input().split())
maze=[list(map(int,input().strip())) for _ in range(r)]
dx=[1,-1,0,0]
dy=[0,0,1,-1]
q=deque()
visited=[[0]*c for _ in range (r)]
q.append((0,0))
visited[0][0]=1
while q:
    x,y=q.popleft()
    for i in range(4):
        nx=x+dx[i]
        ny=y+dy[i]
        if nx<0 or nx>=r or ny<0 or ny>=c:
            continue
        if visited[nx][ny]>0:
            continue
        if maze[nx][ny]==0:
            continue
        visited[nx][ny]=visited[x][y]+1
        q.append((nx,ny))
print(visited[r-1][c-1])