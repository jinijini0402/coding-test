s = input()

d = []
cnt = 0

for i in s:
    if i == 'X':
        cnt += 1
    else:
        d.append('AAAA' * (cnt // 4))
        cnt %= 4
        d.append('BB' * (cnt // 2))
        cnt %= 2
        if cnt > 0:
            print(-1)
            break
        d.append('.')
else:
    d.append('AAAA' * (cnt // 4))
    cnt %= 4
    d.append('BB' * (cnt // 2))
    cnt %= 2
    if cnt > 0:
        print(-1)
    else:
        print(''.join(d))