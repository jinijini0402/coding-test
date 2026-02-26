N, r, c = map(int, input().split())
N = 2 ** N
ans = 0

while N > 1:
    N //= 2

    if r < N and c < N:
        ans += 0
    elif r < N and c >= N:
        ans += N * N
        c -= N
    elif r >= N and c < N:
        ans += N * N * 2
        r -= N
    else:
        ans += N * N * 3
        r -= N
        c -= N

print(ans)