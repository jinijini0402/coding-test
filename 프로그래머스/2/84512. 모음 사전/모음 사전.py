def solution(word):
    vowel=['A','E','I','O','U']
    dic=[]
    def dfs(cur:str):
        if 1<=len(cur)<=5:
            dic.append(cur)
        if len(cur)==5:
            return
        for i in vowel:
            dfs(cur+i)
    dfs("")
    return dic.index(word)+1