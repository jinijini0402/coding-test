from itertools import combinations
while True:
    i=input().strip()
    if i=='0':
        break
    d=list(map(int,i.split()))
    d=d[1:]
    d.sort()
    for some in combinations(d,6):
        print(' '.join(map(str,some)))
    print()