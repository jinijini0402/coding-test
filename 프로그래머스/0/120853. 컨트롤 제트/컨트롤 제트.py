def solution(s):
    d=s.split()
    stack=[]
    for i in d:
        if i=='Z':
            stack.pop()
        else:
            stack.append(int(i))
    return sum(stack)