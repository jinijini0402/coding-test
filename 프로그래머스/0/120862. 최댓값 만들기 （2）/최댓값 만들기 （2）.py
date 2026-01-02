def solution(numbers):
    numbers.sort()
    if numbers[len(numbers)-1] * numbers[len(numbers)-2]>=numbers[0]*numbers[1]:
        return numbers[len(numbers)-1] * numbers[len(numbers)-2]
    else:
        return numbers[0]*numbers[1]