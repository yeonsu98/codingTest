# https://school.programmers.co.kr/learn/courses/30/lessons/160585

def cor(arr):
    if arr == "OOO":
        return "O"
    elif arr == "XXX":
        return "X"
    else: return -1

def success(board):
    l = len(board)
    co = cx = 0  # O, X, .
    tmp = [[''], [''], ['']]
    
    for i in range(l):
        for j in range(l):
            if board[i][j] == "O":
                co += 1
            elif board[i][j] == "X":
                cx += 1
                
            # 대각선 일치
            if i == j:
                tmp[0] += board[i][j]
            elif l - j == i:
                tmp[1] += board[i][j]
    
    for i, b in enumerate(board):
        tmp[2].append(b[i])
        if cor(b):              # 가로 일치
            return co, cx, cor(b)
        elif cor(tmp[0]):       # 대각선 일치
            return co, cx, cor(tmp[0])
        elif cor(tmp[1]):       # 대각선 일치
            return co, cx, cor(tmp[1])
        elif cor(tmp[2]):       # 세로 일치                           
            return co, cx, cor(tmp[2])

def solution(board):
    co, cx, sus = success(board)
    
    # 1) 후공이 먼저 공격("X"만 1개 있을 때), 선공과 후공의 차이가 2이상
    if (co == 0 and cx == 1) or abs(co - cx) > 1:
        return 0
    # 2) 게임이 끝났는데 계속 공격
    print(sus)
    if sus == "O":
        if co == cx: return 0
    elif sus == "X":
        if co > cx: return 0
        
    return 1

# 나올 수 있는 게임 상황이 아닌 경우
# 1) 후공이 먼저 공격 - "X"만 1개 있을 때
# 2) 게임이 끝났는데 계속 공격
# -> 게임이 끝난 경우 : 가로, 세로, 대각선 3개 일치

# "O"를 표시할 차례인데 "X"를 표시하거나 반대로 "X"를 표시할 차례인데 "O"를 표시한다.
# 선공이나 후공이 승리해서 게임이 종료되었음에도 그 게임을 진행한다.