n=int(input())
d=[int(input()) for _ in range (n)]
d.sort()
ans=[]
for i in range(n):
    ans.append(d[i]*(n-i))
print(max(ans))