n=int(input())
d=[input() for _ in range (n)]
ans=0
for i in d:
    l=0
    r=len(i)-1
    check=0
    while l<r:
        if i[l]==i[r]:
            l+=1
            r-=1
        else:
            def pal(l,r):
                while l<r:
                    if i[l]!=i[r]:
                        return False
                    l+=1
                    r-=1
                return True
            if pal(l+1,r) or pal(l,r-1):
                check=1
            else:
                check=2
            break
    print(check)
            