def solution(numbers):
    ans=[]
    for i in numbers:
        if i%2==0:
            ans.append(i+1)
        else:
            binary="0"+bin(i)[2:]
            idx=binary.rfind("01")
            binary=binary[:idx]+"10"+binary[idx+2:]
            ans.append(int(binary,2))
    return ans