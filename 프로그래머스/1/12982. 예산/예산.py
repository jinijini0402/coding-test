def solution(d, budget):
    d=sorted(d)
    ans=0
    for i in d:
        budget-=i
        if budget<0:
            break
        ans+=1
    return ans