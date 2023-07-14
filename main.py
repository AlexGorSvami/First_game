import pygame


pygame.init()
screen = pygame.display.set_mode((600, 300), )  #flags=pygame.NOFRAME
pygame.display.set_caption('My first game')
icon = pygame.image.load('images/game_icon.png')
pygame.display.set_icon(icon)



square = pygame.Surface((50, 150))
square.fill('Green')

myfont = pygame.font.Font('fonts/Tektur-ExtraBold.ttf', 40)
text_surface = myfont.render('First game', True, 'Blue')

player = pygame.image.load('images/game_icon.png')


running = True

while running:

    pygame.draw.circle(screen, 'Blue', (10, 20), 5)
    screen.blit(square, (10, 0))
    screen.blit(text_surface, (300, 100))
    screen.blit(player, (50, 50))
    pygame.display.update()

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
            pygame.quit()
