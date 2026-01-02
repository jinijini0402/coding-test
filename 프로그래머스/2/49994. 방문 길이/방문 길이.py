def solution(dirs):
    cur = (0, 0)
    visited = set()
    answer = 0

    delta = {
        "U": (0, 1),
        "D": (0, -1),
        "L": (-1, 0),
        "R": (1, 0)
    }

    for ch in dirs:
        dx, dy = delta[ch]
        nx, ny = cur[0] + dx, cur[1] + dy
        if not (-5 <= nx <= 5 and -5 <= ny <= 5):
            continue
        nxt = (nx, ny)
        edge = (cur, nxt) if cur < nxt else (nxt, cur)
        if edge not in visited:
            visited.add(edge)
            answer += 1
        cur = nxt
    return answer
