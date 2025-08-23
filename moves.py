
def knightMoves(knight, y, x, board):
    if (len(board[0]) < y - 2 >= 0 and x + 1 <= 3):
        knight = board[y - 2][x + 1]
    elif (y - 2 >= 0 and x - 1 >= 0):
        knight = board[y - 2][x - 1]
    elif (y + 2 <= 3 and x + 1 <= 3):
        knight = board[y + 2][x + 1]
    elif (y + 2 <= 3 and x - 1 >= 0):
        knight = board[y + 2][x - 1]
    elif (y + 1 <= 3 and x - 2 >= 0):
        knight = board[y + 1][x - 2]
    elif (y + 1 <= 3 and x + 2 <= 3):
        knight = board[y + 1][x + 2]
    elif (y - 1 >= 0 and x + 2 <= 3):
        knight = board[y - 1][x + 2]
    elif (y - 1 >= 0 and x - 2 >= 0):
        knight = board[y - 1][x - 2]

    return knight