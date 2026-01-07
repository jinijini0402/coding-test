from collections import deque
n=int(input())
d=[list(input().split()) for _ in range(n)]
X=deque()
for i in d:
    if i[0]=='push':
        X.append(i[1])
    elif i[0]=='pop':
        print(X.popleft() if X else -1)
    elif i[0]=='size':
        print(len(X))
    elif i[0]=='empty':
        print(0 if X else 1)
    elif i[0]=='front':
        print(X[0] if X else -1)
    elif i[0]=='back':
        print(X[-1] if X else -1)