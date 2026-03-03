s = list(input().rstrip())

mx = []
m = 0
for ch in s:
    if ch == 'M':
        m += 1
    else:
        mx.append('5' + '0' * m)
        m = 0
if m != 0:
    mx.append('1' * m)

print(''.join(mx))

mn = []
m = 0
for ch in s:
    if ch == 'M':
        m += 1
    else:
        if m:
            mn.append('1' + '0' * (m - 1))
            m = 0
        mn.append('5')
if m:
    mn.append('1' + '0' * (m - 1))
    
print(''.join(mn))