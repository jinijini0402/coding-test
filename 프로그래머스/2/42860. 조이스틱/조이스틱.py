def solution(name):
    ans=0
    for i in name:
        n=ord(i)-ord('A')
        if n<=13:
            ans+=n
        else:
            ans+=26-n
    n=len(name)
    move=n-1
    for i in range(n):
        next_i=i+1
        while next_i<n and name[next_i]=='A':
            next_i+=1
        move=min(
            move,
            i*2+(n-next_i),
            (n-next_i)*2+i
        )
    ans+=move
    return ans