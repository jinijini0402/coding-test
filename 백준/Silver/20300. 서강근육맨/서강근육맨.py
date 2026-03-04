n = int(input())
d = list(map(int, input().split()))

d.sort()
l = len(d)
ans = []

s = 0
if l % 2 == 0:
    e = l - 1
else:
    e = l - 2
while s < e:
    ans.append(d[s] + d[e])
    s += 1
    e -= 1

if l % 2 != 0:
    ans.append(d[l - 1])
    
print(max(ans))