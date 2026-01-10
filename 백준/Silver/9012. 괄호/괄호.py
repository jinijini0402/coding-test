n = int(input())
for _ in range(n):
    s = input().strip()
    stack = []
    check = True

    if s[0] == ')' or s[-1] == '(' or len(s) % 2 != 0:
        print("NO")
        continue

    for ch in s:
        if ch == '(':
            stack.append('(')
        else:
            if not stack:
                check = False
                break
            stack.pop()

    print("YES" if check and not stack else "NO")