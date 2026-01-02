def solution(t, p):
    a=len(p)
    b=len(t)
    ans=0
    for i in range (0,b-a+1):
        if int(t[i:i+a])<=int(p):
            ans+=1
    return ans