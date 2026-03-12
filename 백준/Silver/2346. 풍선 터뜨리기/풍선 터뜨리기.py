from collections import deque

n = int(input())
d = list(map(int, input().split()))

q = deque()
for i in range (n):
    q.append((i+1, d[i]))

ans = []

while q:
    idx, move = q.popleft()
    ans.append(idx)
    
    if not q:
        break
        
    if move > 0:
        q.rotate(-(move-1))
    else:
        q.rotate(-move)
    
print(' '.join(map(str, ans)))