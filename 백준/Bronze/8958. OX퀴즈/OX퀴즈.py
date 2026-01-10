n=int(input())
d=[input() for _ in range (n)]
for i in d:
    cnt=0
    add=0
    for j in i:
        if j=='O':
            cnt+=1
            add+=cnt
        else:
            cnt=0
    print(add)