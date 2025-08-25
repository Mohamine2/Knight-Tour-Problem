def knightMoves(y, x, state):
    moves = [
        (-2, 1), (-2, -1),
        (2, 1), (2, -1),
        (1, 2), (1, -2),
        (-1, 2), (-1, -2)
    ]
    
    legal_positions = []

    for dy, dx in moves:
        nx, ny = x + dx, y + dy
        if 0 <= nx < 4 and 0 <= ny < 4:
            if state[nx][ny] == 0:
                legal_positions.append((nx, ny))
    
    return legal_positions


