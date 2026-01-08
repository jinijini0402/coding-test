r,c=map(int,input().split())
d=[input() for _ in range (r)]
rn=0
cn=0
for i in d:
    if i.count('X')==0:
        rn+=1
for i in range(c):
    check=False
    for j in range(r):
        if d[j][i]=='X':
            check=True
            break
    if not check:
        cn+=1
print(max(rn,cn))    