def solution(N, stages):
    cnt=[0]*(N+2)
    for s in stages:
        cnt[s]+=1
    remain=len(stages)
    rate=[]
    for stage in range(1,N+1):
        if remain==0:
            fail=0
        else:
            fail=cnt[stage]/remain
        rate.append((fail,stage))
        remain-=cnt[stage]
    rate.sort(key=lambda x: (-x[0], x[1]))
    return [i for _,i in rate]