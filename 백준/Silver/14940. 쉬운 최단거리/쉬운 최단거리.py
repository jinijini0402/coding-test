from collections import deque

H, W = map(int,input().split())
d = [list(map(int, input().split())) for _ in range (H)]

sx = -1
sy = -1
for i in range (H):
    for j in range (W):
        if d[i][j] == 2:
            sx, sy = i, j
            break
    if sx != -1:
        break

q = deque([(sx, sy)])
visited = [[-1]*(W) for _ in range (H)]
visited[sx][sy] = 0

dx = [1, -1, 0, 0]
dy = [0, 0, 1, -1]

while q:
    x, y = q.popleft()
    for k in range(4):
        nx = x+dx[k]
        ny = y+dy[k]
        
        if 0<=nx<H and 0<=ny<W:
            if visited[nx][ny]==-1 and d[nx][ny]==1:
                    visited[nx][ny] = visited[x][y]+1
                    q.append((nx, ny))

for i in range (H):
    for j in range (W):
        if d[i][j]==0:
            visited[i][j] = 0
            
for i in visited:
    print(' '.join(map(str, i)))