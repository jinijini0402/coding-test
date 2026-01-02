def solution(food):
    d=[i//2 for i in food]
    ans=''
    idx=1
    for i in d[1:]:
        if i!=0:
            ans+=str(idx)*i
        idx+=1
    return ans+'0'+ans[::-1]