d=[input() for _ in range (3)]
ans=0
for i in range(3):
    if d[i].isdigit():
        ans=int(d[i])+3-i
        break
if ans%15==0:
    print("FizzBuzz")
elif ans%3==0 and ans%5!=0:
    print("Fizz")
elif ans%5==0 and ans%3!=0:
    print("Buzz")
else:
    print(ans)