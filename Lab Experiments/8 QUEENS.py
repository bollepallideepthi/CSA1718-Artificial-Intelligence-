def is_safe(board, row, col):

    for i in range(row):
        if board[i] == col:
            return False

    for i, j in zip(range(row-1, -1, -1), range(col-1, -1, -1)):
        if board[i] == j:
            return False

    for i, j in zip(range(row-1, -1, -1), range(col+1, 8)):
        if board[i] == j:
            return False

    return True


def solve(board, row=0):
    if row == 8:
        print_board(board)
        return True

    for col in range(8):
        if is_safe(board, row, col):
            board[row] = col
            if solve(board, row + 1):
                return True
    return False


def print_board(board):
    for row in range(8):
        line = ""
        for col in range(8):
            if board[row] == col:
                line += "Q "
            else:
                line += ". "
        print(line)
    print()


def main():
    board = [-1] * 8  
    if not solve(board):
        print("No solution found")


if __name__ == "__main__":
    main()