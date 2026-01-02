def solution(num, k):
    a=str(num)
    if str(k) in a:
        return a.index(str(k))+1
    return -1