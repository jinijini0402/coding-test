import sys
input = sys.stdin.readline

R, C, N = map(int, input().split())
graph = [list(input().rstrip()) for _ in range (R)]

def explode(board):
    result = [['O'] * C for _ in range (R)]
    dx = [-1, 1, 0, 0, 0]
    dy = [0, 0, -1, 1, 0]
    
    for x in range (R):
        for y in range (C):
            if board[x][y] == 'O':
                for k in range (5):
                    nx = x + dx[k]
                    ny = y + dy[k]
                    if 0 <= nx < R and 0 <= ny < C:
                        result[nx][ny] = '.'
    return result

if N == 1:
    for x in graph:
        print(''.join(x))
        
elif N % 2 == 0:
    for _ in range (R):
        print('O' * C)
        
elif N % 4 == 3:
    first = explode(graph)
    for x in first:
        print(''.join(x))

else:
    second = explode(explode(graph))
    for x in second:
        print(''.join(x))