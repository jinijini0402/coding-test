n = int(input())
s = input().rstrip()

cnt = 1
prv = s[0]
for ch in s:
    if ch != prv:
        cnt += 1
    prv = ch

cnt //= 2
print(cnt + 1)