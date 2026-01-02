from collections import deque
def solution(cacheSize, cities):
    if cacheSize==0:
        return len(cities)*5
    q=deque()
    time=0
    for i in cities:
        i=i.lower()
        if i in q:
            q.remove(i)
            q.append(i)
            time+=1
        else:
            if len(q)==cacheSize:
                q.popleft()
            q.append(i)
            time+=5
    return time