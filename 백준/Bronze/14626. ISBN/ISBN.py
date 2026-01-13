s=input()
ans=0
idx=-1
for i in range (13):
    if s[i]=='*':
        idx=i
        continue
    else:
        if i%2==0:
            ans+=int(s[i])*1
        else:
            ans+=int(s[i])*3
ans%=10
for i in range(10):
    if idx%2==0:
        t=(ans+i)%10
    else:
        t=(ans+i*3)%10
    if t==0:
        print(i)
        break