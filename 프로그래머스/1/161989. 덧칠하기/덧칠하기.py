def solution(n, m, section):
    ans=0
    p=0
    for i in section:
        if i>p:
            p=i+m-1
            ans+=1
    return ans