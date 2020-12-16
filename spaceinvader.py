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
YELLOW_LAZER = pygame.image.load(os.path.join("assets", "pixel_laser_yellow.png"))

#imports for the background image
BACKGROUND = pygame.transform.scale(pygame.image.load(os.path.join("assets", "background-black.png")), (WIDTH, HEIGHT))

#class for a ship object
class Ship:
    def __init__(self, x, y, health = 100):
        self.x = x
        self.y = y
        self.health = health
        self.shipImage = None
        self.laserImage = None
        self.lasers = []
        self.coolDownCounter = 0

    #Draws the ship to the screen
    def draw(self, window):
        window.blit(self.shipImage, (self.x, self.y))

    def get_width(self):
        return self.shipImage.get_width()

    def get_height(self):
        return self.shipImage.get_height()

class Player(Ship):
    def __init__(self, x, y, health = 100):
        super().__init__(x, y, health)
        self.shipImage = YELLOW_SPACE_SHIP
        self.laserImage = YELLOW_LAZER
        self.mask = pygame.mask.from_surface(self.shipImage)
        self.maxHealth = health

class enemyShip(Ship):
    COLOUR_MAP = {
        "red" : (RED_SPACE_SHIP, RED_LAZER),
        "blue" : (BLUE_SPACE_SHIP, BLUE_LAZER),
        "green" : (GREEN_SPACE_SHIP, GREEN_LAZER)
    }
    def __init__(self, x, y, colour, health = 100):
        super().__init__(x, y, health)
        self.shipImage, self.laserImage = self.COLOUR_MAP[colour]
        self.mask = pygame.mask.from_surface(self.shipImage)

    def move(self, vel) :
        self.y += vel
def main():
    run = True
    FPS = 60
    level = 1
    lives = 5
    playerVelocity = 5
    mainFont = pygame.font.SysFont("comicsans", 50)
    clock = pygame.time.Clock()

    player = Player(300, 650)

    def redrawWindow():
        WINDOW.blit(BACKGROUND, (0,0))
        #draw lives and level labels to the screen
        livesLabel = mainFont.render(f"lives: {lives}", 1, (255, 255, 255))
        levelLabel = mainFont.render(f"level: {level}", 1, (255, 255, 255))
        WINDOW.blit(livesLabel, (10, 10))
        WINDOW.blit(levelLabel, (WIDTH - levelLabel.get_width() - 10, 10))

        player.draw(WINDOW)
        pygame.display.update()
    while run:
        clock.tick(FPS)
        redrawWindow()
        #check for closed window
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                run = False

        #Player movement control
        keys = pygame.key.get_pressed()
        if keys[pygame.K_a] and player.x - playerVelocity > 0: #left
            player.x -= playerVelocity
        if keys[pygame.K_d] and player.x + playerVelocity + player.get_width() < WIDTH: #Right
            player.x += playerVelocity
        if keys[pygame.K_s] and player.y + playerVelocity + player.get_height() < HEIGHT: #Down
            player.y += playerVelocity
        if keys[pygame.K_w] and player.y - playerVelocity > 0:  #Up
            player.y -= playerVelocity
main()
