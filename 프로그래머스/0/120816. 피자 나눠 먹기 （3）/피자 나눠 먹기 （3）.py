def solution(slice, n):
    sum=0
    ans=0
    while n>sum:
        sum+=slice
        ans+=1
    return ans