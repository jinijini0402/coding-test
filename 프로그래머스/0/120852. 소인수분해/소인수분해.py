def solution(n):
    ans=[]
    i=2
    while i*i<=n:
        if n%i==0:
            ans.append(i)
            n//=i
        else:
            i+=1
    if n>1:
        ans.append(n)
    return sorted(set(ans))