import pygame
import os
import time
import random
pygame.font.init()

WIDTH = 750
HEIGHT = 750
WINDOW = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Space Invader Shooty Thing")

#imports for the ship images
RED_SPACE_SHIP = pygame.image.load(os.path.join("assets", "pixel_ship_red_small.png"))
GREEN_SPACE_SHIP = pygame.image.load(os.path.join("assets", "pixel_ship_green_small.png"))
BLUE_SPACE_SHIP = pygame.image.load(os.path.join("assets", "pixel_ship_blue_small.png"))
YELLOW_SPACE_SHIP = pygame.image.load(os.path.join("assets", "pixel_ship_yellow.png"))

#imports for the lazer images
RED_LAZER = pygame.image.load(os.path.join("assets", "pixel_laser_red.png"))
GREEN_LAZER = pygame.image.load(os.path.join("assets", "pixel_laser_green.png"))
BLUE_LAZER = pygame.image.load(os.path.join("assets", "pixel_laser_blue.png"))
RED_LAZER = pygame.image.load(os.path.join("assets", "pixel_laser_yellow.png"))

#imports for the background image
BACKGROUND = pygame.transform.scale(pygame.image.load(os.path.join("assets", "background-black.png")), (WIDTH, HEIGHT))

class Ship:
    def __init__(self, x, y, health = 100):
        self.x = x
        self.y = y
        self.health = health
        self.shipImage = None
        self.laserImage = None
        self.lasers = []
        self.coolDownCounter = 0

    def draw(self, window):
        pygame.draw.rect(window, (255, 0, 0), (self.x, self.y, 50, 50))


def main():
    run = True
    FPS = 60
    level = 1
    lives = 5
    playerVelocity = 5
    mainFont = pygame.font.SysFont("comicsans", 50)
    clock = pygame.time.Clock()

    ship = Ship(300, 650)

    def redrawWindow():
        WINDOW.blit(BACKGROUND, (0,0))
        #draw lives and level labels to the screen
        livesLabel = mainFont.render(f"lives: {lives}", 1, (255, 255, 255))
        levelLabel = mainFont.render(f"level: {level}", 1, (255, 255, 255))
        WINDOW.blit(livesLabel, (10, 10))
        WINDOW.blit(levelLabel, (WIDTH - levelLabel.get_width() - 10, 10))

        ship.draw(WINDOW)
        pygame.display.update()
    while run:
        clock.tick(FPS)
        redrawWindow()
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                run = False

        keys = pygame.key.get_pressed()
        if keys[pygame.K_a]: #left
            ship.x -= playerVelocity
        if keys[pygame.K_d]: #Right
            ship.x += playerVelocity
        if keys[pygame.K_s]: #Down
            ship.y += playerVelocity
        if keys[pygame.K_w]:  #Up
            ship.y -= playerVelocity
main()
