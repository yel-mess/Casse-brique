from random import randint

WIDTH = 800 # x
HEIGHT = 600 # y
life = 15 #nombre de vie
loose = False
power_up_apparition = 10 #pourcent de chance des powerup
projectile_apparition = 2 #chance des projectile
time_big_player = 0 #pendant cmb de tps le powerup va durer
time_kill_ennemies = 0 #durée du powerup étoile
win = False

background = Actor("brick_wall") #background

ball = Actor("neon_ball") #balle
ball.pos = [400, 500]
ball_speed = [3, -3] #vitesse de la balle

ennemy_speed = [2, 0]

gameover = Actor("gameover") #gameover

player = Actor("neon_player2") #plateforme
player.pos = [400, 550]

power_up_speed = [0, 3] #vitesse des powerup
projectile_speed = [0, 4] #vitesse des projectiles

victory = Actor("victory") #victoire

all_bricks = [] #liste des briques
all_super_bricks = [] #liste des super briques
all_transparent_bricks = []
all_power_up_big_player = [] #liste des powerup big player
all_power_up_slower = [] #liste des sabliers
all_power_up_kill_ennemy = [] #liste des étoiles
all_ennemies = [] #liste des ennemis
all_projectiles = [] #liste des projectiles
all_heart = [] #liste des coeur

for x in range(0, 800, 50): # placer les briques dans les liste et à la bonne position
    for y in range(0, 50, 50):
        brick = Actor("neon_yellow_50", anchor=["left", "top"])
        brick.pos = [x, y]
        all_bricks.append(brick)
    for y in range(50, 100, 50):
        brick = Actor("neon_green_50", anchor=["left", "top"])
        brick.pos = [x, y]
        all_bricks.append(brick)
    for y in range(200, 250, 50):
        brick = Actor("neon_blue_50", anchor=["left", "top"])
        brick.pos = [x, y]
        all_bricks.append(brick)
    for y in range(250, 300, 50):
        brick = Actor("neon_violet_50", anchor=["left", "top"])
        brick.pos = [x, y]
        all_bricks.append(brick)
for x in range(50, 750, 200): #super briques
    super_brick = Actor("neon_aqua_100", anchor=["left", "top"])
    super_brick.pos = [x, 125]
    all_super_bricks.append(super_brick)
for x in range(50, 750, 200):
    transparent_brick = Actor("transparent_brick", anchor=["left", "top"])
    transparent_brick.pos = [x, 125]
    all_transparent_bricks.append(transparent_brick)
for x in range(190, 600, 200): #ennemis
    ennemy = Actor("ennemy", anchor=["left", "center"])
    ennemy.pos = [x, 150]
    all_ennemies.append(ennemy)
for x in range(280, 530, 17):
    heart = Actor("heart", anchor=["left", "center"])
    heart.pos = [x, 582]
    all_heart.append(heart)

#music.play("approaching_eve2") #musique créée avec BeepBox
#music.play("fire_inside") #music sample
#music.set_volume(0.4) #volume de la musique

def reboot():
    global all_bricks
    global all_ennemies
    global all_heart
    global all_power_up_big_player
    global all_power_up_kill_ennemy
    global all_power_up_slower
    global all_projectiles
    global all_super_bricks
    global all_transparent_bricks
    global ball
    global ball_speed
    global ennemy_speed
    global life
    global loose
    global player
    global power_up_apparition
    global projectile_apparition
    global time_big_player
    global time_kill_ennemies
    global win

    power_up_apparition = 10 #pourcent de chance des powerup
    projectile_apparition = 2 #chance des projectile
    time_big_player = 0 #pendant cmb de tps le powerup va durer
    time_kill_ennemies = 0 #durée du powerup étoile
    life = 15 #nombre de vie
    loose = False
    win = False

    background = Actor("brick_wall") #background
    ball = Actor("neon_ball") #balle
    ball.pos = [400, 500]
    ball_speed = [3, -3] #vitesse de la balle

    ennemy_speed = [2, 0]

    gameover = Actor("gameover") #gameover
    victory = Actor("victory") #victoire

    player = Actor("neon_player2") #plateforme
    player.pos = [400, 550]

    projectile_speed = [0, 4] #vitesse des projectiles
    power_up_speed = [0, 3] #vitesse des powerup

    all_bricks = [] #liste des briques
    all_super_bricks = [] #liste des super briques
    all_transparent_bricks = []
    all_power_up_big_player = [] #liste des powerup big player
    all_power_up_slower = [] #liste des sabliers
    all_power_up_kill_ennemy = [] #liste des étoiles
    all_ennemies = [] #liste des ennemis
    all_projectiles = [] #liste des projectiles
    all_heart = [] #liste des coeur

    for x in range(0, 800, 50): # placer les briques dans les liste et à la bonne position
        for y in range(0, 50, 50):
            brick = Actor("neon_yellow_50", anchor=["left", "top"])
            brick.pos = [x, y]
            all_bricks.append(brick)
        for y in range(50, 100, 50):
            brick = Actor("neon_green_50", anchor=["left", "top"])
            brick.pos = [x, y]
            all_bricks.append(brick)
        for y in range(200, 250, 50):
            brick = Actor("neon_blue_50", anchor=["left", "top"])
            brick.pos = [x, y]
            all_bricks.append(brick)
        for y in range(250, 300, 50):
            brick = Actor("neon_violet_50", anchor=["left", "top"])
            brick.pos = [x, y]
            all_bricks.append(brick)
    for x in range(50, 750, 200): #super briques
        super_brick = Actor("neon_aqua_100", anchor=["left", "top"])
        super_brick.pos = [x, 125]
        all_super_bricks.append(super_brick)
    for x in range(50, 750, 200):
        transparent_brick = Actor("transparent_brick", anchor=["left", "top"])
        transparent_brick.pos = [x, 125]
        all_transparent_bricks.append(transparent_brick)
    for x in range(190, 600, 200): #ennemis
        ennemy = Actor("ennemy", anchor=["left", "center"])
        ennemy.pos = [x, 150]
        all_ennemies.append(ennemy)
    for x in range(280, 530, 17):
        heart = Actor("heart", anchor=["left", "center"])
        heart.pos = [x, 582]
        all_heart.append(heart)
    
    #music.play("approaching_eve2") #musique créée avec BeepBox
    #music.play("fire_inside") #music sample
    #music.set_volume(0.4) #volume de la musique

