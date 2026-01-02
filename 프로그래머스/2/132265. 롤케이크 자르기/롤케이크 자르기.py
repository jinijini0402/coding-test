from collections import Counter
def solution(topping):
    ans=0
    right=Counter(topping)
    left=set()
    for i in topping[:-1]:
        left.add(i)
        right[i]-=1
        if right[i]==0:
            del right [i]
        if len(left)==len(right):
            ans+=1
    return ans