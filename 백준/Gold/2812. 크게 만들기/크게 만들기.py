a,b=map(int,input().split())
s=input().strip()
stack=[]
k=b
for ch in s:
    while stack and stack[-1]<ch and k>0:
        stack.pop()
        k-=1
    stack.append(ch)
if k>0:
    stack=stack[:-k]
print(''.join(stack))