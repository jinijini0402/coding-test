a=[int(input()) for _ in range(28)]
ans=[i for i in range(1,31)]
for i in a:
    ans.remove(i)
for i in ans:
    print(i)