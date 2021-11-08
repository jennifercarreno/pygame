import pygame
pygame.init()

screen = pygame.display.set_mode([500, 500])

running = True
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
    
    #pink circle 
    # screen.fill((255, 255, 255))
    # color = (255, 0, 255)
    # position = (250, 250)
    # pygame.draw.circle(screen, color, position, 75)
    # pygame.display.flip()

    #Challenge 1
    screen.fill((255, 255, 255))
    red = (255, 0, 0)
    orange = (255, 141, 7)
    yellow = (255, 255, 0)
    green = (0, 255, 0)
    blue = (0, 0, 255)

    red_position = (125, 125)
    orange_position = (375, 125)
    yellow_position = (250, 250)
    green_position = (125, 375)
    blue_position = (375, 375)

    pygame.draw.circle(screen, red, red_position, 50)
    pygame.draw.circle(screen, orange, orange_position, 50)
    pygame.draw.circle(screen, yellow, yellow_position, 50)
    pygame.draw.circle(screen, green, green_position, 50)
    pygame.draw.circle(screen, blue, blue_position, 50)

    pygame.display.flip()




