from random import randint

WIDTH = 750
HEIGHT = 750

digletts = []
lines = []

next_diglett = 0
game_won = False
game_over = False

diglett_count = randint(6, 12)

for diglett in range(0, diglett_count):
    actor = Actor("diglett")
    actor.pos = randint(20, WIDTH - 20), randint(20, HEIGHT - 20)
    digletts.append(actor)
    
def draw():
    if game_won:
        screen.fill("light sea green")
        screen.draw.text("Congratulations, player because You Won!", color="light cyan", topleft=(90, 90), fontsize=45)
    elif game_over:
        screen.fill("crimson")
        screen.draw.text("Time's up, so try again!", color="pink", topleft=(90,90), fontsize=45)
    else:
        screen.fill("khaki")
        number = 1
        for diglett in digletts:
            screen.draw.text(str(number), (diglett.pos[0], diglett.pos[1] + 18))
            diglett.draw()
            number = number + 1
        for line in lines:
            screen.draw.line(line[0], line[1], (70, 130, 180))
        
def on_mouse_down(pos):
    global next_diglett
    global lines
    global game_won
    global diglett_count
    
    if game_won:
        return

    if digletts[next_diglett].collidepoint(pos):
        if next_diglett:
            lines.append((digletts[next_diglett - 1].pos, digletts[next_diglett].pos))
        next_diglett = next_diglett + 1
        
        if next_diglett == diglett_count:
            game_won = True
        
    else:
        lines = []
        next_diglett = 0
        
def time_up():
    global game_over
    game_over = True
       
clock.schedule(time_up, 30.0)
        