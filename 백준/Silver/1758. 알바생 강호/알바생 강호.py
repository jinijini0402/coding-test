n = int(input())
d = [int(input()) for _ in range (n)]

d.sort(reverse=True)

ans = 0
for i, v in enumerate(d):
    if v - i > 0:
        ans += v - i

print(ans)