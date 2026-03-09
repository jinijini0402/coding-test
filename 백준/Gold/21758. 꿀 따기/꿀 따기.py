n = int(input())
d = list(map(int, input().split()))

pre = [0] * n
pre[0] = d[0]
for i in range(1, n):
    pre[i] = pre[i-1] + d[i]

ans = 0
total = pre[-1]

for i in range(1, n-1):
    #벌통이 맨 오른쪽
    ans = max(ans, total - d[0] - d[i] + total - pre[i])
    #벌통이 맨 왼쪽
    ans = max(ans, pre[-2] - d[i] + pre[i-1])
    #벌통이 중앙
    ans = max(ans, total - d[0] - d[-1] + d[i])
    
print(ans)