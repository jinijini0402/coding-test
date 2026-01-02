def solution(s):
    ans=0
    n=len(s)
    if len(s)%2!=0:
        return 0
    for i in range(n):
        stack=[]
        ok=True
        if s[0] in ')]}' or s[-1] in '([{':
                ok=False
        else:
            for j in s:
                if j in '([{':
                    stack.append(j)
                else:
                    if not stack:
                        ok=False
                        break
                    top=stack[-1]
                    if (top=='(' and j==')') or (top=='[' and j==']') or (top=='{' and j=='}'):
                        stack.pop()
                    else:
                        ok=False
                        break
        if stack:
            ok=False
        s=s[1:]+s[:1]
        ans+=ok
    return ans