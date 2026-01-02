def solution(phone_book):
    s=set(phone_book)
    for num in phone_book:
        prefix=""
        for ch in num:
            prefix+=ch
            if prefix!=num and prefix in s:
                return False
    return True