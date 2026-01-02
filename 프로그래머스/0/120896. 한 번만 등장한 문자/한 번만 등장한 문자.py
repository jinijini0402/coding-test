def solution(s):
    ans=[]
    for i in set(s):
        if s.count(i)==1:
            ans.append(i)
    ans.sort()
    return ''.join(ans)