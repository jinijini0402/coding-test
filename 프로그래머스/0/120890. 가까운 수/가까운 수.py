def solution(array, n):
    ans = min(array, key= lambda x: (abs(x-n),x))
    return ans