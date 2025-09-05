import pygame
import moves

pygame.init()
font = pygame.font.Font('font/Pixeltype.ttf', 50)

#Mark the visited cases
def draw_visited(screen, board):
    for row in range(board.size):
        for col in range(board.size):
            state, index = board.state_list[row][col]
            if state == 1:
                number_text = font.render (f'{index}', False, 'Black')
                number_rect = number_text.get_rect(center = (board.board_list[row][col]))
                screen.blit(number_text, number_rect)
        


class Knight(pygame.sprite.Sprite):
    def __init__(self, board):
        super().__init__()
        self.surface = pygame.image.load('sprites/knight.png').convert_alpha()
        self.knight_width, self.knight_height = board.case_w, board.case_h
        self.image = pygame.transform.scale(self.surface, ( self.knight_width, self.knight_height))
        self.row = 0
        self.col = 0
        self.index = 1
        board.state_list[self.row][self.col] = (1,self.index)
        self.rect = self.image.get_rect(center = board.board_list[self.row][self.col])
        self.dragging = False
        self.board_rect = board.board_rect
        self.running = None

    def legal_moves(self, screen, board):

        self.legal = moves.knightMoves(self.row, self.col, board.state_list, board.size)

        for nrow, ncol in self.legal:
            pixel_x = self.board_rect.left + ncol * board.case_w
            pixel_y = self.board_rect.top + nrow * board.case_h
            pygame.draw.rect(screen, (255, 0, 0), pygame.Rect(pixel_x, pixel_y, board.case_w, board.case_h), 5)     

    def drag_and_drop(self, board):
        mouse_pos = pygame.mouse.get_pos()
        mouse_pressed = pygame.mouse.get_pressed()

        if self.rect.collidepoint(mouse_pos) and mouse_pressed[0]:
            self.dragging = True

        if not mouse_pressed[0] and self.dragging:
            self.snap_to_grid(mouse_pos, board)
            self.dragging = False

        if self.dragging:
            self.rect.center = mouse_pos

    def snap_to_grid(self, pos, board):
        
        #Calculate the center of the nearest case
        col = int((pos[0] - self.board_rect.left) // board.case_w)
        row = int((pos[1] - self.board_rect.top) // board.case_h)

        #Check if it is a legal case
        if (row,col) in self.legal:
            self.row = row
            self.col = col
            self.index += 1
            board.state_list[row][col] = (1,self.index)

        #Border Limits
        if self.col > board.size - 1:
            self.col = board.size - 1
        if self.col < 0:
            self.col = 0
        if self.row > board.size - 1:
            self.row = board.size - 1
        if self.row < 0:
            self.row = 0

        self.rect.center = board.board_list[self.row][self.col]

    def isWin(self, screen, board):
        if self.index != 1 and self.index == board.size*board.size:
            pygame.draw.rect(screen, (94,129,162), pygame.Rect(100, 200, 390, 150))
            lose_text_1 = font.render ("All cases visited.", False, 'Blue')
            lose_text_2 = font.render ("Congratulations !", False, 'Blue')
            lose_rect_1 = lose_text_1.get_rect(center = (300, 250))
            lose_rect_2 = lose_text_2.get_rect(center = (300, 300))
            screen.blit(lose_text_1, lose_rect_1)
            screen.blit(lose_text_2, lose_rect_2)
        elif not self.legal:
            pygame.draw.rect(screen, (94,129,162), pygame.Rect(100, 200, 390, 200))
            lose_text_1 = font.render ("No legal moves.", False, 'Blue')
            lose_text_2 = font.render ("Please press space", False, 'Blue')
            lose_text_3 = font.render ("to go back to the menu.", False, 'Blue')
            lose_rect_1 = lose_text_1.get_rect(center = (300, 250))
            lose_rect_2 = lose_text_2.get_rect(center = (300, 300))
            lose_rect_3 = lose_text_3.get_rect(center = (300, 350))
            screen.blit(lose_text_1, lose_rect_1)
            screen.blit(lose_text_2, lose_rect_2)
            screen.blit(lose_text_3, lose_rect_3)
        
    def update(self, screen, board):
        self.legal_moves(screen, board)
        self.drag_and_drop(board)
        self.isWin(screen, board)

knight = pygame.sprite.GroupSingle()

def knight_init(board):
    knight.add(Knight(board))

def knight_update(screen, board):
    knight.draw(screen)
    knight.update(screen, board)
