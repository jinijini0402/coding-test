a=int(input())
res=(a//10+a%10)%10+(a%10)*10
ans=1
while a!=res:
    add=res//10+res%10
    res=(res%10)*10+add%10
    ans+=1
print(ans)