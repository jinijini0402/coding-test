def dfs(numbers,step,total,target):
    if len(numbers)==step:
        if total==target: return 1
        else: return 0
    ret=0
    ret+=dfs(numbers,step+1,total+numbers[step],target)
    ret+=dfs(numbers,step+1,total-numbers[step],target)
    return ret
def solution(numbers, target):
    return dfs(numbers,0,0,target)