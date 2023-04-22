# https://school.programmers.co.kr/learn/courses/30/lessons/160585




def success(arr):
    if arr == "OOO":
        return "O"
    elif arr == "XXX":
        return "X"
    else:
        return False


def solution(board):
    L = len(board)
    def cnt():
        co = cx = 0
        for i in range(L):
            for j in range(L):
                if board[i][j] == "O":
                    co += 1
                elif board[i][j] == "X":
                    cx += 1
        return co, cx

    def winner():
        # 대각선
        diagonal = ''.join([board[i][i] for i in range(L)])
        if success(diagonal):
            return diagonal[0]
        # 대각선
        antidiagonal = ''.join([board[i][L-i-1] for i in range(L)]) 
        if success(antidiagonal):
            return antidiagonal[0]
        # 가로 일치
        for b in board:
            if success(b):
                return success(b)
        # 세로 일치
        for i in range(L):
            column = [board[j][i] for j in range(L)]
            if success(column):
                return success(column)
        return False

    co, cx = cnt()
    # 1) 후공이 먼저 공격("X"만 1개 있을 때), 선공과 후공의 차이가 1이상
    if co - cx < 0 or co - cx > 1:
        return 0
    win = winner()
    # 2) 게임이 끝났는데 계속 공격
    if win == "O":
        if co == cx: 
            return 0
    elif win == "X":
        if co > cx: 
            return 0
    return 1

print(solution(["O.X", ".O.", "..X"]))

# O X O
# X O X
# O X O

# X X X
# O O O
# . . .
# -> 이 경우 고려해보기

# 나올 수 있는 게임 상황이 아닌 경우
# 1) 후공이 먼저 공격 - "X"만 1개 있을 때
# 2) 게임이 끝났는데 계속 공격
# -> 게임이 끝난 경우 : 가로, 세로, 대각선 3개 일치

# "O"를 표시할 차례인데 "X"를 표시하거나 반대로 "X"를 표시할 차례인데 "O"를 표시한다.
# 선공이나 후공이 승리해서 게임이 종료되었음에도 그 게임을 진행한다.

# tmp 쓰지 말기