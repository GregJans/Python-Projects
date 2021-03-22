import pygame, random, sys

pygame.init()

width = 800
height = 800
screen = pygame.display.set_mode((width, height))
pygame.display.set_caption('Killer Cubes')

clock = pygame.time.Clock()
speed = 20

xpos = 300
ypos = 300
player_size = 50
player_speed = 20

enemy_size = 30
enemy_x = [random.randint(0, width - enemy_size), random.randint(0, width - enemy_size), random.randint(0, width - enemy_size), random.randint(0, width - enemy_size), random.randint(0, width - enemy_size)]
enemy_y = [random.randint(0, height - enemy_size), random.randint(0, height - enemy_size), random.randint(0, height - enemy_size), random.randint(0, height - enemy_size), random.randint(0, height - enemy_size)]
total_enemies = 5
enemy_speed = [random.randint(1, 7), random.randint(1, 7), random.randint(1, 7), random.randint(1, 7), random.randint(1, 7)]

color = (0,0,255)
score = 0

def border_check():
    global xpos, ypos, width, height, player_size

    if xpos >= width - player_size:
        xpos = width - player_size
    elif xpos <= 0:
        xpos = 0
    if ypos <= 0:
        ypos = 0
    elif ypos >= height - player_size:
        ypos = height - player_size
    

def count():
    global score, total_enemies
    score += 1
    
    if score == 100:
        total_enemies += 1
        enemy_x.append(random.randint(0, width - enemy_size))
        enemy_y.append(random.randint(0, height - enemy_size))
        enemy_speed.append(random.randint(1,7))
        
    elif score == 200:
        for x in range(4):
            enemy_x.append(random.randint(0, width - enemy_size))
            enemy_y.append(random.randint(0, height - enemy_size))
            enemy_speed.append(random.randint(3,10))
        total_enemies += 4
    elif score == 300:
        for x in range(5):
            enemy_x.append(random.randint(0, width - enemy_size))
            enemy_y.append(random.randint(0, height - enemy_size))
            enemy_speed.append(random.randint(5,12))
        total_enemies += 5

def place_enemy():
    global enemy_x, enemy_y, enemy_size, total_enemies

    for i in range(total_enemies):
        pygame.draw.rect(screen, (255,0,0), (enemy_x[i], enemy_y[i], enemy_size, enemy_size))

def move_enemy():
    global enemy_list, enemy_size, gameOver, total_enemies

    for enemy in range(total_enemies):
        if enemy_x[enemy] < xpos:
            enemy_x[enemy] += enemy_speed[enemy]
        if enemy_x[enemy] > xpos:
            enemy_x[enemy] -= enemy_speed[enemy]
        if enemy_y[enemy] < ypos:
            enemy_y[enemy] += enemy_speed[enemy]
        if enemy_y[enemy] > ypos:
            enemy_y[enemy] -= enemy_speed[enemy]

        if xpos - 10 <= enemy_x[enemy] <= xpos + 10 and ypos - 10 <= enemy_y[enemy] <= ypos + 10:
            color = (255,0,0)
            gameOver = True
            





def text_objects(text, font):
    textSurface = font.render(text, True, (255,255,255))
    return textSurface, textSurface.get_rect()

def message_display(text):
    largeText = pygame.font.Font('freesansbold.ttf',50)
    TextSurf, TextRect = text_objects(text, largeText)
    TextRect.center = ((width/2),(50))
    screen.blit(TextSurf, TextRect)


gameOver = False
while not gameOver:

    clock.tick(speed)

    for event in pygame.event.get():

        #Allows you to close out window
        if event.type == pygame.QUIT:
            sys.exit()

        #scanns for key press

    keys = pygame.key.get_pressed()

    if keys[pygame.K_LEFT]:
        xpos -= player_speed
    if keys[pygame.K_RIGHT]:
        xpos += player_speed
    if keys[pygame.K_UP]:
        ypos -= player_speed
    if keys[pygame.K_DOWN]:
        ypos += player_speed
            
    
    border_check()
    count()
    
    screen.fill((0,0,0))

    place_enemy()
    move_enemy()
    
    message_display(f'Score: {score}')

    pygame.draw.rect(screen, color, (xpos, ypos, player_size, player_size))

    

    pygame.display.update()


sys.exit()