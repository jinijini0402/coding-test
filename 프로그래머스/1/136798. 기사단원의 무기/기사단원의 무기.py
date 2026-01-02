def solution(number, limit, power):
    ans=0
    for x in range(1,number+1):
        cnt=0
        i=1
        while i*i<=x:
            if x%i==0:
                cnt+=1 if i*i==x else 2
                if cnt>limit:
                    cnt=power
                    break
            i+=1
        ans+=cnt
    return ans