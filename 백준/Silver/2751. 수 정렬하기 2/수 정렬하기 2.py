import sys
input=sys.stdin.readline

n=int(input())
d=[int(input()) for _ in range (n)]
d.sort()

print('\n'.join(map(str,d)))