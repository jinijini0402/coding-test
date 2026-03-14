s = input().rstrip()

d = []
ans = 0
t = 1

for i in range(len(s)):
    
    if s[i] == '(':
        d.append('(')
        t *= 2
        
    elif s[i] == '[':
        d.append('[')
        t *= 3
        
    elif s[i] == ')':
        if not d or d[-1] != '(':
            ans = 0
            break
            
        if s[i-1] == '(':
            ans += t
        d.pop()
        t //= 2
        
    elif s[i] == ']':
        if not d or d[-1] != '[':
            ans = 0
            break
            
        if s[i-1] == '[':
            ans += t
        d.pop()
        t //= 3
        
if d:
    print(0)
else:
    print(ans)