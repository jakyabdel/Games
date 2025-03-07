import pygame
import sys
import random

pygame.init()

width = 400
height = 500
pygame.display.set_caption('Simple Stacking Game')
display = pygame.display.set_mode((width, height))
clock = pygame.time.Clock()

background = (23, 32, 42)

white = (236, 240, 241)


color = [(31, 40, 120), (38, 49, 148), (46, 58, 176), (53, 67, 203), (60, 76, 231), (99, 112, 236), (138, 148, 241), (177, 183, 245), (216, 219, 250), (236, 237, 253),
            (231, 249, 254), (207, 243, 252), (159, 231, 249), (111, 220, 247), (63, 208, 244), (15, 196, 241), (13, 172, 212), (11, 149, 183), (10, 125, 154), (8, 102, 125),
         (9, 81, 126), (12, 100, 156), (14, 119, 185), (30, 111, 202), (16, 137, 214), (18, 156, 243), (65, 176, 245), (113, 196, 248),(160, 215, 250), (208, 235, 253), (231, 245, 254),
         (232, 246, 243), (162, 217, 206), (162, 217, 206),
         (115, 198, 182), (69, 179, 157), (22, 160, 133),
         (19, 141, 117), (17, 122, 101), (14, 102, 85),
         (11, 83, 69),
         (21, 67, 96), (26, 82, 118), (31, 97, 141),
        (36, 113, 163), (41, 128, 185), (84, 153, 199),
        (127, 179, 213), (169, 204, 227), (212, 230, 241),
        (234, 242, 248),
         (230, 238, 251), (204, 221, 246), (153, 187, 237),
         (112, 152, 229), (51, 118, 220), (0, 84, 211),
         (0, 74, 186), (0, 64, 160), (0, 54, 135),
         (0, 44, 110)
         ]

colorIndex = 0

brickH = 10
brickW = 100

score = 0
speed = 3



class Brick:
    def __init__(self, x, y, color, speed):
        self.x = x
        self.y = y
        self.w = brickW
        self.h = brickH
        self.color = color
        self.speed = speed

    def draw(self):
        pygame.draw.rect(display, self.color, (self.x, self.y, self.w, self.h))

    def move(self):
        self.x += self.speed
        if self.x > width:
            self.speed *= -1
        if self.x + self.w < 1:
            self.speed *= -1



class Stack:
    def __init__(self):
        global colorIndex
        self.stack = []
        self.initSize = 25
        for i in range(self.initSize):
            newBrick = Brick(width/2 - brickW/2, height - (i + 1)*brickH, color[colorIndex], 0)
            colorIndex += 1
            self.stack.append(newBrick)

    def show(self):
        for i in range(self.initSize):
            self.stack[i].draw()

    def move(self):
        for i in range(self.initSize):
            self.stack[i].move()

    def addNewBrick(self):
        global colorIndex, speed

        if colorIndex >= len(color):
            colorIndex = 0
        
        y = self.peek().y
        if score > 50:
            speed += 0
        elif score%5 == 0:
            speed += 1
        
        newBrick = Brick(width, y - brickH, color[colorIndex], speed)
        colorIndex += 1
        self.initSize += 1
        self.stack.append(newBrick)
        
    def peek(self):
        return self.stack[self.initSize - 1]

    def pushToStack(self):
        global brickW, score
        b = self.stack[self.initSize - 2]
        b2 = self.stack[self.initSize - 1]
        if b2.x <= b.x and not (b2.x + b2.w < b.x):
            self.stack[self.initSize - 1].w = self.stack[self.initSize - 1].x + self.stack[self.initSize - 1].w - b.x
            self.stack[self.initSize - 1].x = b.x
            if self.stack[self.initSize - 1].w > b.w:
                self.stack[self.initSize - 1].w = b.w
            self.stack[self.initSize - 1].speed = 0
            score += 1
        elif b.x <= b2.x <= b.x + b.w:
            self.stack[self.initSize - 1].w = b.x + b.w - b2.x
            self.stack[self.initSize - 1].speed = 0
            score += 1
        else:
            gameOver()
        for i in range(self.initSize):
            self.stack[i].y += brickH

        brickW = self.stack[self.initSize - 1].w


def gameOver():
    loop = True

    font = pygame.font.SysFont("ARIAL", 60)
    text = font.render("Game Over!", True, white)

    textRect = text.get_rect()
    textRect.center = (width/2, height/2 - 80)

    while loop:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                close()
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_q:
                    close()
                if event.key == pygame.K_r:
                    gameLoop()
            if event.type == pygame.MOUSEBUTTONDOWN:
                gameLoop()
        display.blit(text, textRect)
        
        pygame.display.update()
        clock.tick()


def showScore():
    font = pygame.font.SysFont("ARIAL", 30)
    text = font.render("Score: " + str(score), True, white)
    display.blit(text, (10, 10))



def close():
    pygame.quit()
    sys.exit()


def gameLoop():
    global brickW, brickH, score, colorIndex, speed
    loop = True

    brickH = 10
    brickW = 100
    colorIndex = 0
    speed = 3

    score = 0

    stack = Stack()
    stack.addNewBrick()

    while loop:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                close()
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_q:
                    close()
                if event.key == pygame.K_r:
                    gameLoop()
            if event.type == pygame.MOUSEBUTTONDOWN:
                stack.pushToStack()
                stack.addNewBrick()
                

        display.fill(background)

        stack.move()
        stack.show()

        showScore()
        
        pygame.display.update()
        clock.tick(60)

gameLoop()
