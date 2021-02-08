def solution(board, moves):
    answer = 0
    check_board = board
    size = len(board)
    gain_dolls = []
    for move in moves:
        for i in range(size):
            if check_board[i][move-1] != 0:
                gain_dolls.append(check_board[i][move-1])
                check_board[i][move-1] = 0
                break;
        if len(gain_dolls) > 1:
            if gain_dolls[-1] == gain_dolls[-2]:
                gain_dolls.pop()
                gain_dolls.pop()
                answer += 2
    return answer