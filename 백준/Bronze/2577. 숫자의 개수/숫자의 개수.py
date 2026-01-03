a=[int(input()) for _ in range(3)]
mul=str(a[0]*a[1]*a[2])
ans=[0]*10
for i in mul:
    i=int(i)
    ans[i]+=1
for i in ans:
    print(i)