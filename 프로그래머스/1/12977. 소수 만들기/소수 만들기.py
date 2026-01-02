from itertools import combinations
def solution(nums):
    ans=0
    a=len(nums)
    for i in combinations(nums,3):
        s=sum(i)
        for x in range(2,s):
            if s%x==0:
                ans+=1
                break
    return a*(a-1)*(a-2)//6-ans