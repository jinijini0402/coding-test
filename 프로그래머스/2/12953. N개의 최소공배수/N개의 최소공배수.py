import math
def solution(arr):
    res=arr[0]
    for i in arr[1:]:
        res=res*i//math.gcd(res,i)
    return res