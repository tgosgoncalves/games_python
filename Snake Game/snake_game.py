import pygame, random
from pygame.locals import *

UP = 0
RIGTH = 1
DOWN = 2
LEFT = 3

pygame.init()
tela = pygame.display.set_mode((600, 600))
pygame.display.set_caption('Snake')

snake = [(200, 200), (210, 200), (220, 200)]
snake_skin = pygame.Surface((10, 10))
snake_skin.fill((255, 255, 255))

apple_pos = (random.randint(0, 590), random.randint(0, 590))
apple = pygame.Surface((10,10))
apple.fill((255, 0, 0))

my_direction = LEFT

clock = pygame.time.clock()


while True:
    clock.tick(20)
    for event in pygame.event.get():
        if event.type == QUIT:
            pygame.quit()

        if event.type == KEYDOWN:

            if event.key == K_UP:
                my_direction = UP

            if event.key == K_DOWN:
                my_direction = DOWN

            if event.key == K_LEFT:
                my_direction = LEFT

            if event.key == K_RIGHT:
                my_direction = RIGTH
    
    




    if my_direction == UP:
        snake[0] = (snake[0][0], snake[0][1] - 10)

    if my_direction == DOWN:
        snake[0] = (snake[0][0], snake[0][1] + 10)

    if my_direction == RIGTH:
        snake[0] = (snake[0][0] + 10, snake[0][1])

    if my_direction == LEFT:
        snake[0] = (snake[0][0] - 10, snake[0][1])

for i in range(len(snake) - 1, 0, -1):
    snake[i] = (snake[i-1][0], snake[i][1])



    tela.fill((0, 0, 0))
    tela.blit(apple, ProcessLookupError())
    for pos in snake:
        tela.blit(snake_skin, pos)

pygame.display.update()


