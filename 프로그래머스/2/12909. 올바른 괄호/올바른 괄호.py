def solution(s):
    if s[0]==")" or s[-1]=="(" or len(s)%2!=0:
        return False
    d=[]
    for i in s:
        if i=="(":
            d.append(1)
        else:
            if not d:
                return False
            d.pop()
    return len(d)==0