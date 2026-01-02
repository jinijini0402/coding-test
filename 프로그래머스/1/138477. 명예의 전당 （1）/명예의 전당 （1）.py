def solution(k, score):
    d,ans=[],[]
    for i in score:
        d.append(i)
        d.sort(reverse=True)
        if len(d)>k:
            d.pop()
        ans.append(d[-1])
    return ans