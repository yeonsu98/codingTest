# https://school.programmers.co.kr/learn/courses/30/lessons/169199

def move(r, c, board):
    mv = []
    R = len(board)    
    C = len(board[0])
    
    # left 
    rr = r
    cc = c
    while((c != 0) and (board[r][c] != 'D')):
        c -= 1
    if c != cc: mv.append([rr, cc])
        
    # right [0, ..., C-1]
    rr = r
    cc = c
    while((c != C-1) and (board[r][c] != 'D')):
        c += 1
    if c != cc: mv.append([rr, cc])
    
    # up
    rr = r
    cc = c
    while((r != 0) and (board[r][c] != 'D')):
        r -= 1
    if r != rr: mv.append([rr, cc])
    
    # down [0, ..., R-1]
    rr = r
    cc = c
    while((r != R-1) and (board[r][c] != 'D')):
        r += 1
    if r != rr: mv.append([rr, cc])
    
    return mv
    
def solution(board):
    r = c = 0
    for i, b in enumerate(board):
        if b.find('R') != -1:
            r = i
            c = b.find('R')
            break
            
    q = []
    visited = [[0]*len(board[0]) for _ in range(len(board))]
    q.append([r, c, 0])
    
    while q:
        nr, nc, cnt = q.pop(0)
        if board[nr][nc] == 'G': 
            return cnt
        
        if visited[nr][nc] == 1: 
            continue
        visited[nr][nc] = 1
        
        mv = move(nr, nc, board)
        for tr, tc in mv:
            q.append([tr, tc, cnt+1])
    
    return -1