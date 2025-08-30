import pygame

pygame.init()

def getCaseSize(board, size):
    width, height = board.get_size()
    width /= size
    height /= size
    return width, height

def boardToArray(size, board_rect, case_w, case_h):
    board_array = [[None for _ in range(size)] for _ in range(size)]

    for row in range (size):
        for col in range(size):
            x = board_rect.left + col * case_w + case_w // 2
            y = board_rect.top + row * case_h + case_h // 2
            board_array[col][row] = (x, y)
    return board_array

def board_init(screen, size):
    background_surface = pygame.image.load('sprites/background.png')

    #Board sprite
    board_surface = pygame.image.load(f'sprites/{size}x{size}.png').convert()
    scaled_board = pygame.transform.scale(board_surface, (500, 500))

    board_rect = scaled_board.get_rect(center = (screen.get_width()//2, screen.get_height()//2))

    case_w, case_h = getCaseSize(scaled_board, size)
    board_array = boardToArray(size, board_rect, case_w, case_h)

    #State array (0 = 'normal case' 1 = 'visited case')
    state_array = [[0 for _ in range(size)] for _ in range(size)]

    return background_surface, scaled_board, board_rect, case_w, case_h, board_array, state_array
			
