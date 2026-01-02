def solution(n):
    ans=''
    while n>0:
        ans=str(n%3)+ans
        n//=3
    return int(str(ans)[::-1],3)