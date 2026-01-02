def solution(s):
    ans=[]
    idx=0
    for i in s:
        if i==' ':
            ans.append(' ')
            idx=0
        else:
            if idx%2==0:
                ans.append(i.upper())
            else:
                ans.append(i.lower())
            idx+=1
    return ''.join(ans)