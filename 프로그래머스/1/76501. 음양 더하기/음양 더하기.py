def solution(absolutes, signs):
    ans=0
    for i in range(0,len(signs)):
        if signs[i]==True:
            ans+=absolutes[i]
        else:
            ans-=absolutes[i]
    return ans