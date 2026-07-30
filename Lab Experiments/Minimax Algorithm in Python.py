# Minimax Algorithm in Python

import math
values = [3, 5, 2, 9]
def minimax(depth, index, isMax):
    if depth == 2:
        return values[index]
    if isMax:
        return max(
            minimax(depth + 1, index * 2, False),
            minimax(depth + 1, index * 2 + 1, False)
        )
    else:
        return min(
            minimax(depth + 1, index * 2, True),
            minimax(depth + 1, index * 2 + 1, True)
        )
best = minimax(0, 0, True)

print("Best possible score is:", best)
