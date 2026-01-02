def solution(s):
    count1=0
    count2=0
    ans=0
    cur=''
    for i in s:
        if cur=='':
            cur=i
            count1+=1
        elif cur==i:
            count1+=1
        else:
            count2+=1
        if count1==count2:
            ans+=1
            cur=''
            count1=0
            count2=0
    if cur:
        ans+=1
    return ans