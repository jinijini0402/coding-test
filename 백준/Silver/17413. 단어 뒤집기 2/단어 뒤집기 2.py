s=input()
tag=False
d=[]
buf=[]
for i in s:
    if i=='<':
        if buf:
            d+=buf[::-1]
            buf=[]
        tag=True
        d.append(i)
    elif i=='>':
        tag=False
        d.append(i)
    elif tag:
        d.append(i)
    else:
        if i==' ':
            if buf:
                d+=buf[::-1]
                buf=[]
            d.append(' ')
        else:
            buf.append(i)
if buf:
    d+=buf[::-1]
print(''.join(d))