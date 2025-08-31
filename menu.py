import pygame

pygame.font.init()
font = pygame.font.Font('font/Pixeltype.ttf', 50)

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

def menu_display(screen,):
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
        size_rect = size_text.get_rect(center = (300, size_gap))
        size_array.append(i)
        screen.blit(size_text, size_rect)
        rect_gap += 70
        size_gap += 70

    running, size = press_button(rect_array, size_array)

    return running, size
    