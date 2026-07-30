# Tic-Tac-Toe Game in Python

board = [" "] * 9

# Function to display the board
def show():
    print()
    print(board[0], "|", board[1], "|", board[2])
    print("--+---+--")
    print(board[3], "|", board[4], "|", board[5])
    print("--+---+--")
    print(board[6], "|", board[7], "|", board[8])
    print()

# Function to check winner
def win(player):
    wins = [
        (0, 1, 2), (3, 4, 5), (6, 7, 8),
        (0, 3, 6), (1, 4, 7), (2, 5, 8),
        (0, 4, 8), (2, 4, 6)
    ]

    for a, b, c in wins:
        if board[a] == board[b] == board[c] == player:
            return True
    return False

player = "X"

# Game loop
for i in range(9):
    show()

    pos = int(input("Player " + player + ", enter position (1-9): ")) - 1

    if board[pos] == " ":
        board[pos] = player

        if win(player):
            show()
            print("Player", player, "wins!")
            break

        # Change player
        if player == "X":
            player = "O"
        else:
            player = "X"

    else:
        print("Position already taken! Try again.")

else:
    show()
    print("Match Draw!")