def solution(arr1, arr2):
    a=len(arr1)
    for x in range(0,a):
        for y in range(0,len(arr1[x])):
            arr1[x][y]+=arr2[x][y]
    return arr1