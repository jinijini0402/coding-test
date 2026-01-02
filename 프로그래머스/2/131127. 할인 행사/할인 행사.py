def solution(want, number, discount):
    ans=0
    for i in range(len(discount)-9):
        d=discount[i:i+10]
        ok=True
        for ind,name in enumerate(want):
            if d.count(name)!=number[ind]:
                ok=False
                break
        if ok:
            ans+=1
    return ans