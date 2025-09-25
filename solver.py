import moves 

def backtrack(i, size, state, knight):

    if size*size == i:
        knight.index = i
        return True

    legal = moves.knightMoves(knight.row, knight.col, state, size)

    for nrow, ncol in legal:
        state[nrow][ncol] = (1,i+1)
        knight.row = nrow
        knight.col = ncol
        knight.index = i+1
        if backtrack(i+1,size, state, knight):
            return True
        state[nrow][ncol] = (0,0)

    return False
        