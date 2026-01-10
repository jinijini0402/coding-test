n=int(input())
d=[list(input().split())+[i] for i in range(n)]
d.sort(key=lambda x:(int(x[0]),x[2]))
for a,b,c in d:
    print(a+' '+b)