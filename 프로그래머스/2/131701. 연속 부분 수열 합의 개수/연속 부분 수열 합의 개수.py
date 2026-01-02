def solution(elements):
    l=len(elements)
    elements=elements+elements
    ans=set()
    for i in range(0,l):
        for j in range(0,l):
            ans.add(sum(elements[j:j+i]))
    return len(ans)