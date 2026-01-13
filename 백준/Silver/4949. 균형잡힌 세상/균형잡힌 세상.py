while True:
    s=input()
    if s=='.':
        break
    stack=[]
    ans="yes"
    for i in s:
        if i=='(' or i=='[':
            stack.append(i)
        elif i==')':
            if not stack or stack.pop()!='(':
                ans="no"
                break
        elif i==']':
            if not stack or stack.pop()!='[':
                ans="no"
                break
    if stack:
        ans="no"
    print(ans)