import pygame
import moves

pygame.init()
font = pygame.font.Font('font/Pixeltype.ttf', 50)

#Mark the visited cases
def draw_visited(screen, board):
    for row in range(board.size):
        for col in range(board.size):
            state, index = board.state_array[row][col]
            if state == 1:
                number_text = font.render (f'{index}', False, 'Black')
                number_rect = number_text.get_rect(center = (board.board_array[row][col]))
                screen.blit(number_text, number_rect)


class Knight(pygame.sprite.Sprite):
    def __init__(self, board):
        super().__init__()
        self.surface = pygame.image.load('sprites/knight.png').convert_alpha()
        self.knight_width, self.knight_height = board.case_w, board.case_h
        self.image = pygame.transform.scale(self.surface, ( self.knight_width, self.knight_height))
        self.x = 0
        self.y = 0
        self.index = 1
        board.state_array[self.x][self.y] = (1,self.index)
        self.rect = self.image.get_rect(center = board.board_array[self.x][self.y])
        self.dragging = False
        self.board_rect = board.board_rect

    def legal_moves(self, screen, board):

        # Get the knight's position on the board_array
        col = self.x
        row = self.y

        self.legal = moves.knightMoves(col, row, board.state_array, board.size)

        for nx, ny in self.legal:
            pixel_x = self.board_rect.left + nx * board.case_w
            pixel_y = self.board_rect.top + ny * board.case_h
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
        
        #Find the center of the nearest case
        x = int((pos[0] - self.board_rect.left) // board.case_w)
        y = int((pos[1] - self.board_rect.top) // board.case_h)

        #Check if it is a legal case
        if (x,y) in self.legal:
            self.x = x
            self.y = y
            self.index += 1
            board.state_array[x][y] = (1,self.index)

        #Border Limits
        if self.x > board.size - 1:
            self.x = board.size - 1
        if self.x < 0:
            self.x = 0
        if self.y > board.size - 1:
            self.y = board.size - 1
        if self.y < 0:
            self.y = 0

        self.rect.center = board.board_array[self.x][self.y]
    
    def update(self, screen, board):
        self.legal_moves(screen, board)
        self.drag_and_drop(board)


knight = pygame.sprite.GroupSingle()

def knight_init(board):
    knight.add(Knight(board))

def knight_update(screen, board):
    knight.draw(screen)
    knight.update(screen, board)
