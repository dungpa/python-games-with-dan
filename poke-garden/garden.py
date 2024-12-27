from random import randint
import time

WIDTH = 800
HEIGHT = 600
CENTRE_X = WIDTH / 2
CENTRE_Y = HEIGHT / 2

game_over = False
finalised = False
garden_happy = True
fangflower_collision = False

time_elapsed = 0
start_time = time.time()

aggron = Actor("letitgron")
aggron.pos = 100, 500

flower_list = []
wilted_list = []
fangflower_list = []

fangflower_vy_list = []
fangflower_vx_list = []

def draw():
    global game_over, time_elapsed, finalised
    if not game_over:
        screen.clear()
        screen.blit("garden", (0, 0))
        aggron.draw()
        for flower in flower_list:
            flower.draw()
        for fangflower in fangflower_list:
            fangflower.draw()
        time_elapsed = int(time.time() - start_time)
        screen.draw.text("Garden happy for: " + str(time_elapsed) + " seconds", topleft=(10, 10), color="black")
    else:
        if not finalised:
            aggron.draw()
            screen.draw.text("Garden happy for: " + str(time_elapsed) + " seconds", topleft=(10, 10), color="black")
            if not garden_happy:
                screen.draw.text("GARDEN UNHAPPY - GAME OVER!", color="black", topleft=(10, 50))
                finalised = True
            else:
                screen.draw.text("FANGFLOWER ATTACK - GAME OVER!", color="black", topleft=(10, 50))
                finalised = True
                
def new_flower():
    global flower_list, wilted_list
    flower_new = Actor("flower")
    flower_new.pos = randint(50, WIDTH - 50), randint(150, HEIGHT - 100)
    flower_list.append(flower_new)
    wilted_list.append("happy")
    return
    
def add_flowers():
    global game_over
    if not game_over:
        new_flower()
        clock.schedule(add_flowers, 4)
    return
    
def check_wilt_times():
    global wilted_list, game_over, garden_happy
    if wilted_list:
        for wilted_since in wilted_list:
            if (not wilted_since == "happy"):
                time_wilted = int(time.time() - wilted_since)
                if (time_wilted) > 10.0:
                    garden_happy = False
                    game_over = True
                    break
    return
    
def wilt_flower():
    global flower_list, wilted_list, game_over
    if not game_over:
        if flower_list:
            rand_flower = randint(0, len(flower_list) - 1)
            if (flower_list[rand_flower].image == "flower"):
                flower_list[rand_flower].image = "flower-wilt"
                wilted_list[rand_flower] = time.time()
        clock.schedule(wilt_flower, 3)
    return
    
def check_flower_collision():
    global aggron, flower_list, wilted_list
    index = 0
    for flower in flower_list:
        if (flower.colliderect(aggron) and flower.image == "flower-wilt"):
            flower.image = "flower"
            wilted_list[index] = "happy"
            break
        index = index + 1
    return
    
def check_fangflower_collision():
    global cow, fangflower_list, fangflower_collision
    global game_over
    for fangflower in fangflower_list:
        if fangflower.colliderect(aggron):
            aggron.image = "zap"
            game_over = True
            break
    return
        
    
    
def velocity():
    random_dir = randint(0, 1)
    random_velocity = randint(2, 3)
    if random_dir == 0:
        return -random_velocity
    else:
        return random_velocity
    
def mutate():
    global flower_list, fangflower_list, fangflower_vy_list
    global fangflower_vx_list, game_over
    if not game_over and flower_list:
        rand_flower = randint(0, len(flower_list) - 1)
        fangflower = Actor("flowey")
        fangflower.pos = flower_list[rand_flower].x, flower_list[rand_flower].y
        del flower_list[rand_flower]
        fangflower_vx = velocity()
        fangflower_vy = velocity()
        fangflower = fangflower_list.append(fangflower)
        fangflower_vx_list.append(fangflower_vx)
        fangflower_vy_list.append(fangflower_vy)
        clock.schedule(mutate, 20)
    return
    
def update_fangflowers():
    global fangflower_list, game_over
    if not game_over:
        index = 0
        for fangflower in fangflower_list:
            fangflower_vx = fangflower_vx_list[index]
            fangflower_vy = fangflower_vy_list[index]
            fangflower.x = fangflower.x + fangflower_vx
            fangflower.y = fangflower.y + fangflower_vy
            if fangflower.left < 0:
                fangflower_vx_list[index] = -fangflower_vx
            if fangflower.right > WIDTH:
                fangflower_vx_list[index] = -fangflower_vx
            if fangflower.top < 150:
                fangflower_vy_list[index] = -fangflower_vy
            if fangflower.bottom > HEIGHT:
                fangflower_vy_list[index] = -fangflower_vy
            index = index + 1
    return
    
def reset_aggron():
    global game_over
    if not game_over:
        aggron.image = "letitgron"
    return
    
def update():
    global score, game_over, fangflower_collision
    global flower_list, fangflower_list, time_elapsed
    fangflower_collision = check_fangflower_collision()
    check_wilt_times()
    if not game_over:
        if keyboard.space:
            aggron.image = "aggrongrow"
            clock.schedule(reset_aggron, 0.5)
            check_flower_collision()
        if keyboard.left and aggron.x > 0:
            aggron.x -= 5
        elif keyboard.right and aggron.x < WIDTH:
            aggron.x += 5
        elif keyboard.up and aggron.y > 150:
            aggron.y -= 5     
        elif keyboard.down and aggron.y < HEIGHT:
            aggron.y += 5  
        if time_elapsed > 15 and not fangflower_list:
            mutate()
        update_fangflowers()
            
add_flowers()
wilt_flower()