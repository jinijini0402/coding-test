from collections import Counter
s=input()
cnt=Counter(s)
odd=[]
for k in sorted(cnt):
    if cnt[k]%2!=0:
        odd.append(k)
if len(odd)>1:
    print("I'm Sorry Hansoo")
else:
    ans=''
    for k in sorted(cnt):
        ans+=k*(cnt[k]//2)
    if len(odd)==0:
        print(ans+ans[::-1])
    else:
        print(ans+odd[0]+ans[::-1])