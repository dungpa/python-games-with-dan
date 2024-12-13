from random import randint
import time

zapdos = Actor("zapdos")
message = "Click the bird!"

def draw():
    screen.clear()
    screen.draw.text(message, topleft=(25,25))
    zapdos.draw()
    
def place_zapdos():
    zapdos.x = randint(10, 800)
    zapdos.y = randint(10, 600)

def on_mouse_down(pos):
    global message  # Declare `message` as global
    if zapdos.collidepoint(pos):
        message = "Good shot!"
        sounds.squawk.play() 
        place_zapdos()
    else:
        message = "Sorry, player, but you missed!"
        clock.schedule(quit_game, 2)  # Schedule the quit after 2 seconds

def quit_game():
    quit()

place_zapdos()
