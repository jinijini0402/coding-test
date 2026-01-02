def solution(s):
    d={}
    ans=[]
    idx=0
    for i in s:
        if i not in d:
            ans.append(-1)
        else:
            ans.append(idx-d[i]+1)
        idx+=1
        d[i]=idx
    return ans