from itertools import permutations
end,n=map(int,input().split())
d=[i for i in range (1,end+1)]
com=list(permutations(d,n))
for i in com:
    print(' '.join(map(str,i)))