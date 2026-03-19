from collections import deque
import sys
input = sys.stdin.readline

N, M, V = map(int, input().split())

graph = [[] for _ in range(N + 1)]

for _ in range (M):
    a, b = map(int, input().split())
    graph[a].append(b)
    graph[b].append(a)

for i in range (1, N + 1):
    graph[i].sort()

def dfs(v, visited):
    visited[v] = True
    print(v, end = ' ')
    
    for nxt in graph[v]:
        if not visited[nxt]:
            dfs(nxt, visited)

def bfs(start):
    visited = [False] * (N + 1)
    q = deque([start])
    visited[start] = True
    
    while q:
        x = q.popleft()
        print(x, end = ' ')
        
        for nxt in graph[x]:
            if not visited[nxt]:
                visited[nxt] = True
                q.append(nxt)

visited = [False] * (N + 1)
dfs(V, visited)
print()
bfs(V)