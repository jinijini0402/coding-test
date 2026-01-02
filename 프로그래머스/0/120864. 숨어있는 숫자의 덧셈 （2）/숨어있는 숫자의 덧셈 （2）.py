import re
def solution(my_string):
    res = list(map(int,re.findall(r'\d+', my_string)))
    num = sum(res)
    return num