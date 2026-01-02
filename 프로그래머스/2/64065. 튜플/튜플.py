from collections import Counter
def solution(s):
    d=s[2:-2].split("},{")
    ans=[]
    for i in d:
        num=list(map(int,i.split(",")))
        for i in num:
            ans.append(i)
    c=Counter(ans)
    sorted_item=sorted(c.items(),key=lambda x:x[1], reverse=True)
    return [i for i,_ in sorted_item]