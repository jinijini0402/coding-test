def solution(answers):
    a=[1,2,3,4,5]
    b=[2,1,2,3,2,4,2,5]
    c=[3,3,1,1,2,2,4,4,5,5]
    ac,bc,cc=0,0,0
    ans=[]
    for i in range (0,len(answers)):
        if answers[i]==a[i%5]:
            ac+=1
        if answers[i]==b[i%8]:
            bc+=1
        if answers[i]==c[i%10]:
            cc+=1
    biggest=max(ac,bc,cc)
    if biggest==ac:
        ans.append(1)
    if biggest==bc:
        ans.append(2)
    if biggest==cc:
        ans.append(3)
    return ans