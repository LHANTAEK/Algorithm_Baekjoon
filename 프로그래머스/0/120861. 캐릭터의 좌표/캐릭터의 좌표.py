def solution(keyinput, board):
    answer = []
    x = 0
    y = 0
    for i in keyinput:
        if i == 'left':
            if x > -int(board[0] / 2):
                x += -1
        elif i == 'right':
            if x < int(board[0] / 2):
                x += 1
        elif i == 'up':
            if y < int(board[1] / 2):
                y += 1
        else:
            if y > -int(board[1] / 2):
                y += -1
    answer += [x,y]
    return answer