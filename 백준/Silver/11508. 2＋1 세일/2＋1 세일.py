n = int(input())
d = [int(input()) for _ in range (n)]

d.sort(reverse=True)

ans = 0
for i in range (1, n+1):
    if i % 3 != 0:
        ans += d[i-1]
        
print(ans)