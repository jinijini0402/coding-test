def solution(array, height):
    array.sort()
    ans=0
    for i in array:
        if height<i:
            ans+=1
    return ans