def solution(n):
    if n<2:
        return 0
    prime=[True]*(n+1)
    prime[0]=prime[1]=0
    i=2
    while i*i<=n:
        if prime[i]:
            start=i*i
            step=i
            for j in range(start,n+1,step):
                prime[j]=False
        i+=1
    return sum(prime)