n=int(input())
for _ in range(n):
    a,idx=map(int, input().split())
    d=list(map(int,input().split()))
    d1=[]
    for i in range(a):
        d1.append([d[i],i])
    cnt=0
    while True:
        cur=d1.pop(0)
        if d1 and cur[0]<max(x[0] for x in d1):
            d1.append(cur)
        else:
            cnt+=1
            if cur[1]==idx:
                print(cnt)
                break