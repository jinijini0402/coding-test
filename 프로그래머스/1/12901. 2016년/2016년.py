def solution(a, b):
    d=['FRI','SAT','SUN','MON','TUE','WED','THU']
    cnt=0
    if a!=1:
        for i in range (1,a):
            if i==2:
                cnt+=29
            elif i in [1, 3, 5, 7, 8, 10, 12]:
                cnt+=31
            else:
                cnt+=30
    return d[(cnt+b-1)%7]