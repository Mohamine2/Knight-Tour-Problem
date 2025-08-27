def knightMoves(y, x, state, size):
    moves = [
        (-2, 1), (-2, -1),
        (2, 1), (2, -1),
        (1, 2), (1, -2),
        (-1, 2), (-1, -2)
    ]
    
    legal_positions = []

    for dy, dx in moves:
        nx, ny = x + dx, y + dy
        if 0 <= nx < size and 0 <= ny < size:
            if state[nx][ny] == 0:
                legal_positions.append((nx, ny))
    
    return legal_positions


