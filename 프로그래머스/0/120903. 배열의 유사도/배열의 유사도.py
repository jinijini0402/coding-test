def solution(s1, s2):
    ans=list(set(s1) & set(s2))
    return len(ans)