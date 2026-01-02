def solution(brown, yellow):
    a=(brown-4)//2
    ans=[]
    for i in range (1,a+1):
        if i*(a-i)==yellow:
            ans.append(a-i+2)
            ans.append(i+2)
            break
    return ans