def solution(order):
    s=str(order)
    ans=0
    for i in s:
        if int(i)%3==0 and int(i)!=0:
            ans+=1
    return ans