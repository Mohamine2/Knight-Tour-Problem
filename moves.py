def knightMoves(y, x):
    moves = [
        (-2, 1), (-2, -1),
        (2, 1), (2, -1),
        (1, 2), (1, -2),
        (-1, 2), (-1, -2)
    ]
    
    legal_positions = []

    for dy, dx in moves:
        ny, nx = y + dy, x + dx
        if 0 <= ny < 4 and 0 <= nx < 4:
            legal_positions.append((ny, nx))
    
    return legal_positions


