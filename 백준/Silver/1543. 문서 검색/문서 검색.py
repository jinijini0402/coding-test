ful=input()
fin=input()
l=len(fin)
ans=0
while ful:
    idx=ful.find(fin)
    if idx==-1: break
    else:
        ans+=1
        ful=ful[idx+l:]
print(ans)