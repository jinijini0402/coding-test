import sys
input = sys.stdin.readline
write = sys.stdout.write

n = int(input())
s = set()

for _ in range(n):
    cmd = input().split()
    op = cmd[0]

    if op == 'add':
        s.add(cmd[1])

    elif op == 'remove':
        s.discard(cmd[1])

    elif op == 'check':
        write('1\n' if cmd[1] in s else '0\n')

    elif op == 'toggle':
        x = cmd[1]
        if x in s:
            s.remove(x)
        else:
            s.add(x)

    elif op == 'all':
        s = {'1','2','3','4','5','6','7','8','9','10','11','12','13','14','15','16','17','18','19','20'}

    elif op == 'empty':
        s.clear()
