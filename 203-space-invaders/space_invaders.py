import pygame, sys, random, time
from pygame.locals import *
pygame.init()
clock = pygame.time.Clock()
pygame.display.set_caption("Space Invaders")
screen = pygame.display.set_mode((640, 650))

badguy_image = pygame.image.load("badguy.png").convert()
badguy_image.set_colorkey((0, 0, 0))
fighter_image = pygame.image.load("fighter.png").convert()
fighter_image.set_colorkey((255, 255, 255))
missile_image = pygame.image.load("missile.png").convert()
missile_image.set_colorkey((255, 255, 255))

last_badguy_spawn_time = 0


class Badguy:
    def __init__(self):
        self.x = random.randint(0, 570)
        self.y = -100
        self.dy = random.randint(2, 6)
        self.dx = random.choice((-1, 1))*self.dy
        
    def move(self):
        if self.x < 0 or self.x > 570:
            self.dx *= -1
        self.x += self.dx
        self.y += self.dy
        
    def draw(self):
        screen.blit(badguy_image, (self.x, self.y))
    
    def bounce(self):
        if self.x < 0 or self.x > 570:
            self.dx *= -1
            
    def off_screen(self):
        return self.y > 640

class Fighter:
    def __init__(self):
        self.x = 320

    def move(self):
        if pressed_keys[K_LEFT] and self.x > 0:
            self.x -= 3
        if pressed_keys[K_RIGHT] and self.x < 540:
            self.x += 3

    def draw(self):
        screen.blit(fighter_image, (self.x, 591))

    def fire(self):
        missiles.append(Missile(self.x + 50))

class Missile:
    def __init__(self,x):
        self.x = x
        self.y = 591

    def move(self):
        self.y -= 5

    def off_screen(self):
        return self.y < -8

    def draw(self):
        screen.blit(missile_image, (self.x - 4, self.y))



badguy = Badguy()
badguys = []
fighter = Fighter()
missiles = []

while True:
    clock.tick(60)
    for event in pygame.event.get():
        if event.type == QUIT:
            sys.exit()
        if event.type == KEYDOWN and event.key == K_SPACE:
            fighter.fire()
    pressed_keys = pygame.key.get_pressed()
    if time.time() - last_badguy_spawn_time > 0.5:
        badguys.append(Badguy())
        last_badguy_spawn_time = time.time()
    
            
    screen.fill((0, 0, 0))
    
    badguy.move()
    badguy.bounce()
    badguy.draw()

    fighter.move()
    fighter.draw()
    
    i = 0
    while i < len(badguys):
        badguys[i].move()
        badguys[i].bounce()
        badguys[i].draw()
        if badguys[i].off_screen():
            del badguys[i]
            i -= 1
        i += 1

    i = 0
    while i < len(missiles):
        missiles[i].move()
        missiles[i].draw()
        if missiles[i].off_screen():
            del missiles[i]
            i -= 1
        i += 1
    
    pygame.display.update()