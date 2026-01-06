n=int(input())
d=list(map(int,input().split()))
find=int(input())
ans=0
for i in d:
    if i==find:
        ans+=1
print(ans)