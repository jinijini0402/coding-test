def solution(balls, share):
    a=1 
    for i in range (balls,share,-1):
        a*=i
    b=1
    for i in range (balls-share,0,-1):
        b*=i
    return a//b