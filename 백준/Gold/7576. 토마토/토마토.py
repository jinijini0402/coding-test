from collections import deque
import sys
input = sys.stdin.readline

W, H = map(int, input().split())
d = [list(map(int, input().split())) for _ in range (H)]

q = deque()
for i in range (H):
    for j in range (W):
        if d[i][j] == 1:
            q.append((i, j))

dx = (1, -1, 0, 0)
dy = (0, 0, -1, 1)

while q:
    x, y = q.popleft()
    for k in range (4):
        nx = x + dx[k]
        ny = y + dy[k]
        if 0 <= nx < H and 0 <= ny < W:
            if d[nx][ny] == 0:
                q.append((nx, ny))
                d[nx][ny] = d[x][y] + 1
                
mx = 1
for i in range (H):
    for j in range (W):
        if d[i][j] == 0:
            print(-1)
            sys.exit(0)
        mx = max(mx, d[i][j])
print(mx - 1)