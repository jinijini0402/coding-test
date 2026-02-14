import sys
sys.setrecursionlimit(10**6)
input=sys.stdin.readline

R,C,n=map(int,input().split())
d=[list(map(int,input().split())) for _ in range (n)]

visited=[[False]*C for _ in range (R)]
for x1,y1,x2,y2 in d:
    for r in range(y1,y2):
        for c in range(x1,x2):
            visited[r][c]=True

dx=[1,-1,0,0]
dy=[0,0,1,-1]

def dfs(x,y):
    visited[x][y]=True
    area=1
    for i in range (4):
        nx=x+dx[i]
        ny=y+dy[i]
        if 0<=nx<R and 0<=ny<C and not visited[nx][ny]:
            area+=dfs(nx,ny)
    return area

areas=[]
for i in range(R):
    for j in range(C):
        if not visited[i][j]:
            areas.append(dfs(i,j))

areas.sort()
print(len(areas))
print(' '.join(map(str,areas)))