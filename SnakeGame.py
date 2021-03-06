# Game code base from https://github.com/kmeng01/pygame-snake/blob/master/snake.py


import pygame
import time
import random

pygame.init()

white = (255,255,255)
black = (0,0,0)
red = (255,0,0)
green = (0,255,0)
blue = (0,0,255)
purple = (128,0,128)

display_w = 300
display_h = 300

clock = pygame.time.Clock()
fps = 10
block_size = 50

font = pygame.font.SysFont(None, 25)

def snake(block_size, snakeList, snakeHead, lead_x, lead_y):
    for XnY in snakeList:
        pygame.draw.rect(gameDisplay, purple, [XnY[0],XnY[1],block_size,block_size])
        pygame.draw.rect(gameDisplay, red, [lead_x,lead_y,block_size,block_size])

def message_to_screen(msg,color,x,y):
    screen_text = font.render(msg, True, color)
    gameDisplay.blit(screen_text, [x,y])

gameDisplay = pygame.display.set_mode((display_w,display_h))
pygame.display.set_caption("Slithery Snake")

def gameLoop():
    gameExit = False
    gameOver = False

    lead_x = display_w/2
    lead_y = display_h/2
    lead_x_change = 0
    lead_y_change = 0

    snakeList = []
    snakeLength = 1

    score = 0

    randAppleX = round(random.randrange(0, display_w - block_size)/block_size)*block_size
    randAppleY = round(random.randrange(0, display_h - block_size)/block_size)*block_size

    while not gameExit:
        while gameOver == True:
            gameDisplay.fill(red)
            message_to_screen("Your snake has died! Press C to continue or Q to quit.", white, display_h/2, display_w/2)
            message_to_screen(''.join(["Your score was: ",str(score)]), white, display_h/2, display_w/2)
            pygame.display.update()

            for event in pygame.event.get():
                if event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_c:
                        gameLoop()
                    if event.key == pygame.K_q:
                        gameExit = True
                        gameOver = False
                elif event.type == pygame.QUIT:
                    gameExit = True
                    gameOver = False

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                gameExit = True
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_LEFT:
                    lead_x_change = -block_size
                    lead_y_change = 0
                elif event.key == pygame.K_RIGHT:
                    lead_x_change = block_size
                    lead_y_change = 0
                elif event.key == pygame.K_DOWN:
                    lead_y_change = block_size
                    lead_x_change = 0
                elif event.key == pygame.K_UP:
                    lead_y_change = -block_size
                    lead_x_change = 0

        if lead_x >= display_w or lead_x <0 or lead_y >= display_h or lead_y <0:
            gameOver = True

        lead_x += lead_x_change
        lead_y += lead_y_change
        gameDisplay.fill(white)
        message_to_screen(''.join(["Score: ",str(score)]), black, 10,10)
        pygame.draw.rect(gameDisplay, black, [randAppleX, randAppleY, block_size, block_size])

        snakeHead = []
        snakeHead.append(lead_x)
        snakeHead.append(lead_y)
        snakeList.append(snakeHead)

        if len(snakeList) > snakeLength:
            del snakeList[0]
        for eachSegment in snakeList[:-1]:
            if eachSegment == snakeHead:
                gameOver = True

        snake(block_size, snakeList, snakeHead, lead_x, lead_y)

        if lead_x == randAppleX and lead_y == randAppleY:
            randAppleX = round(random.randrange(0, display_w - block_size)/block_size)*block_size
            randAppleY = round(random.randrange(0, display_h - block_size)/block_size)*block_size
            snakeLength += 1
            score += 1
            message_to_screen(''.join(["Score: ",str(score)]), black, 10, 10)

        pygame.display.update()

        clock.tick(fps)

    pygame.quit()

gameLoop()