def solution(num):
    ans=0
    while ans<500 and num!=1:
        ans+=1
        num=num//2 if num%2==0 else num*3+1
    return ans if num==1 else -1