def draw():
    screen.clear()
    for transparent_brick in all_transparent_bricks:
        transparent_brick.draw()
    background.draw()

    for brick in all_bricks:
        brick.draw()
    for super_brick in all_super_bricks:
        super_brick.draw()
    
    for power_up_big_player in all_power_up_big_player:
        power_up_big_player.draw()

    for power_up_slower in all_power_up_slower:
        power_up_slower.draw()

    for power_up_kill_ennemy in all_power_up_kill_ennemy:
        power_up_kill_ennemy.draw()

    for projectile in all_projectiles:
        projectile.draw()

    for ennemy in all_ennemies:
        ennemy.draw()
    
    for heart in all_heart:
        heart.draw()
    
    player.draw()
    ball.draw()
    
    if loose:
        gameover.draw()
        sounds.laser_5.stop()
    if win:
        victory.draw()
        sounds.laser_5.stop()

def on_mouse_move(pos):
    player.pos = [pos[0], player.pos[1]]

def invert_horzontal_speed():
    ball_speed[0] = ball_speed[0] * -1

def invert_vertical_speed():
    ball_speed[1] = ball_speed[1] * -1

def invert_ennemy_horizontal_speed():
    ennemy_speed[0] = ennemy_speed[0] * -1

def upgrade_ball_speed(upgrade): #augmente la vitesse de la balle
    
    if ball_speed[0] > 0:
        ball_speed[0] = ball_speed[0] + upgrade
    else:
        ball_speed[0] = ball_speed[0] - upgrade

    if ball_speed[1] > 0:
        ball_speed[1] = ball_speed[1] + upgrade
    else:
        ball_speed[1] = ball_speed[1] - upgrade

def on_key_up(key):
    if key == keys.SPACE:
        reboot()

