# https://school.programmers.co.kr/learn/courses/30/lessons/160585
def success(arr): # o_win, x_win
    if arr == "OOO":
        return True, False
    elif arr == "XXX":
        return False, True
    else:
        return False, False

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
        o_win = x_win = False
        # 대각선
        diagonal = ''.join([board[i][i] for i in range(L)])
        o, x = success(diagonal)
        o_win = o_win or o
        x_win = x_win or x
        # 반대각선
        antidiagonal = ''.join([board[i][L-i-1] for i in range(L)]) 
        o, x = success(antidiagonal)
        o_win = o_win or o
        x_win = x_win or x
        # 가로 일치
        for b in board:
            o, x = success(b)
            o_win = o_win or o
            x_win = x_win or x
        # 세로 일치
        for i in range(L):
            column = [board[j][i] for j in range(L)]
            o, x = success(column)
            o_win = o_win or o
            x_win = x_win or x

        return o_win, x_win

    co, cx = cnt()
    # 1) 후공이 먼저 공격("X"만 1개 있을 때), 선공과 후공의 차이가 1이상
    if co - cx < 0 or co - cx > 1:
        return 0
    o_win, x_win = winner()
    # if o_win and x_win:
    #     return 0
    # 2) 게임이 끝났는데 계속 공격
    if o_win:
        if co == cx: 
            return 0
    elif x_win:
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

# O X .
# O X .
# O X .
# -> 이런 경우 고려해보기

# 나올 수 있는 게임 상황이 아닌 경우
# 1) 후공이 먼저 공격 - "X"만 1개 있을 때
# 2) 게임이 끝났는데 계속 공격
# -> 게임이 끝난 경우 : 가로, 세로, 대각선 3개 일치

# tmp 쓰지 말기