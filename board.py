import pygame

def getCaseSize(board):
    width, height = board.get_size()
    width /= 4
    height /= 4
    return width, height

class Knight(pygame.sprite.Sprite):
    def __init__(self, board_rect):
        super().__init__()
        self.surface = pygame.image.load('sprites/knight.png').convert_alpha()
        self.knight_width, self.knight_height = getCaseSize(scaled_board)
        self.image = pygame.transform.scale(self.surface, ( self.knight_width, self.knight_height))
        self.rect = self.image.get_rect(center=(board_rect.left + self.knight_width//2,
                                                board_rect.top + self.knight_height//2))
        self.dragging = False
        self.board_rect = board_rect
    
    def mouse_detection(self):
        mouse_pos = pygame.mouse.get_pos()
        mouse_pressed = pygame.mouse.get_pressed()

        if self.rect.collidepoint(mouse_pos) and mouse_pressed[0]:
            self.dragging = True

        if not mouse_pressed[0] and self.dragging:
            # Quand on relâche → snap sur la case
            self.snap_to_grid(mouse_pos)
            self.dragging = False

        if self.dragging:
            x, y = mouse_pos
            # Restriction à la zone du plateau
            if self.board_rect.left < x < self.board_rect.right and self.board_rect.top < y < self.board_rect.bottom:
                self.rect.center = mouse_pos
    
    def snap_to_grid(self, pos):
        """Aligne le chevalier au centre de la case la plus proche"""
        case_w, case_h = getCaseSize(scaled_board)

        col = int((pos[0] - self.board_rect.left) // case_w)
        row = int((pos[1] - self.board_rect.top) // case_h)

        # Centre exact de la case
        snapped_x = self.board_rect.left + col * case_w + case_w // 2
        snapped_y = self.board_rect.top + row * case_h + case_h // 2
        self.rect.center = (snapped_x, snapped_y)

    def update(self):
        self.mouse_detection()
        

#Pygame initialization
pygame.init()
screen = pygame.display.set_mode((600,600))
pygame.display.set_caption('Knight Tour Problem')
clock = pygame.time.Clock()

background_surface = pygame.image.load('sprites/background.png')

#Board sprite
board_surface = pygame.image.load('sprites/4x4.png').convert()
scaled_board = pygame.transform.scale(board_surface, (500, 500))

board_rect = scaled_board.get_rect(center = (screen.get_width()//2, screen.get_height()//2))

#Groups
knight = pygame.sprite.GroupSingle()
knight.add(Knight(board_rect))

while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            exit()

    screen.blit(background_surface, (0,0))
    screen.blit(scaled_board,board_rect)
    knight.draw(screen)
    knight.update()

    pygame.display.update()
    clock.tick(60)
			