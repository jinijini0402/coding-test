def solution(n):
    f=[1,2]
    if n<=2:
        return f[n-1]
    for i in range(2,n):
        f.append(f[i-1]+f[i-2])
    return f[n-1]%1234567