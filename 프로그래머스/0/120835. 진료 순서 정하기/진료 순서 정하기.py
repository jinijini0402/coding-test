def solution(emergency):
    ans=[]
    sor=sorted(emergency, reverse=True)
    for i in emergency:
        ans.append(sor.index(i)+1)
    return ans