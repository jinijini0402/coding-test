s=input()
d=['c=','c-','dz=','d-','lj','nj','s=','z=']
for word in d:
    s=s.replace(word,'*')
print(len(s))