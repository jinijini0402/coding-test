def solution(k, tangerine):
    d=[0]*(max(tangerine)+1)
    for i in tangerine:
        d[i]+=1
    d=[x for x in d if x]
    d.sort(reverse=True)
    limit=0
    kind=0
    for i in d:
        limit+=i
        kind+=1
        if limit>=k:
            break
    return kind