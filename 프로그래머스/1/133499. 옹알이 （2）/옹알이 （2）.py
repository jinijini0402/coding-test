def solution(babbling):
    mp={"aya": "0","ye": "1","woo": "2","ma": "3"}
    ans=[1]*len(babbling)
    for i in babbling:
        for k,v in mp.items():
            i=i.replace(k,v)
        if i.isdigit():
            for j in range(0,len(i)):
                if j>=1 and i[j]==i[j-1]:
                    ans.pop()
                    break
        else:
            ans.pop()
    return sum(ans)