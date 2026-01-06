n=int(input())
d=list(map(int,input().split()))
m=max(d)
for i in range (n):
    d[i]=(d[i]/m)*100
print(sum(d)/n)