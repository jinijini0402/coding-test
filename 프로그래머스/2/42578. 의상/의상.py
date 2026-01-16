def solution(clothes):
    d=dict()
    for a,b in clothes:
        if b not in d:
            d[b]=1
        else:
            d[b]+=1
    ans=1
    for i in d.values():
        ans*=i+1
    return ans-1