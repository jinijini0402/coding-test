n=int(input())
d=[list(map(int,input().split())) for _ in range (n)]
for i in d:
    avr=sum(i[1:])/i[0]
    cnt=0
    for j in i[1:]:
        if j>avr:
            cnt+=1
    print(f"{cnt/i[0]*100:.3f}"+"%")