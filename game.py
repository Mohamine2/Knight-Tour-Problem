import pygame
import menu
import board
import knight_interactions
        

#Pygame initialization
pygame.init()
screen = pygame.display.set_mode((600,600))
pygame.display.set_caption('Knight Tour Problem')
clock = pygame.time.Clock()
running = False

while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            exit()

    if running:
        screen.blit(background_surface, (0,0))
        screen.blit(scaled_board, board_infos.board_rect)
        running = knight_interactions.knight_update(screen, board_infos)
        knight_interactions.draw_visited(screen, board_infos)
    else:
        running, size = menu.menu_display(screen)

        if running:
            background_surface, scaled_board, board_infos = board.board_init(screen, size)

            #Groups
            knight_interactions.knight_init(board_infos)


    pygame.display.update()
    clock.tick(60)
