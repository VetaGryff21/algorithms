import pygame
# import time
import random

pygame.init()

white = (255, 255, 255)
black = (0, 0, 0)
red = (255, 0, 0)
green = (0, 155, 0)

display_width = 800
display_height = 600

gameDisplay = pygame.display.set_mode((display_width, display_height))
pygame.display.set_caption('Snake')


img = pygame.image.load('C:/Users/Victoria/My Documents/snakehead.png')
appleimg = pygame.image.load('C:/Users/Victoria/My Documents/apple.png')
flyimg = pygame.image.load('C:/Users/Victoria/My Documents/slither/fly2.png')


clock = pygame.time.Clock()

block_size = 10
FPS = 30

direction = "right"

font = pygame.font.SysFont(None, 25)


def pause():
    paused = True

    while paused:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                quit()

            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_c:
                    paused = False
                if event.key == pygame.K_q:
                    pygame.quit()
                    quit()
        gameDisplay.fill(black)
        message_to_screen("Paused", white, -100)
        message_to_screen("Press C to continue or Q to quit", white, 25)
        pygame.display.update()
        clock.tick(5)


def score(score):
    text = font.render("Score: " + str(score), True, white)
    gameDisplay.blit(text, [0, 0])


def randAppleGen():
    randAppleX = round(random.randrange(0, display_width - block_size) / 10.0) * 10.0
    randAppleY = round(random.randrange(0, display_height - block_size) / 10.0) * 10.0

    return randAppleX, randAppleY


def randFlyGen():
    randFlyX = round(random.randrange(0, display_width - block_size) / 10.0) * 10.0
    randFlyY = round(random.randrange(0, display_height - block_size) / 10.0) * 10.0

    return randFlyX, randFlyY


def game_intro():
    intro = True

    while intro:

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                quit()
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_c:
                    intro = False
                if event.key == pygame.K_q:
                    pygame.quit()
                    quit()

        gameDisplay.fill(black)
        message_to_screen("The objective of the game is to eat flies but don't eat the apples!", white, -70)
        message_to_screen("Press C to continue or Q to quit", white, -30)

        pygame.display.update()
        clock.tick(15)


def snake(block_size, snakelist):
    if direction == "right":
        head = pygame.transform.rotate(img, 270)
    if direction == "left":
        head = pygame.transform.rotate(img, 90)
    if direction == "up":
        head = pygame.transform.rotate(img, 0)
    if direction == "down":
        head = pygame.transform.rotate(img, 180)
    gameDisplay.blit(head, (snakelist[-1][0], snakelist[-1][1]))
    for XnY in snakelist[:-1]:
        pygame.draw.rect(gameDisplay, green, [XnY[0], XnY[1], block_size, block_size])


def text_objects(text, color):
    textSurface = font.render(text, True, color)
    return textSurface, textSurface.get_rect()


def message_to_screen(msg, color, y_displace=0):
    textSurf, textRect = text_objects(msg, color)
    # screen_text = font.render(msg, True, color)
    # gameDisplay.blit(screen_text, [display_width/2, display_height/2])
    textRect.center = (display_width / 2), (display_height / 2) + y_displace
    # y_displace: adding whatever amount of pixels needing to be displaced
    gameDisplay.blit(textSurf, textRect)


def gameLoop():
    global direction

    snakeList = []
    snakeLength = 1

    gameExit = False
    gameOver = False

    lead_x = display_width / 2
    lead_y = display_height / 2

    lead_x_change = 10
    lead_y_change = 10

    randAppleX = round(random.randrange(0, display_width - block_size) / 10.0) * 10.0
    randAppleY = round(random.randrange(0, display_height - block_size) / 10.0) * 10.0
    # has to be put in gameLoop

    randFlyX = round(random.randrange(0, display_width - block_size) / 10.0) * 10.0
    randFlyY = round(random.randrange(0, display_height - block_size) / 10.0) * 10.0

    while not gameExit:

        while gameOver == True:
            gameDisplay.fill(white)
            message_to_screen("Game over", red, -50)
            message_to_screen("Press C to continue or Q to quit", black, 5)
            pygame.display.update()

            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    gameExit = True
                    gameOver = False
                if event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_q:
                        gameExit = True
                        gameOver = False
                    if event.key == pygame.K_c:
                        gameLoop()

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                gameExit = True
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_LEFT:
                    direction = "left"
                    lead_x_change = -block_size
                    lead_y_change = 0
                elif event.key == pygame.K_RIGHT:
                    direction = "right"
                    lead_x_change = block_size
                    lead_y_change = 0
                elif event.key == pygame.K_UP:
                    direction = "up"
                    lead_y_change = -block_size
                    lead_x_change = 0
                elif event.key == pygame.K_DOWN:
                    direction = "down"
                    lead_y_change = block_size
                    lead_x_change = 0

                elif event.key == pygame.K_p:
                    pause()

        if lead_x > display_width:
            lead_x = 0
        elif lead_x < 0:
            lead_x = display_width
        elif lead_y > display_height:
            lead_y = 0
        elif lead_y < 0:
            lead_y = display_height

        lead_x += lead_x_change
        lead_y += lead_y_change

        gameDisplay.fill(black)

        apple = pygame.transform.rotate(appleimg, 0)
        fly = pygame.transform.rotate(flyimg, 0)
        AppleThickness = 10
        FlyThickness = 10

        gameDisplay.blit(appleimg, (randAppleX, randAppleY))
        gameDisplay.blit(flyimg, (randFlyX, randFlyY))

        snakeHead = []
        snakeHead.append(lead_x)
        snakeHead.append(lead_y)
        snakeList.append(snakeHead)

        if len(snakeList) > snakeLength:
            del snakeList[0]
            for eachSegment in snakeList[:-1]:
                if eachSegment == snakeHead:
                    gameOver = True

        snake(block_size, snakeList)


        score(snakeLength - 1)
        pygame.display.update()

        if lead_x == randFlyX and lead_y == randFlyY:
            randFlyX, randFlyY = randFlyGen()
            snakeLength += 1
            randAppleGen()

        elif lead_x == randAppleX and lead_y == randAppleY:
            randAppleX, randAppleY = randAppleGen()
            # randAppleX = round(random.randrange(0,display_width-block_size)/10.0)*10.0
            # randAppleY = round(random.randrange(0,display_height-block_size)/10.0)*10.0
            snakeLength -= 10
            randAppleGen()


        elif snakeLength < 0:
            gameOver = True

        clock.tick(FPS)


    message_to_screen("You suck", red)
    # deleted:
    # pygame.display.update()
    # have to add update again
    # time.sleep(2)

    pygame.quit()
    quit()


game_intro()
gameLoop()