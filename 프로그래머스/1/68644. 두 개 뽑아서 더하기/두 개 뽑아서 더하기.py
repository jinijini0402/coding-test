from itertools import combinations
def solution(numbers):
    ans=[]
    d=combinations(numbers,2)
    for i in d:
        ans.append(sum(i))
    return sorted(set(ans))