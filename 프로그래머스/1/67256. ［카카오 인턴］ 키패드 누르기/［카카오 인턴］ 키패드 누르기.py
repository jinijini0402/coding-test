def solution(numbers, hand):
    key=[(3,1),(0,0),(0,1),(0,2),(1,0),(1,1),(1,2),(2,0),(2,1),(2,2),(3,0),(3,2)]
    right=11
    left=10
    ans=[]
    for i in numbers:
        if i in [1,4,7]:
            ans.append("L")
            left=i
        elif i in [3,6,9]:
            ans.append("R")
            right=i
        else:
            rdist=abs(key[right][0]-key[i][0])+abs(key[right][1]-key[i][1])
            ldist=abs(key[left][0]-key[i][0])+abs(key[left][1]-key[i][1])
            if rdist>ldist:
                ans.append("L")
                left=i
            elif rdist<ldist:
                ans.append("R")
                right=i
            else:
                if hand=="right":
                    ans.append("R")
                    right=i
                else:
                    ans.append("L")
                    left=i
    return ''.join(ans)