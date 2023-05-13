# https://school.programmers.co.kr/learn/courses/30/lessons/159993

def solution(maps):
    R = len(maps)
    C = len(maps[0])
    r = l = lr = lc = 0
    min_try = float("inf")
    
    # 출발좌표("S"), 레버좌표("L") 찾기
    for i, m in enumerate(maps):
        if m.find("S") != -1:
            r = i
            c = m.find("S")
        if m.find("L") != -1:
            lr = i
            lc = m.find("L")
    
    while maps[r][c] not in ["E", "X"]:
        # left
        if c != 0 and maps[r][c] != "O":
            c -= 1
        # right [0, ..., C-1]
        if c != C-1 and maps[r][c] != "O":
            c += 1
        # up
        if r != 0 and maps[r][c] != "O":
            r -= 1
        # down [0, ..., R-1]
        if r != R-1 and maps[r][c] != "O":
            r += 1
    
    return min(min_try, 0)