def solution(n):
    ans=1
    fac=1
    while fac*(ans+1)<=n:
        ans+=1
        fac*=ans
    return ans