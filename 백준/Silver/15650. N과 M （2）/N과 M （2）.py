from itertools import combinations
a,b=map(int,input().split())
for i in combinations(range(1,a+1),b):
    print(' '.join(map(str,i)))