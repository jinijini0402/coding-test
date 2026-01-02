def solution(s):
    d=s.split()
    d=[int(i) for i in d]
    return str(min(d))+' '+str(max(d))