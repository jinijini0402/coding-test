def solution(n):
    ans=0
    for i in range(1,n+1):
        add=0
        temp=i
        while add<n:
            add+=temp
            temp+=1
        if add==n:
            ans+=1
    return ans