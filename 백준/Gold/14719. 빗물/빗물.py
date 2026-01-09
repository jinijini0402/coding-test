r, c = map(int, input().split())
h = list(map(int, input().split()))
ans = 0
for i in range(1, c-1):
    left = max(h[:i])
    right = max(h[i+1:])
    water = min(left, right) - h[i]
    if water > 0:
        ans += water
print(ans)