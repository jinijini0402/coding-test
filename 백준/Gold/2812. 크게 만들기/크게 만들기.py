a,b=map(int,input().split())
s=input().strip()
stack=[]
for i in s:
    while b>0 and stack and stack[-1]<i:
        stack.pop()
        b-=1
    stack.append(i)
if b>0:
    stack=stack[:-b]
print(''.join(stack))