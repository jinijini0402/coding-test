from collections import deque
n = int(input())

node = [[] for _ in range (n + 1)]
for _ in range (n - 1):
    a, b = map(int, input().split())
    node[a].append(b)
    node[b].append(a)

ans = [0] * (n + 1)
visited = [False] * (n + 1)
q = deque([1])
visited[1] = True
while q:
    a = q.popleft()
    
    for x in node[a]:
        if not visited[x]:
            visited[x] = True
            q.append(x)
            ans[x] = a
        
for i in range (2, n+1):
    print(ans[i])