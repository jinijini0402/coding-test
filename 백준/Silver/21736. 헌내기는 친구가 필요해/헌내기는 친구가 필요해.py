from collections import deque
import sys
input = sys.stdin.readline

H, W = map(int, input().split())
d = [list(input().rstrip()) for _ in range (H)]

sx = sy = -1
for i in range (H):
    for j in range (W):
        if d[i][j] == 'I':
            sx = i
            sy = j
            break
    if sx != -1:
        break

dx = (1, -1, 0, 0)
dy = (0, 0, 1, -1)

q = deque([(sx, sy)])
visited = [[False]*W for _ in range (H)]
visited[sx][sy] = True
ans = 0

while q:
    x, y = q.popleft()
    if d[x][y] == 'P':
        ans += 1
    
    for k in range (4):
        nx = x + dx[k]
        ny = y + dy[k]
        
        if 0 <= nx < H and 0 <= ny < W:
            if d[nx][ny] != 'X' and not visited[nx][ny]:
                visited[nx][ny] = True
                q.append((nx, ny))

if ans == 0:
    print('TT')
else:
    print(ans)