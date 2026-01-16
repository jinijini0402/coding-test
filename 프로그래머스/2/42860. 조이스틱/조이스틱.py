def solution(name):
    ans=0
    for ch in name:
        o=ord(ch)-ord('A')
        if o<14:
            ans+=o
        else:
            ans+=26-o
    l=len(name)
    mn=l-1
    for i in range(l-1):
        if name[i+1]=='A':
            idx=i+1
            while idx<l and name[idx]=='A':
                idx+=1
            mn=min(
                mn,
                i*2+(l-idx),
                (l-idx)*2+i)
    return ans+mn