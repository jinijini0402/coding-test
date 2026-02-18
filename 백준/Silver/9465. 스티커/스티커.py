import sys
input = sys.stdin.readline

t = int(input())

for _ in range(t):
    C = int(input())
    d0 = [0] + list(map(int, input().split()))
    d1 = [0] + list(map(int, input().split()))

    dp0 = [0] * (C + 1)
    dp1 = [0] * (C + 1)   # 여기!

    dp0[1] = d0[1]
    dp1[1] = d1[1]

    for i in range(2, C + 1):
        dp0[i] = max(dp1[i - 1], dp1[i - 2]) + d0[i]
        dp1[i] = max(dp0[i - 1], dp0[i - 2]) + d1[i]

    print(max(dp0[C], dp1[C]))
