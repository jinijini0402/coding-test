n=int(input())
sp=n-1
st=1
for i in range (n):
    print(' '*sp+'*'*st)
    sp-=1
    st+=2
sp+=1
st-=2
for i in range (n-1):
    sp+=1
    st-=2
    print(' '*sp+'*'*st)