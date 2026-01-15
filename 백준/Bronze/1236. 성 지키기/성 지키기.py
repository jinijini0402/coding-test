R,C=map(int,input().split())
d=[input() for _ in range (R)]
Rc=0
Cc=0
for i in d:
    if 'X' not in i:
        Rc+=1
for i in range(C):
    check=False
    for j in range(R):
        if d[j][i]=='X':
            check=True
            break
    if not check:
        Cc+=1
print(max(Rc,Cc))