s=input().strip()
n=int(input())
d=[input().strip() for _ in range (n)]
d.sort()
ans=[]
for i in d:
    L=s.count('L')+i.count('L')
    O=s.count('O')+i.count('O')
    V=s.count('V')+i.count('V')
    E=s.count('E')+i.count('E')
    ans.append(((L+O)*(L+V)*(L+E)*(O+V)*(O+E)*(V+E))%100)
print(d[ans.index(max(ans))])