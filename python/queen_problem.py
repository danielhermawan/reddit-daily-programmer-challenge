def get_board(n):
    board = []
    for i in range(n):
        row = []
        for j in range(n):
            row.append(0)
        board.append(row)
    return board


def print_board(board):
    for row in board:
        for col in row:
            print(col, end='')
        print()


def can_place(board, col, row):
    if col == 0:
        return True
    for i in range(col):
        if board[row][i] == 1: return False
    j = 0
    while j < col and j < row:
        if board[row - j - 1][col - j - 1] == 1: return False
        j += 1
    j = 0
    while row + j + 1 < len(board) and j < col:
        if board[row + j + 1][col - j - 1] == 1:
            return False
        j += 1
    return True


def can_solve(board, col):
    if col >= len(board):
        return True
    for i in range(len(board)):
        if can_place(board, col, i):
            board[i][col] = 1
            if can_solve(board, col + 1):
                return True
            board[i][col] = 0
    return False


def queen_problem(n):
    res = get_board(n)
    if can_solve(res, 0):
        return res


print_board(queen_problem(5))
