def knightMoves(y, x, state, size):
    moves = [
        (-2, 1), (-2, -1),
        (2, 1), (2, -1),
        (1, 2), (1, -2),
        (-1, 2), (-1, -2)
    ]
    
    legal_positions = []

    for dy, dx in moves:
        ny, nx = y + dy, x + dx
        if 0 <= nx < size and 0 <= ny < size:
            if state[ny][nx][0] == 0:
                legal_positions.append((ny, nx))
    
    return legal_positions


