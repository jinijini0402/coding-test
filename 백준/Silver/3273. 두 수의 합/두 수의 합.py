n=int(input())
d=list(map(int, input().split()))
find=int(input())
seen=set()
ans=0
for i in d:
    if find-i in seen:
        ans+=1
    seen.add(i)
print(ans)