find_num=int(input())
find=set(map(int,input().split()))
hold_num=int(input())
hold=list(map(int,input().split()))
ans=[]
for i in hold:
    if i in find:
        ans.append('1')
    else:
        ans.append('0')
print(' '.join(ans))