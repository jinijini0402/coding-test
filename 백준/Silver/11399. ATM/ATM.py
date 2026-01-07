n=int(input())
d=list(map(int,input().split()))
d.sort()
ans=0
add=0
for i in d:
    add+=i
    ans+=add
print(ans)