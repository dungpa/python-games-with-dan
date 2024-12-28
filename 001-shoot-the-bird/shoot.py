from random import randint
import time

zapdos = Actor("zapdos")
message = "Click the bird!"
WIDTH = 1000
HEIGHT = 800
score = 0

def draw():
    screen.clear()
    x = randint (10, 50)
    y = randint (10, 50)
    screen.draw.text(message, topleft=(x, y))
    screen.draw.text("Score: " + str(score), topleft=(5, 5))
    zapdos.draw()    
    
def place_zapdos():
    zapdos.x = randint(10, (WIDTH - 10))
    zapdos.y = randint(10, (HEIGHT - 10))

def reset_zapdos_image():
    zapdos.image = "zapdos"

def on_mouse_down(pos):
    global message  # Declare `message` as global
    global score
    if zapdos.collidepoint(pos):
        message = "Good shot!"
        score = score + 1
        sounds.squawk.play()
        zapdos.image = "zapdoscream"
        clock.schedule(reset_zapdos_image, 0.5)  # Reset image after 0.5 seconds
        place_zapdos()
    else:
        message = "Sorry, player, but you missed!"
        clock.schedule(quit, 2)  # Schedule the quit after 2 seconds

place_zapdos()
