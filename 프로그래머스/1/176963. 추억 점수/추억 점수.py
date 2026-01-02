def solution(name, yearning, photo):
    d=dict(zip(name,yearning))
    ans=[]
    for i in photo:
        total=0
        for person in i:
            total+=d.get(person,0)
        ans.append(total)
    return ans