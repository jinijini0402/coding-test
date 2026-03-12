import sys
input = sys.stdin.readline

from collections import deque

n = int(input())

q = deque()

for _ in range(n):
    s = input().rstrip()

    if s == 'pop':
        if not q:
            print(-1)
        else:
            print(q.popleft())

    elif s == 'front':
        if not q:
            print(-1)
        else:
            print(q[0])

    elif s == 'back':
        if not q:
            print(-1)
        else:
            print(q[-1])

    elif s == 'size':
        print(len(q))

    elif s == 'empty':
        if not q:
            print(1)
        else:
            print(0)

    else:
        _, x = s.split()
        q.append(int(x))