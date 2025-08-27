import pygame
import moves

def press_button(rect, size):
        mouse_pos = pygame.mouse.get_pos()
        mouse_pressed = pygame.mouse.get_pressed()

        if rect[0].collidepoint(mouse_pos) and mouse_pressed[0]:
            return True, size[0]
        
        elif rect[1].collidepoint(mouse_pos) and mouse_pressed[0]:
            return True, size[1]

        elif rect[2].collidepoint(mouse_pos) and mouse_pressed[0]:
            return True, size[2]
        
        else:
            return False, None

def getCaseSize(board):
    width, height = board.get_size()
    width /= 4
    height /= 4
    return width, height

def boardToArray():
    board_array = [[None for _ in range(4)] for _ in range(4)]

    for row in range (4):
        for col in range(4):
            x = board_rect.left + row * case_w + case_w // 2
            y = board_rect.top + col * case_h + case_h // 2
            board_array[row][col] = (x, y)
    return board_array

#Mark the visited cases
def draw_visited():
    for row in range(4):
        for col in range(4):
            if state_array[row][col] == 1:
                pixel_x = board_rect.left + row * case_w
                pixel_y = board_rect.top + col * case_h
                pygame.draw.rect(screen, (0, 255, 0), pygame.Rect(pixel_x, pixel_y, case_w, case_h), 5)


class Knight(pygame.sprite.Sprite):
    def __init__(self, board_rect):
        super().__init__()
        self.surface = pygame.image.load('sprites/knight.png').convert_alpha()
        self.knight_width, self.knight_height = getCaseSize(scaled_board)
        self.image = pygame.transform.scale(self.surface, ( self.knight_width, self.knight_height))
        self.x = 0
        self.y = 0
        state_array[self.x][self.y] = 1
        self.rect = self.image.get_rect(center = board_array[self.x][self.y])
        self.dragging = False
        self.board_rect = board_rect

    def snap_to_grid(self, pos):
        
        #Find the center of the nearest case
        x = int((pos[0] - self.board_rect.left) // case_w)
        y = int((pos[1] - self.board_rect.top) // case_h)

        #Check if it is a legal case
        if (x,y) in self.legal:
            self.x = x
            self.y = y
            state_array[x][y] = 1

        #Border Limits
        if self.x > 3:
            self.x = 3
        if self.x < 0:
            self.x = 0
        if self.y > 3:
            self.y = 3
        if self.y < 0:
            self.y = 0

        self.rect.center = board_array[self.x][self.y]

    def legal_moves(self):

        # Récupère la position du cavalier en indices de grille
        col = self.x
        row = self.y

        self.legal = moves.knightMoves(row, col, state_array)

        for nx, ny in self.legal:
            pixel_x = self.board_rect.left + nx * case_w
            pixel_y = self.board_rect.top + ny * case_h
            pygame.draw.rect(screen, (255, 0, 0), pygame.Rect(pixel_x, pixel_y, case_w, case_h), 5)

    
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
            self.rect.center = mouse_pos
    

    def update(self):
        self.mouse_detection()
        self.legal_moves()
        

#Pygame initialization
pygame.init()
screen = pygame.display.set_mode((600,600))
pygame.display.set_caption('Knight Tour Problem')
clock = pygame.time.Clock()
game_active = False
font = pygame.font.Font('font/Pixeltype.ttf', 50)

while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            exit()

    if game_active:
        screen.blit(background_surface, (0,0))
        screen.blit(scaled_board,board_rect)
        knight.draw(screen)
        knight.update()
        draw_visited()
    else:
        screen.fill((94,129,162))
        title_text = font.render('KNIGHT TOUR PROBLEM', False, 'Black')
        title_rect = title_text.get_rect(center = (300,130))
        screen.blit(title_text, title_rect)

        size_text = font.render ('Choose the chessboard size', False, 'Blue')
        size_rect = size_text.get_rect(center = (300,200))
        screen.blit(size_text, size_rect)


        rect_array = []
        size_array = []
        rect_gap = 230
        size_gap = 260
        for i in range(3, 6):
            rect_array.append(pygame.draw.rect(screen, 'Black', pygame.Rect(150, rect_gap, 300, 50), 5))
            size_text = font.render (f'{i}x{i}', False, 'Blue')
            size_rect = size_text.get_rect(center = (300,size_gap))
            size_array.append(f'{i}x{i}')
            screen.blit(size_text, size_rect)
            rect_gap += 70
            size_gap += 70

        game_active, size = press_button(rect_array, size_array)

        if game_active:
            background_surface = pygame.image.load('sprites/background.png')

            #Board sprite
            board_surface = pygame.image.load(f'sprites/{size}.png').convert()
            scaled_board = pygame.transform.scale(board_surface, (500, 500))

            board_rect = scaled_board.get_rect(center = (screen.get_width()//2, screen.get_height()//2))

            case_w, case_h= getCaseSize(scaled_board)
            case_size = case_w * case_h
            board_array = boardToArray()

            #State array (0 = 'normal case' 1 = 'visited case')
            state_array = board = [[0 for _ in range(4)] for _ in range(4)]

            #Groups
            knight = pygame.sprite.GroupSingle()
            knight.add(Knight(board_rect))


    pygame.display.update()
    clock.tick(60)
			