from random import randint

WIDTH = 800
HEIGHT = 800
score = 0
game_over = False

shark = Actor("garchomp")
shark.pos = 100, 100

coin = Actor("coin")
coin.pos = 200, 200

def draw():
    screen.fill("teal")
    shark.draw()
    coin.draw()
    screen.draw.text("Score: " + str(score), color="azure", topleft=(10,10))
    
    if game_over:
        screen.fill("crimson")
        screen.draw.text("Final Score: " + str(score), topleft=(10,10), fontsize=60)
    
def place_coin():
    coin.x = randint(20, (WIDTH - 20))
    coin.y = randint(20, (HEIGHT - 20))
    
def time_up():
    global game_over
    game_over = True
    
def update():
    global score
    speed = 5
    if keyboard.left:
        shark.x = shark.x - speed
    elif keyboard.right:
        shark.x = shark.x + speed
    elif keyboard.up:
        shark.y = shark.y - speed
    elif keyboard.down:
        shark.y = shark.y + speed
        
    coin_collected = shark.colliderect(coin)
    
    if coin_collected:
        score = score + 10
        sounds.coincollect.play()
        place_coin()
        
clock.schedule(time_up, 20.0)
place_coin()
    