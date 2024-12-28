from random import randint

WIDTH = 800
HEIGHT = 600

dragon = Actor("wingedtoad")
dragon.pos = 400, 300

bird = Actor("articunoup")
bird.pos = randint(800, 1600), randint(10, 200)

house = Actor("house")
house.pos = randint(800, 1600), 460

tree = Actor("tree")
tree.pos = randint(800, 1600), 450

bird_up = True
up = False
game_over = False
score = 0
number_of_updates = 0

scores = []
game_theme = sounds.dragonflying
game_theme.play(loops=-1)

def update_high_scores():
    global score, scores
    filename = r"C:\Repos\python-games-with-dan\006-dragon-flight\high-scores.txt"
    scores = []
    with open(filename, "r") as file:
        line = file.readline()
        high_scores = line.split()
        for high_score in high_scores:
            if(score > int(high_score)):
                scores.append(str(score) + " ")
                score = int(high_score)
            else:
                scores.append(str(high_score) + " ")
      
    with open(filename, "w") as file:      
        for high_score in scores:
            file.write(high_score)
    
def display_high_scores():
    screen.draw.text("HIGH SCORES", (350, 150), color="black")
    y = 175
    position = 1
    for high_score in scores:
        screen.draw.text(str(position) + ". " + high_score, (350, y), color="black")
        y += 25
        position += 1
    
def draw():
    screen.blit("background", (0, 0))
    if not game_over:
        dragon.draw()
        bird.draw()
        house.draw()
        tree.draw()
        screen.draw.text("Score: " + str(score), (700, 5), color="black")
    else:
        display_high_scores()
        
def on_mouse_down():
    global up
    up = True
    dragon.y -= 50
    
def on_mouse_up():
    global up
    up = False
    
def flap():
    global bird_up
    if bird_up:
        bird.image = "articunodown"
        bird_up = False
    else:
        bird.image = "articunoup"
        bird_up = True
        
def update():
    global game_over, score, number_of_updates
    if not game_over:
        if not up:
            dragon.y += 1
            
        if bird.x > 0:
            bird.x -= 4
            if number_of_updates == 9:
                flap()
                number_of_updates = 0
            else:
                number_of_updates += 1
                
        else:
            bird.x = randint(800, 1600)
            bird.y = randint(10, 200)
            score += 1
            number_of_updates = 0
            
        if house.right > 0:
            house.x -= 2
        else:
            house.x = randint(800, 1600)
            score += 1 
            
        if tree.right > 0:
            tree.x -= 2
        else:
            tree.x = randint(800, 1600)
            score += 1 
            
        if dragon.top < 0 or dragon.bottom > 560:
            game_over = True
            update_high_scores()
            
        if dragon.collidepoint(bird.pos) or dragon.collidepoint(house.pos) or dragon.collidepoint(tree.pos):
            game_over = True
            update_high_scores()
       