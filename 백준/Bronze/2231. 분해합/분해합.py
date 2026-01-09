n=int(input())
c=False
for i in range (1,n+1):
    t=i
    add=i
    while t>0:
        add+=t%10
        t=t//10
    if add==n:
        print(i)
        c=True
        break
if not c:
    print(0)