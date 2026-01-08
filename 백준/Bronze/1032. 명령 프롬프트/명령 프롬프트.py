n=int(input())
d=[input() for _ in range (n)]
ans=[]
for i in range (len(d[0])):
    check=True
    cur=''
    for j in range (n):
        if j==0:
            cur=d[j][i]
        if cur!=d[j][i]:
            check=False
            break
    if not check:
        ans.append('?')
    else:
        ans.append(cur)
print(''.join(ans))