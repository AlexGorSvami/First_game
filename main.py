import pygame


pygame.init()
screen = pygame.display.set_mode((600, 300), )  #flags=pygame.NOFRAME
pygame.display.set_caption('My first game')
icon = pygame.image.load('images/game_icon.png')
pygame.display.set_icon(icon)

running = True

while running:

    # screen.fill((50, 168, 98))

    pygame.display.update()

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
            pygame.quit()
        elif event.type == pygame.KEYDOWN:
            if event.key == pygame.K_p:
                screen.fill((50, 121, 168))