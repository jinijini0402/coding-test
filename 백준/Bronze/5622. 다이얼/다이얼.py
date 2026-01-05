s=input()
d={'ABC':3,'DEF':4,'GHI':5,'JKL':6,'MNO':7,'PQRS':8,'TUV':9,'WXYZ':10}
add=0
for word in s:
    for k,v in d.items():
        if word in k:
            add+=v
            break
print(add)