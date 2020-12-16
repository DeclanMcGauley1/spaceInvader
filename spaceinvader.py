import pygame
import os
import time
import random

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
BACKGROUND = pygame.image.load(os.path.join("assets", "background-black.png"))
