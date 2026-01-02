def solution(a, b):
    ans=0
    for i in range (0,len(a)):
        ans+=a[i]*b[i]
    return ans