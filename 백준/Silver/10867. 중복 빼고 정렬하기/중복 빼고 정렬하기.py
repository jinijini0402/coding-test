n=int(input())
d=set(map(int,input().split()))
ans=[]
for i in d:
    ans.append(int(i))
ans.sort()
print(' '.join(map(str,ans)))