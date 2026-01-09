from collections import deque
N,K=map(int,input().split())
MAX=100000
visited=[-1]*(MAX+1)
q=deque()
q.append(N)
visited[N]=0
while q:
    x=q.popleft()
    if x==K:
        print(visited[x])
        break
    for nx in (x+1, x-1, x*2):
        if nx<0 or nx>MAX:
            continue
        if visited[nx]!=-1:
            continue
        visited[nx]=visited[x]+1
        q.append(nx)