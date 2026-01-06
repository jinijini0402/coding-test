n,need=map(int,input().split())
d=[int(input()) for _ in range (n)]
d.sort(reverse=True)
ans=0
for i in d:
    if i<=need:
        ans+=need//i
        need=need%i
print(ans)