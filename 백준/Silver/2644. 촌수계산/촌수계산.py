from collections import deque
import sys
input = sys.stdin.readline

people = int(input())
start, end = map(int,input().split())
n = int(input())

graph = [[] for _ in range (people+1)]
for _ in range (n):
    a, b = map(int,input().split())
    graph[a].append(b)
    graph[b].append(a)

visited = [-1]*(people+1)
q = deque([start])
visited[start] = 0

while q:
    cur = q.popleft()
    if cur == end:
        break
    for nxt in graph[cur]:
        if visited[nxt] == -1:
            visited[nxt] = visited[cur]+1
            q.append(nxt)
            
print(visited[end])