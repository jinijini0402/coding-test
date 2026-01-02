def solution(a, b, n):
    ans,r,p=0,0,0
    while n>=a:
        r=n%a
        p=n//a
        ans+=p*b
        n=r+p*b
    return ans