def solution(my_string):
    d=[]
    for i in my_string:
        if i.isdigit():
            d.append(int(i))
    d.sort()
    return d