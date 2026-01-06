n=int(input())
d=[int(input()) for _ in range (n)]
stack=[]
for i in d:
    if i!=0:
        stack.append(i)
    else:
        stack.pop()
print(sum(stack))