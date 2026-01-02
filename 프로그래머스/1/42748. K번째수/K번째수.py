def solution(array, commands):
    d=[]
    for i,j,k in commands:
        d.append(sorted(array[i-1:j])[k-1])
    return d