def update(dt):
    global ball
    global ball_speed
    global life
    global loose
    global win
    global ennemy
    global player
    global projectile
    global time_big_player
    global time_kill_ennemies

    if time_big_player > 0:
        time_big_player = time_big_player - dt
    if time_big_player <= 0:
        player = Actor("neon_player2", player.pos)
    
    if time_kill_ennemies > 0:
        time_kill_ennemies = time_kill_ennemies - dt
    if time_kill_ennemies <= 0:
        ball = Actor("neon_ball", ball.pos)

    new_x = ball.pos[0] + ball_speed[0] # new_x = position de la balle + vitesse de la balle (3)
    new_y = ball.pos[1] + ball_speed[1] # new_y = position de la balle + vitesse de la balle (-3)
    ball.pos = [new_x, new_y]
    
    #on peut aussi écrire : ball.pos = [ball.pos[0] + ball_speed[0], ball.pos[1] + ball_speed[1]]

    for ennemy in all_ennemies:
        new_x = ennemy.pos[0] + ennemy_speed[0]
        new_y = ennemy.pos[1] + ennemy_speed[1]
        ennemy.pos = [new_x, new_y]
    
    for projectile in all_projectiles:
        new_x = projectile.pos[0] + projectile_speed[0]
        new_y = projectile.pos[1] + projectile_speed[1]
        projectile.pos = [new_x, new_y]

    for power_up_big_player in all_power_up_big_player: # powerup player descend
        new_x = power_up_big_player[0] + power_up_speed[0]
        new_y = power_up_big_player[1] + power_up_speed[1]
        power_up_big_player.pos = [new_x, new_y]
    
    for power_up_slower in all_power_up_slower: #powerup sablier descend
        new_x = power_up_slower[0] + power_up_speed[0]
        new_y = power_up_slower[1] + power_up_speed[1]
        power_up_slower.pos = [new_x, new_y]
    
    for power_up_kill_ennemy in all_power_up_kill_ennemy:
        new_x = power_up_kill_ennemy[0] + power_up_speed[0]
        new_y = power_up_kill_ennemy[1] + power_up_speed[1]
        power_up_kill_ennemy.pos = [new_x, new_y]

    if ball.right >= WIDTH or ball.left <= 0:
        invert_horzontal_speed()
    
    if ball.top <= 0: #si la balle touche le haut de l'écran
        invert_vertical_speed()

    if ball.colliderect(player): # quand balle touche le joueur elle change de direction + vitesse de la balle
        if ball.pos[0] >= player.left and ball.pos[0] <= player.right:
            invert_vertical_speed()
        else:
            invert_horzontal_speed()
        upgrade_ball_speed(0.70)
    
    for brick in all_bricks: #balle rebondit sur chaques briques, et les powerup apparaissent
        if ball.colliderect(brick):
            if ball.pos[0] >= brick.left and ball.pos[0] <= brick.right:
                invert_vertical_speed()
            else:
                invert_horzontal_speed()
            all_bricks.remove(brick)
            rnd1 = randint(0, 110)
            rnd2 = randint(0, 120)
            rnd3 = randint(0, 140)
            if rnd1 <= power_up_apparition: #check si une powerup(big) apparait
                power_up = Actor("neon_arrow", anchor=["left", "top"])
                power_up.pos = brick.pos
                all_power_up_big_player.append(power_up)
            elif rnd2 <= power_up_apparition:
                power_up2 = Actor("sablier", anchor=["left", "top"]) #check si un sablier apparait #------
                power_up2.pos = brick.pos
                all_power_up_slower.append(power_up2)
            elif rnd3 <= power_up_apparition:
                power_up3 = Actor("star", anchor=["left", "top"]) #check si un  apparait #------
                power_up3.pos = brick.pos
                all_power_up_kill_ennemy.append(power_up3)
    
    for super_brick in all_super_bricks: #quand la balle touche la brique
        if super_brick.colliderect(ball):
            invert_vertical_speed()
            all_super_bricks.remove(super_brick)
            brick = Actor("neon_pink_100", anchor=["left", "top"])
            brick.pos = super_brick.pos
            all_bricks.append(brick)

    for ennemy in all_ennemies: #brique transparent et %projectile
        for transparent_brick in all_transparent_bricks:
            if transparent_brick.colliderect(ennemy):
                invert_ennemy_horizontal_speed()
        rdm = randint(0, 340)
        if rdm < projectile_apparition:
            projectile = Actor("projectile")
            projectile.pos = ennemy.pos
            all_projectiles.append(projectile)
            sounds.laser_5.play()

    for projectile in all_projectiles: #quand les prjectiles touchent le joueur
        if player.colliderect(projectile):
            all_projectiles.remove(projectile)
            all_heart.pop(-1)
            #print("You can take " + str(life) + " more hit(s).")
            life = life - 1
    
    for power_up_big_player in all_power_up_big_player: # player attrape powerup et grandit
        if player.colliderect(power_up_big_player):
            all_power_up_big_player.remove(power_up_big_player)
            time_big_player = 4
            player = Actor("neon_bigger_player", player.pos)
    
    for power_up_slower in all_power_up_slower: #quand le joueur touche le sablier
        if player.colliderect(power_up_slower):
            all_power_up_slower.remove(power_up_slower)
            if ball_speed[0] > 0:
                ball_speed[0] = 3
            else:
                ball_speed[0] = -3
            if ball_speed[1] > 0:
                ball_speed[1] = 3
            else:
                ball_speed[1] = -3

    for power_up_kill_ennemy in all_power_up_kill_ennemy: #player attrape le powerup et balle change
        if player.colliderect(power_up_kill_ennemy):
            all_power_up_kill_ennemy.remove(power_up_kill_ennemy)
            time_kill_ennemies = 5
            ball = Actor("superball", ball.pos)
    
    for ennemy in all_ennemies: #retirer un ennemi touché par la balle
        if ennemy.colliderect(ball) and time_kill_ennemies > 0:
            all_ennemies.pop(-1)

    if (all_bricks == [] and all_super_bricks == []) and not win: #victoire
        music.play("palms")
        music.set_volume(0.4)
        win = True

    elif (ball.bottom > HEIGHT or life == 0) and not loose and not win: #gameover
        music.play("stargazer")
        music.set_volume(0.4)
        loose = True