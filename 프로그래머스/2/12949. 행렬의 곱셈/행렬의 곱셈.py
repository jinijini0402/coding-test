def solution(arr1, arr2):
    n=len(arr1)
    m=len(arr1[0])
    k=len(arr2[0])
    d=[[0]*k for _ in range(n)]
    for i in range(n):
        for j in range(k):
            for x in range(m):
                d[i][j]+=arr1[i][x]*arr2[x][j]
    return d