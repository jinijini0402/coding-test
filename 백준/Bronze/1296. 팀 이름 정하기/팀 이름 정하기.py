Y=input()
n=int(input())
d=[input() for _ in range(n)]
d.sort()
ans=[]
L,O,V,E=Y.count('L'),Y.count('O'),Y.count('V'),Y.count('E')
for i in d:
    Lt,Ot,Vt,Et=L+i.count('L'),O+i.count('O'),V+i.count('V'),E+i.count('E')
    ans.append(((Lt+Ot)*(Lt+Vt)*(Lt+Et)*(Ot+Vt)*(Ot+Et)*(Vt+Et))%100)
print(d[ans.index(max(ans))])