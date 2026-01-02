def solution(array):
    sum=0
    for i in array:
        sum+=str(i).count('7')
    return sum