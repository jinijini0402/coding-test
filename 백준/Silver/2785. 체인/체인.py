n = int(input())
d = list(map(int,input().split()))
d.sort()

left = 0
right = n-1
ans = 0

while left <= right:
    need = d[left]
    left += 1
    
    while need > 0 and left <= right:
        need -= 1
        right -= 1
        ans += 1

print(ans)