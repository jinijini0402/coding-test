n=int(input())
d=[list(input().split()) for _ in range(n)]
for x,y in d:
    for word in y:
        print(word*int(x),end='')
    print()