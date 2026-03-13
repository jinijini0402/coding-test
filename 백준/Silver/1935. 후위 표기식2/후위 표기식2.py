n = int(input())
s = input().rstrip()
num = [int(input()) for _ in range (n)]

q = []
for x in s:
    if x == '*':
        a, b = q.pop(), q.pop()
        q.append(b * a)
    
    elif x == '+':
        a, b = q.pop(), q.pop()
        q.append(b + a)
    
    elif x == '-':
        a, b = q.pop(), q.pop()
        q.append(b - a)
    
    elif x == '/':
        a, b = q.pop(), q.pop()
        q.append(b / a)
    
    else:
        q.append(num[ord(x) - ord('A')])
        
print(f"{q[0]:.2f}")