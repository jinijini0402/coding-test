def solution(clothes):
    kind=[]
    count=[]
    for i in clothes:
        if i[1] not in kind:
            kind.append(i[1])
            count.append(1)
        else:
            count[kind.index(i[1])]+=1
    res=1
    for i in count:
        res*=(i+1)
    return res-1