n=int(input())
d=[input() for _ in range (n)]
d=list(set(d))
d.sort(key=lambda x: (len(x),x))
for i in d:
    print(i)