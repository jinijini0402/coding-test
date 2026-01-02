def solution(sides):
    ans=0
    for i in range (1,max(sides)+1):
        if i+min(sides)>max(sides):
            ans+=1
    ans+=min(sides)-1
    return ans