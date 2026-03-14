s = input().rstrip()

q = []
ans = 0

for i in range(len(s)):
    if s[i] == '(':
        q.append('(')
        
    else:
        q.pop()
        
        if s[i-1] == '(':
            ans += len(q)
        else:
            ans += 1
            
print(ans)