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

def main():
    run = True
    FPS = 60
    level = 1
    lives = 5
    mainFont = pygame.font.SysFont("comicsans", 50)
    clock = pygame.time.Clock()

    def redrawWindow():
        WINDOW.blit(BACKGROUND, (0,0))
        #draw lives and level labels to the screen
        livesLabel = mainFont.render(f"lives: {lives}", 1, (255, 255, 255))
        levelLabel = mainFont.render(f"level: {level}", 1, (255, 255, 255))
        WINDOW.blit(livesLabel, (10, 10))
        WINDOW.blit(levelLabel, (WIDTH - levelLabel.get_width() - 10, 10))
        pygame.display.update()
    while run:
        clock.tick(FPS)
        redrawWindow()
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                run = False

main()
