def solution(n, words):
    d=[words[0]]
    check=words[0][-1]
    for i in words[1:]:
        if i not in d and check==i[0]:
            d.append(i)
            check=i[-1]
        else:
            break
    if d==words:
        return [0,0]
    return [len(d)%n+1,len(d)//n+1]