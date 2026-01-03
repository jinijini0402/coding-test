d=[int(input()) for _ in range(9)]
res=sum(d)
t=False
for i in range(8):
    if t: break
    for j in range(i+1,9):
        if (res-d[i]-d[j])==100:
            t=True
            ans=[]
            for k in range(9):
                if k!=i and k!=j:
                    ans.append(d[k])
            ans.sort()
            for x in ans:
                print(x)
        if t: break