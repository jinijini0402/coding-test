def solution(numbers):
    mp={"zero":'0', "one":'1', "two":'2', "three":'3', "four":'4', "five":'5', "six":'6', "seven":'7', "eight":'8', "nine":'9'}
    for b,a in mp.items():
        numbers=numbers.replace(b,a)
    return int(numbers)