from collections import Counter
n=int(input())
d=[list(input().split('.')) for _ in range (n)]
col=[]
for a,b in d:
    col.append(b)
cnt=Counter(col)
for k in sorted(cnt):
    print(k,cnt[k])