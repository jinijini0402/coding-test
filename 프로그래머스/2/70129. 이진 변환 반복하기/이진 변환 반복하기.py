def solution(s):
    count=0
    zero=0
    while s!="1":
        zero+=s.count("0")
        count+=1
        s=bin(s.count("1"))[2:]
    return [count,zero]