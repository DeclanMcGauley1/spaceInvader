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
    COOLDOWN = 30
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
        for laser in self.lasers:
            laser.draw(window)

    def moveLasers(self, vel, obj):
        self.cooldown()
        for laser in self.lasers:
            laser.move(vel)
            if laser.offScreen(HEIGHT):
                self.lasers.remove(laser)
            elif laser.collision(obj):
                obj.health -= 10
                self.lasers.remove(laser)


    def get_width(self):
        return self.shipImage.get_width()

    def get_height(self):
        return self.shipImage.get_height()

    def cooldown(self):
        if self.coolDownCounter >= self.COOLDOWN:
            self.coolDownCounter = 0
        if self.coolDownCounter > 0:
            self.coolDownCounter += 1

    def shoot(self):
        if self.coolDownCounter == 0:
            laser = Laser(self.x, self.y, self.laserImage)
            self.lasers.append(laser)
            self.coolDownCounter = 1

class Player(Ship):
    def __init__(self, x, y, health = 100):
        super().__init__(x, y, health)
        self.shipImage = YELLOW_SPACE_SHIP
        self.laserImage = YELLOW_LAZER
        self.mask = pygame.mask.from_surface(self.shipImage)
        self.maxHealth = health

    def moveLasers(self, vel, objs):
        self.cooldown()
        for laser in self.lasers:
            laser.move(vel)
            if laser.offScreen(HEIGHT):
                self.lasers.remove(laser)
            else:
                for obj in objs:
                    if laser.collision(obj):
                        objs.remove(obj)
                        self.lasers.remove(laser)

    def draw(self, window):
        super().draw(window)
        self.healthbar(window)

    def healthbar(self, window):
        pygame.draw.rect(window, (255, 0, 0), (self.x, self.y + self.shipImage.get_height() + 10, self.shipImage.get_width(), 10))
        pygame.draw.rect(window, (0, 255, 0), (self.x, self.y + self.shipImage.get_height() + 10, self.shipImage.get_width() * (self.health / self.maxHealth), 10))

class Enemy(Ship):
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

    def shoot(self):
        if self.coolDownCounter == 0:
            laser = Laser(self.x - 15, self.y, self.laserImage)
            self.lasers.append(laser)
            self.coolDownCounter = 1

class Laser:
    def __init__(self, x, y, img):
        self.x = x
        self.y = y
        self.img = img
        self.mask = pygame.mask.from_surface(self.img)

    def draw(self, window):
        window.blit(self.img, (self.x, self.y))

    def move(self, vel):
        self.y += vel

    def offScreen(self, height):
        return not (self.y <= height and self.y >= 0)

    def collision(self, obj):
        return collide(obj, self)

def collide(obj1, obj2):
    offsetX = obj2.x - obj1.x
    offsetY = obj2.y - obj1.y
    return obj1.mask.overlap(obj2.mask, (offsetX, offsetY)) != None

def main():
    run = True
    FPS = 60
    level = 0
    lives = 5
    playerVelocity = 5
    mainFont = pygame.font.SysFont("comicsans", 50)
    lostFont = pygame.font.SysFont("comicsans", 60)
    clock = pygame.time.Clock()
    lost = False
    lostCount = 0

    enemies = []
    waveLength = 5
    enemyVelocity = 1
    laserVelocity = 4

    player = Player(300, 630)

    def redrawWindow():
        WINDOW.blit(BACKGROUND, (0,0))
        #draw lives and level labels to the screen
        livesLabel = mainFont.render(f"lives: {lives}", 1, (255, 255, 255))
        levelLabel = mainFont.render(f"level: {level}", 1, (255, 255, 255))
        WINDOW.blit(livesLabel, (10, 10))
        WINDOW.blit(levelLabel, (WIDTH - levelLabel.get_width() - 10, 10))

        for enemy in enemies:
            enemy.draw(WINDOW)

        player.draw(WINDOW)

        if lost:
            lostLabel = lostFont.render("You lost!", 1, (255,255,255))
            WINDOW.blit(lostLabel, (WIDTH / 2 - levelLabel.get_width() / 2, 350))

        pygame.display.update()

    while run:
        clock.tick(FPS)
        redrawWindow()
        if lives <= 0 or player.health <= 0:
            lost = True
            lostCount += 1

        if lost:
            if lostCount > FPS * 3:
                run = False
            else:
                continue


        if len(enemies) == 0:
            level += 1
            waveLength += 5
            for i in range(waveLength):
                enemy = Enemy(random.randrange(100, WIDTH - 100), random.randrange(-1500, -100), random.choice(["red", "blue", "green"]))
                enemies.append(enemy)

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
        if keys[pygame.K_s] and player.y + playerVelocity + player.get_height() + 10 < HEIGHT: #Down
            player.y += playerVelocity
        if keys[pygame.K_w] and player.y - playerVelocity > 0:  #Up
            player.y -= playerVelocity
        if keys[pygame.K_SPACE]:
            player.shoot()

        for enemy in enemies[:]:
            enemy.move(enemyVelocity)
            enemy.moveLasers(laserVelocity, player)

            if random.randrange(0, 4*60) == 1:
                enemy.shoot()

            if collide(enemy, player):
                player.health -= 10
                enemies.remove(enemy)
            elif enemy.y + enemy.get_height() > HEIGHT:
                lives -= 1
                enemies.remove(enemy)

        player.moveLasers(-laserVelocity, enemies)
main()
