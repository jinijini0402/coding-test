n=int(input())
s=input()
r=31
M=1234567891
ans=0
power=1
for i in s:
    val=ord(i)-ord('a')+1
    ans=(ans+val*power)%M
    power=(power*r)%M
print(ans)