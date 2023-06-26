"""
Snake Game
Author : Matis Messence
01/05/2023

I am on a coding adventure to learn python, data science and machine learning.
Follow my progress at
https://www.linkedin.com/in/matis-messence/
https://github.com/MessenceM
"""

import pygame
import random

# setup
w = 480
h = 360
length = 0
square_side = 15

# display initialization
running = True
pygame.init()
screen = pygame.display.set_mode((w, h))
pygame.display.set_caption('Snake')
clock = pygame.time.Clock()


class Snake:

    def __init__(self):
        self.x = w / 2
        self.y = h / 2
        self.pos = [self.x, self.y]
        self.length = length
        self.head = pygame.Rect(self.x, self.y, square_side-1, square_side-1)
        self.color = 'white'
        self.direction = 'stopped'
        self.tail = []

    def draw(self):
        pygame.draw.rect(screen, self.color, self.head)
        for i in range(self.length):
            pygame.draw.rect(screen, self.color, pygame.Rect(self.tail[i][0], self.tail[i][1], square_side-1, square_side-1))

    def move(self, pressed):
        self.pos = [self.x, self.y]
        self.tail.insert(0, self.pos)
        del self.tail[-1]

        # only allow perpendicular directions
        if pressed[pygame.K_LEFT] and self.direction != "right":
            self.direction = "left"
        elif pressed[pygame.K_RIGHT] and self.direction != "left":
            self.direction = "right"
        elif pressed[pygame.K_UP] and self.direction != "down":
            self.direction = "up"
        elif pressed[pygame.K_DOWN] and self.direction != "up":
            self.direction = "down"

        # move in the current direction
        # static = 0 left = 1 right = 2 up = 4 down = 5
        if self.direction == "left":
            self.x -= square_side
        elif self.direction == "right":
            self.x += square_side
        elif self.direction == "up":
            self.y -= square_side
        elif self.direction == "down":
            self.y += square_side

        self.x %= w
        self.y %= h
        self.head = pygame.Rect(self.x, self.y, square_side, square_side)

    def eat(self):
        if self.head.colliderect(food.berry):
            self.length += 1
            self.tail.append([self.x, self.y])
            food.__init__()

    def collision(self):
        global running
        for i in range(self.length):
            if [self.x, self.y] == self.tail[i]:
                running = False


class Food:
    def __init__(self):
        self.x = random.randint(1, w / square_side - 1) * square_side
        self.y = random.randint(1, h / square_side - 1) * square_side
        self.berry = pygame.Rect(self.x, self.y, square_side, square_side)
        self.color = "red"

    def draw(self):
        pygame.draw.rect(screen, self.color, self.berry)


snake = Snake()
food = Food()
pressed = pygame.key.get_pressed()

while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

        if event.type == pygame.KEYDOWN:
            pressed = pygame.key.get_pressed()
    screen.fill("black")
    snake.move(pressed)
    snake.collision()
    snake.eat()
    snake.draw()
    food.draw()
    pygame.display.flip()
    clock.tick(10)
pygame.quit()
