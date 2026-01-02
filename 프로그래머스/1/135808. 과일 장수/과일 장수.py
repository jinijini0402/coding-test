def solution(k, m, score):
    score.sort(reverse=True)
    a=0
    for i in range(m-1,len(score),m):
        a+=score[i]
    a*=m
    return a