# coding: utf8
import pygame, time, random

pygame.init()

# функция для отрисовки змейки
def snake(headname, bodyname, snakeList, lead_x, lead_y):
    for XnY in snakeList:
        gameDisplay.blit(pygame.image.load(bodyname),(XnY[0],XnY[1]))
        gameDisplay.blit(pygame.image.load(bodyname),(lead_x, lead_y))

# функция для отображения текста
def message_to_screen(msg, color,x,y):
    screen_txt = font.render(msg, True, color)
    gameDisplay.blit(screen_txt, [x,y])

# задаем цвета заранее
white = (255,255,255)
black = (0,0,0)
red = (255,0,0)
green = (0,255,0)

# задаем размеры окна и блоков змейки
display_width = 600
display_height = 600
block_size = 25

# создаем окно
gameDisplay = pygame.display.set_mode((display_width, display_height))
pygame.display.set_caption("Игра - Змейка")

# объявим шрифт
font = pygame.font.SysFont("Comicsans", 32)

# рубильник для выключения
gameExit = False

# координаты головы змейки
lead_x = display_width/2
lead_y = display_height/2
# направление движения змейки
lead_x_change = 0
lead_y_change = 0

snakeList = []
snakeLength = 1
score = 0

# случайные координаты яблока
appleX = round(random.randrange(0, display_width - block_size)/block_size) * block_size
appleY = round(random.randrange(0, display_height - block_size)/block_size) * block_size

# цикл самой игры
while not gameExit:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            gameExit = True
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_LEFT:
                lead_x_change = -block_size
                lead_y_change = 0
            if event.key == pygame.K_RIGHT:
                lead_x_change = block_size
                lead_y_change = 0
            if event.key == pygame.K_DOWN:
                lead_x_change = 0
                lead_y_change = block_size
            if event.key == pygame.K_UP:
                lead_x_change = 0
                lead_y_change = -block_size

    gameDisplay.fill(white)

    # столковение со стеной
    if lead_x >= display_width - block_size or lead_x <= 0 or lead_y >= display_height - block_size or lead_y <= 0:
        gameDisplay.fill(black)
        message_to_screen(''.join(["GAME OVER! Score: ", str(score)]), white, 200, 200)
        pygame.display.update()
        time.sleep(3)
        gameExit = True

    # движение змейки
    lead_x += lead_x_change
    lead_y += lead_y_change
    snakeHead = [lead_x, lead_y]
    snakeList.append(snakeHead)
    if len(snakeList) > snakeLength:
        del snakeList[0]
    # столковение с самой собой
    for eachSegment in snakeList[:-1]:
        if eachSegment == snakeHead:
            gameDisplay.fill(black)
            message_to_screen(''.join(["GAME OVER! Score: ", str(score)]), white, 100, 200)
            pygame.display.update()
            time.sleep(3)
            gameExit = True
    # столкновение с яблоком
    if lead_x == appleX and lead_y == appleY:
        snakeLength += 1
        score += 1
        appleX = round(random.randrange(0, display_width - block_size) / block_size) * block_size
        appleY = round(random.randrange(0, display_height - block_size) / block_size) * block_size

    # отображение очков
    message_to_screen(''.join(["Score: ", str(score)]), black, 10, 10)
    # отображение яблока
    pygame.draw.rect(gameDisplay, green, [appleX, appleY, block_size, block_size])
    # отображение змейки
    snake(block_size, snakeList)
    pygame.display.update()
    pygame.time.delay(150)

pygame.quit()