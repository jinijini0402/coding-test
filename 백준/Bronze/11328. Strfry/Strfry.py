n=int(input())
d=[list(input().split()) for _ in range(n)]
for a,b in d:
    if sorted(a)==sorted(b):
        print("Possible")
    else:
        print("Impossible")