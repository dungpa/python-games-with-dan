from random import randint
import time

zapdos = Actor("zapdos")
message = "Click the bird!"

def draw():
    screen.clear()
    x = randint (10, 50)
    y = randint (10, 50)
    screen.draw.text(message, topleft=(x, y))
    zapdos.draw()
    
    
def place_zapdos():
    zapdos.x = randint(10, 800)
    zapdos.y = randint(10, 600)

def reset_zapdos_image():
    zapdos.image = "zapdos"

def on_mouse_down(pos):
    global message  # Declare `message` as global
    if zapdos.collidepoint(pos):
        message = "Good shot!"
        sounds.squawk.play()
        zapdos.image = "zapdoscream"
        clock.schedule(reset_zapdos_image, 0.5)  # Reset image after 0.5 seconds
        place_zapdos()
    else:
        message = "Sorry, player, but you missed!"
        clock.schedule(quit, 2)  # Schedule the quit after 2 seconds

place_zapdos()