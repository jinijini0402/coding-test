n1=int(input())
d1=set((map(int,input().split())))
n2=int(input())
d2=list(map(int,input().split()))
for i in d2:
    if i in d1:
        print(1)
    else:
        print(0)