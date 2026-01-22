from collections import deque
n=int(input())
d=[list(input().split()) for _ in range (n)]
dq=deque()
for i in d:
    if i[0]=='push_front':
        dq.appendleft(i[1])
    elif i[0]=='push_back':
        dq.append(i[1])
    elif i[0]=='pop_front':
        if not dq:
            print(-1)
        else:
            print(dq.popleft())
    elif i[0]=='pop_back':
        if not dq:
            print(-1)
        else:
            print(dq.pop())
    elif i[0]=='size':
        print(len(dq))
    elif i[0]=='empty':
        if not dq:
            print(1)
        else:
            print(0)
    elif i[0]=='front':
        if not dq:
            print(-1)
        else:
            print(dq[0])
    elif i[0]=='back':
        if not dq:
            print(-1)
        else:
            print(dq[-1])