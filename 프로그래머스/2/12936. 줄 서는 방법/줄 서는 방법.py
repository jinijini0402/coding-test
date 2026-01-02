from math import factorial
def solution(n, k):
    ans=[]
    d=[i for i in range(1,n+1)]
    k-=1
    while d:
        fac=factorial(len(d)-1)
        idx=k//fac
        k=k%fac
        ans.append(d.pop(idx))
    return ans