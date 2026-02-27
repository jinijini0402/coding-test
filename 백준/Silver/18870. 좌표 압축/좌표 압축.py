n = int(input())
d = list(map(int, input().split()))

t = sorted(set(d))
rank = {}

for i in range (len(t)):
    rank[t[i]] = i

for i in d:
    print(rank[i], end = ' ')