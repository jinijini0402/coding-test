def solution(my_string):
    d=my_string.split()
    ans=int(d[0])
    for i in range (1,len(d),2):
        if d[i]=='+':
            ans+=int(d[i+1])
        else:
            ans-=int(d[i+1])
    return ans