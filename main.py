import pygame
import random
from pygame import mixer

# classes
class Fly(pygame.sprite.Sprite):
    def __init__(self, speed, img):
        super().__init__()
        self.image = img
        self.rect = self.image.get_rect()
        self.rect.x = width // 2 - self.rect.width // 2
        self.rect.y = height // 2 - self.rect.height // 2
        self.speed = [speed, speed]

    def move(self):
        self.rect.x += self.speed[0]
        self.rect.y += self.speed[1]
        if self.rect.left < 0 or self.rect.right > width:
            self.speed[0] = -self.speed[0]
        if self.rect.top < 0 or self.rect.bottom > height:
            self.speed[1] = -self.speed[1]



# Initializing Pygame
pygame.init()
width, height = 800, 600
screen = pygame.display.set_mode((width, height), pygame.RESIZABLE)
pygame.display.set_caption("Catch the Fly!")
icon = pygame.image.load('assets/fly.png')
pygame.display.set_icon(icon)
clock = pygame.time.Clock()
background = pygame.transform.scale(pygame.image.load('assets/bedroom.jpg'), (width, height))
frame_rate = 90
speed = 2
fly_img = pygame.transform.scale(pygame.image.load('assets/fly.png'), (50, 50))
fly = Fly(speed, fly_img)
flies = pygame.sprite.Group()
flies.add(fly)
number_of_flies = 1
font = pygame.font.Font('freesansbold.ttf', 32)

# main loop
running = True
points = 0
while running:

    # background
    screen.blit(background, (0, 0))

    # event handling 
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        if event.type == pygame.MOUSEBUTTONDOWN:
            for fly in flies:
                if fly.rect.collidepoint(event.pos):
                    points += 1
                    # if the points are multiples of 10, then deleting the old fly and adding two new flies
                    if points % 10 == 0:
                        flies.remove(fly)
                        number_of_flies += 1
                        for i in range(number_of_flies):
                            fly = Fly(speed, fly_img)
                            flies.add(fly)

    # moving the flies
    for fly in flies:
        fly.move()

    # drawing the flies
    flies.draw(screen)

    # drawing the points
    text = font.render(f'Points: {points}', True, (255, 255, 255))
    screen.blit(text, (width/2 - text.get_width() // 2, 10))

    clock.tick(frame_rate)
    pygame.display.update()