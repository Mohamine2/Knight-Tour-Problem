import moves 

def backtrack(i, size, state, knight):

    if size*size == i:
        knight.index = i
        return True

    legal = moves.knightMoves(knight.row, knight.col, state, size)

    for ny, nx in legal:
        state[ny][nx] = (1,i)
        knight.row = ny
        knight.col = nx
        knight.index = i
        if backtrack(i+1,size, state, knight):
            return True
        state[ny][nx] = (0,0)

    return False
        