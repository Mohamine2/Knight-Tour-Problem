import pygame

pygame.init()
screen = pygame.display.set_mode((800,500))
pygame.display.set_caption('Knight Tour Problem')
clock = pygame.time.Clock()

while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            exit()

    pygame.display.update()
    clock.tick(60)
			