M,N=map(int,input().split())
check=[True]*(N+1)
check[0]=check[1]=False
for i in range (2,int(N**0.5)+1):
    if check[i]:
        for j in range (i*i,N+1,i):
            check[j]=False
for i in range (M,N+1):
    if check[i]:
        print(i)