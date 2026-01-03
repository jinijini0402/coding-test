a=int(input())
ans=0
if a<=99: print(a)
else:
    ans=99
    for i in range(100,a+1):
        d=[int(j) for j in str(i)]
        if d[1]-d[0]==d[2]-d[1]:
            ans+=1
    print(ans)