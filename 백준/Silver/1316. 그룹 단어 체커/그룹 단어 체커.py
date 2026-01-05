n=int(input())
d=[input() for _ in range(n)]
ans=0
for word in d:
    check=[]
    for i in word:
        if i not in check:
            check.append(i)
        elif i in check and check[-1]!=i:
            ans-=1
            break
print(n+ans)