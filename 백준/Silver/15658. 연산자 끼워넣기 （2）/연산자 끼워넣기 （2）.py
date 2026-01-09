import sys
input=sys.stdin.readline
n=int(input())
d=list(map(int,input().split()))
op=list(map(int,input().split())) #+,-,*,//
mx=-10**18
mn=10**18
def dfs(idx,cur):
    global mx,mn
    if idx==n:
        mx=max(cur,mx)
        mn=min(cur,mn)
        return
    nxt=d[idx]
    for i in range(4):
        if op[i]==0:
            continue
        op[i]-=1
        if i==0: dfs(idx+1,cur+nxt)
        elif i==1: dfs(idx+1,cur-nxt)
        elif i==2: dfs(idx+1,cur*nxt)
        else:
            if cur<0:
                div=-(abs(cur)//nxt)
            else:
                div=cur//nxt
            dfs(idx+1,div)
        op[i]+=1
dfs(1,d[0])
print(mx)
print(mn)