def solution(i, j, k):
    ans=0
    for x in range (i,j+1):
        ans+=str(x).count(str(k))
    return ans