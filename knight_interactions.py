import pygame
import moves

pygame.init()

#Mark the visited cases
def draw_visited(screen, size, state_array, board_rect, case_w, case_h):
    for row in range(size):
        for col in range(size):
            if state_array[row][col] == 1:
                pixel_x = board_rect.left + row * case_w
                pixel_y = board_rect.top + col * case_h
                pygame.draw.rect(screen, (0, 255, 0), pygame.Rect(pixel_x, pixel_y, case_w, case_h), 5)


class Knight(pygame.sprite.Sprite):
    def __init__(self, board_rect,state_array, board_array, case_w, case_h):
        super().__init__()
        self.surface = pygame.image.load('sprites/knight.png').convert_alpha()
        self.knight_width, self.knight_height = case_w, case_h
        self.image = pygame.transform.scale(self.surface, ( self.knight_width, self.knight_height))
        self.x = 0
        self.y = 0
        state_array[self.x][self.y] = 1
        self.rect = self.image.get_rect(center = board_array[self.x][self.y])
        self.dragging = False
        self.board_rect = board_rect

    def legal_moves(self, screen, state_array, size, case_w, case_h):

        # Get the knight's position on the board_array
        col = self.x
        row = self.y

        self.legal = moves.knightMoves(row, col, state_array, size)

        for nx, ny in self.legal:
            pixel_x = self.board_rect.left + nx * case_w
            pixel_y = self.board_rect.top + ny * case_h
            pygame.draw.rect(screen, (255, 0, 0), pygame.Rect(pixel_x, pixel_y, case_w, case_h), 5)     

    def drag_and_drop(self, case_w, case_h, state_array, board_array, size):
        mouse_pos = pygame.mouse.get_pos()
        mouse_pressed = pygame.mouse.get_pressed()

        if self.rect.collidepoint(mouse_pos) and mouse_pressed[0]:
            self.dragging = True

        if not mouse_pressed[0] and self.dragging:
            self.snap_to_grid(mouse_pos, case_w, case_h, state_array, board_array, size)
            self.dragging = False

        if self.dragging:
            self.rect.center = mouse_pos

    def snap_to_grid(self, pos, case_w, case_h, state_array, board_array, size):

        size = int(size)
        
        #Find the center of the nearest case
        x = int((pos[0] - self.board_rect.left) // case_w)
        y = int((pos[1] - self.board_rect.top) // case_h)

        #Check if it is a legal case
        if (x,y) in self.legal:
            self.x = x
            self.y = y
            state_array[x][y] = 1

        #Border Limits
        if self.x > size - 1:
            self.x = size - 1
        if self.x < 0:
            self.x = 0
        if self.y > size - 1:
            self.y = size - 1
        if self.y < 0:
            self.y = 0

        self.rect.center = board_array[self.x][self.y]
    
    def update(self, screen, state_array, board_array, size, case_w, case_h):
        self.legal_moves(screen, state_array, size, case_w, case_h)
        self.drag_and_drop(case_w, case_h, state_array, board_array, size)


knight = pygame.sprite.GroupSingle()

def knight_init(board_rect,state_array, board_array, case_w, case_h):
    knight.add(Knight(board_rect,state_array, board_array, case_w, case_h))

def knight_update(screen, state_array, board_array, size, case_w, case_h):
    knight.draw(screen)
    knight.update(screen, state_array, board_array, size, case_w, case_h)
