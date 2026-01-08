s,e=map(int,input().split())
r=[]
i=0
while len(r)<=e:
    i+=1
    for n in range(i):
        r.append(i)
print(sum(r[s-1:e]))