from collections import deque
import sys
input = sys.stdin.readline

n = int(input())

adj = [[] for _ in range (n)]
for i in range (n):
    d = list(map(int,input().split()))
    for j in range (n):
        if d[j] == 1:
            adj[i].append(j)

for i in range (n):
    ans = [0]*n
    q = deque([i])
    
    while q:
        cur = q.popleft()
        for node in adj[cur]:
            if ans[node] == 0:
                q.append(node)
                ans[node] = 1
    
    print(' '.join(map(str,ans)))