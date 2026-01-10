n=int(input())
d=[list(map(int,input().split())) for _ in range (n)]
ans=[]
for i in d: #i[0]세로,i[1]가로,i[2]순서
    Y=i[2]%i[0]
    X=(i[2]+i[0]-1)//i[0]
    if Y==0:
        Y=i[0]
    ans.append(str(Y)+str(X).zfill(2))
for i in ans:
    print(i)