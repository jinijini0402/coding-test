while True:
    a,b,c=map(int,input().split())
    if a==0:
        break
    mx=max(a,b,c)
    if (mx==a and a>=b+c) or (mx==b and b>=a+c) or (mx==c and c>=a+b):
        print('Invalid')
    elif a==b and b==c:
        print('Equilateral')
    elif a!=b and a!=c and b!=c:
        print('Scalene')
    else:
        print('Isosceles')