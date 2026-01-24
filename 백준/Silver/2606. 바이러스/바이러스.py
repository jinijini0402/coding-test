from collections import deque
computer=int(input())
edge=int(input())
graph=[[] for _ in range (computer+1)]
for _ in range(edge):
    a,b=map(int,input().split())
    graph[a].append(b)
    graph[b].append(a)
d=deque([1])
ans=set()
ans.add(1)
while d:
    cur=d.popleft()
    for nxt in graph[cur]:
        if nxt not in ans:
            d.append(nxt)
            ans.add(nxt)
print(len(ans)-1)