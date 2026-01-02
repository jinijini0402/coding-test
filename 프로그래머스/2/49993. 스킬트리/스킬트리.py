from collections import deque
def solution(skill, skill_trees):
    ans=0
    for i in skill_trees:
        d=deque(skill)
        for j in i:
            if j in d:
                a=d.popleft()
                if a!=j:
                    ans+=1
                    break
    return len(skill_trees)-ans