def solution(age):
    a="abcdefghij"
    return ''.join(a[int(i)] for i in str(age))