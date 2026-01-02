def solution(numbers, k):
    i=(k-1)*2+1
    i%=len(numbers)
    return numbers[i-1]