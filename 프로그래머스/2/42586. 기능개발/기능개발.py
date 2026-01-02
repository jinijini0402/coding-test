def solution(progresses, speeds):
    l=len(progresses)
    d=[(100-progresses[i]+speeds[i]-1)//speeds[i] for i in range(l)]
    ans=[]
    count=1
    cur=d[0]
    for i in range(1,l):
        if d[i]>cur:
            ans.append(count)
            cur=d[i]
            count=1
        else:
            count+=1
    ans.append(count)
    return ans