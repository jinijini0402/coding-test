def solution(n, arr1, arr2):
    ans=[]
    for i in range(0,n):
        a=arr1[i]|arr2[i]
        a=format(a,'b').zfill(n)
        ans.append(a.replace('1','#').replace('0',' '))
    return ans