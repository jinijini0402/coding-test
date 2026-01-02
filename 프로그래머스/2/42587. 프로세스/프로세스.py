from collections import deque
def solution(priorities, location):
    q=deque((v,i) for i,v in enumerate(priorities))
    ans=0
    while q:
        p,i=q.popleft()
        if any(p2>p for p2,_ in q):
            q.append((p,i))
        else:
            ans+=1
            if i==location:
                return ans