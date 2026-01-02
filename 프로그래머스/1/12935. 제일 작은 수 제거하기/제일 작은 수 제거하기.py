def solution(arr):
    ans=[]
    a=min(arr)
    for i in arr:
        if i!=a:
            ans.append(i)
    return ans if ans else [-1]