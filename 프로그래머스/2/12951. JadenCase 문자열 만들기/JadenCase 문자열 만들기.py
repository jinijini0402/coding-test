def solution(s):
    ans=[]
    a=True
    for i in s:
        if i==' ':
            ans.append(' ')
            a=True
        else:
            if a:
                ans.append(i.upper())
                a=False
            else:
                ans.append(i.lower())
    return ''.join(ans)