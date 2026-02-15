n=int(input())
d=[0]+[int(input()) for _ in range (n)]

dp=[0]*(n+1)

if n>=1:
    dp[1]=d[1]
if n>=2:
    dp[2]=d[1]+d[2]

for i in range (3,n+1):
    dp[i]=max(
        dp[i-1],
        dp[i-2]+d[i],
        dp[i-3]+d[i-1]+d[i])

print(dp[n])