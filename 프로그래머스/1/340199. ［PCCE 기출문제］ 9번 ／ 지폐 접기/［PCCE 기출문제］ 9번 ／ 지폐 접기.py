def solution(wallet, bill):
    ans=0
    wallet.sort(reverse=True)
    bill.sort(reverse=True)
    while wallet[0]<bill[0] or wallet[1]<bill[1]:
        bill[0]=bill[0]//2
        ans+=1
        wallet.sort(reverse=True)
        bill.sort(reverse=True)
    return ans