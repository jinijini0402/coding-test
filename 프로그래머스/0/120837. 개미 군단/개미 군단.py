def solution(hp):
    sum=hp//5
    hp%=5
    sum+=hp//3
    hp%=3
    sum+=hp
    return sum