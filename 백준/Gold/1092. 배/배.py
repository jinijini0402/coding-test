import sys
n = int(input())
w = list(map(int, input().split()))
box = int(input())
box_w = list(map(int, input().split()))

w.sort(reverse=True)
box_w.sort(reverse=True)

if box_w[0] > w[0]:
    print(-1)
    sys.exit()

ans = 0
while box_w:
    for i in w:
        for j in box_w:
            if j <= i:
                box_w.remove(j)
                break
    ans += 1
            
print(ans)