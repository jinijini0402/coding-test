a,b=map(int,input().split())
d=list(map(int,input().split()))
total=0
for i in range(0,a-2):
    for j in range(i+1,a-1):
        for k in range(j+1,a):
            n=d[i]+d[j]+d[k]
            if n<=b and n>total:
                total=n
print(total)