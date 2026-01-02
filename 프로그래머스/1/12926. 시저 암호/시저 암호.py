def solution(s, n):
    ans=[]
    for i in s:
        if i.isupper():
            ans.append(chr((ord(i)-ord('A')+n)%26+ord('A')))
        if i.islower():
            ans.append(chr((ord(i)-ord('a')+n)%26+ord('a')))
        if i==' ':
            ans.append(' ')
    return ''.join(ans)