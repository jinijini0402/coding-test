s, e = map(int, input().split())

ans = 0
while e > s:
    if e % 10 == 1:
        e //= 10
    elif e % 2 == 0:
        e //= 2
    else:
        break
    ans += 1
        
if e != s:
    print(-1)
else:
    print(ans + 1)