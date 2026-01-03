n=int(input())
d=[list(map(int,input().split())) for _ in range (n)]
ans=[]
count=0
for h,w in d:
    for h1,w1 in d:
        if (h<h1 and w<w1):
            count+=1
    ans.append(count+1)
    count=0
for i in ans:
    print(i)