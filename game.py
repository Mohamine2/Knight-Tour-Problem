import pygame
import menu
import board
import knight_interactions
import solver
        

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
            if event.type == pygame.KEYDOWN and event.key == pygame.K_SPACE:
                running = False


    if running:
        screen.blit(background_surface, (0,0))
        screen.blit(scaled_board, board_infos.board_rect)
        knight_interactions.draw_visited(screen, board_infos)
        knight_interactions.knight_update(screen, board_infos)
        # solver.backtrack(1, size, board_infos.state_list, 0, 0)

    else:
        running, size = menu.menu_display(screen)

        if running:
            background_surface, scaled_board, board_infos = board.board_init(screen, size)

            #Groups
            knight_interactions.knight_init(board_infos)


    pygame.display.update()
    clock.tick(60)
