s=input()
ans=0
minus=0
digit=''
check=False
for i in s:
    if i!='-' and i!='+':
        digit+=i
    elif not check:
        ans+=int(digit)
        digit=''
        if i=='-':
            check=True
    elif check:
        minus+=int(digit)
        digit=''
if check:
    minus+=int(digit)
else:
    ans+=int(digit)
print(ans-minus)