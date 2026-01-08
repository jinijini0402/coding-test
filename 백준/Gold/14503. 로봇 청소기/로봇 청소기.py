n,m=map(int,input().split())
r,c,d=map(int,input().split())
room=[list(map(int,input().split())) for _ in range (n)]
ans=0
# 북, 동, 남, 서
dr=[-1,0,1,0]
dc=[0,1,0,-1]
while True:
    if room[r][c]==0:
        room[r][c]=2
        ans+=1
    found=False
    for _ in range(4):
        d=(d+3)%4
        nr=r+dr[d]
        nc=c+dc[d]
        if room[nr][nc]==0:
            r,c=nr,nc
            found=True
            break
    if found:
        continue
    back=(d+2)%4
    br=r+dr[back]
    bc=c+dc[back]
    if room[br][bc]==1:
        break
    r,c=br,bc
print(ans)         