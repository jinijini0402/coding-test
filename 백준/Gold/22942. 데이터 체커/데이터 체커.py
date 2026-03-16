import sys
input = sys.stdin.readline

n = int(input())

points = []
for i in range (n):
    x, r = map(int, input().split())
    points.append((x-r, 0, i))
    points.append((x+r, 1, i))

points.sort()
stack = []
for i in range (n*2):
    if i > 0 and points[i][0] == points[i-1][0]:
        print("NO")
        sys.exit()
    
    pos, typ, idx = points[i]
    
    if typ == 0:
        stack.append(idx)
    else:
        if not stack or stack[-1] != idx:
            print("NO")
            sys.exit()
        stack.pop()
            
print("YES")