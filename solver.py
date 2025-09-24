import moves 

def backtrack(i, size, state, y , x):

    if size*size == i:
        return True

    legal = moves.knightMoves(y, x, state, size)

    for ny, nx in legal:
        state[ny][nx] = (1,i)
        if backtrack(i+1, size, state, ny, nx):
            return True
        state[ny][nx] = (0,0)

    return False
        