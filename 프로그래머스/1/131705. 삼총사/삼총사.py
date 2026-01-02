from itertools import combinations
def solution(number):
    ans=0
    for i in combinations(number,3):
        if sum(i)==0:
            ans+=1
    return ans