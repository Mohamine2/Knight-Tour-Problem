import pygame

pygame.init()

class Board:
    def __init__(self, board_rect, size):
        self.size = size
        self.board_rect = board_rect
        self.case_w = board_rect.width // self.size
        self.case_h = board_rect.height // self.size

        #State list (0 = 'normal case' 1 = 'visited case')
        self.state_list = [[(0,0) for _ in range(self.size)] for _ in range(self.size)]

        self.board_list = boardToList(self)


def boardToList(board):

    board_list = [[None for _ in range(board.size)] for _ in range(board.size)]

    #row,col corresponds to the board's list coordinates
    #x,y corresponds to the screen's pixel coordinates
    for row in range (board.size):
        for col in range(board.size):
            x = board.board_rect.left + col * board.case_w + board.case_w // 2
            y = board.board_rect.top + row * board.case_h + board.case_h // 2
            board_list[row][col] = (x, y)
    return board_list

def board_init(screen, size):
    background_surface = pygame.image.load('sprites/background.png')

    #Board sprite
    board_surface = pygame.image.load(f'sprites/{size}x{size}.png').convert()
    scaled_board = pygame.transform.scale(board_surface, (500, 500))

    board_rect = scaled_board.get_rect(center = (screen.get_width()//2, screen.get_height()//2))

    board = Board(board_rect, size)

    return background_surface, scaled_board, board
			
