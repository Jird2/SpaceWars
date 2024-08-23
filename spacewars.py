import pygame
import os   ## Gonna need operating system to help define the path to images
pygame.font.init() ## Initialize pygame font library (for text)
pygame.mixer.init() ## Initialize sound in pygame

pygame.init()
WIDTH, HEIGHT = 900, 500 ## In pygame, (0,0) is the top left corner of the screen
SCREEN = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("SPACE WARS!")

HEART_WIDTH, HEART_HEIGHT = 20,20
FULL_HEART_IMAGE = pygame.image.load(os.path.join('Accessories', 'heart pixel art 254x254.png'))
FULL_HEART = pygame.transform.scale(FULL_HEART_IMAGE, (HEART_WIDTH, HEART_HEIGHT))
OPENING_SOUND = pygame.mixer.Sound(os.path.join('Accessories', 'MegaMan 2 Intro CLIPPED - Made with Clipchamp.mp3'))
GAME_SOUND = pygame.mixer.Sound(os.path.join('Accessories', 'Megaman X - Storm Eagle Stage.mp3' ))
REDWINNER  = (255, 0, 0)
YELLOWWINNER = (255,255,51)
DRAW = (0,0, 175)
STARTING_BACKGROUND = pygame.transform.scale(pygame.image.load(os.path.join('Accessories', 'Blue Nebula 2 - 1024x1024.png')), (WIDTH, HEIGHT))
BORDER = pygame.Rect(WIDTH//2 - 5, 0, 10, HEIGHT) ## Create a border in the middle of the screen using a rectangle
BORDER_WIDTH, BORDER_HEIGHT = 50, HEIGHT
BORDER_IMAGE = pygame.image.load(os.path.join('Accessories', 'Black_hole.png'))
BORDER_IMAGE = pygame.transform.scale(BORDER_IMAGE, (BORDER_WIDTH, BORDER_HEIGHT))
BORDER_X, BORDER_Y = WIDTH//2, HEIGHT//2
BULLET_HIT_SOUND = pygame.mixer.Sound(os.path.join('Accessories', 'GRENADE UPDATED SOUND - Made with Clipchamp.mp3')) ## Command to use sound
BULLET_FIRE_SOUND = pygame.mixer.Sound(os.path.join('Accessories', 'LASER SOUND EFFECT - Made with Clipchamp.mp3'))
VICTORY_SOUND = pygame.mixer.Sound(os.path.join('Accessories', 'Old victory sound roblox.mp3'))
HEALTH_FONT = pygame.font.SysFont('georgia', 40) ## (font, size)
FPS = 60
SPACESHIP_MOVEMENT = 5
BULLET_VELOC = 7 
MAX_BULLETS = 1000
WINNER_FONT = pygame.font.SysFont('georgia', 100)
SPACESHIP_WIDTH, SPACESHIP_HEIGHT = 55, 40 ## Size of spaceship
RSS1I = pygame.image.load(os.path.join('Accessories', 'spaceship_red.png'))
RSS1 = pygame.transform.rotate(pygame.transform.scale(RSS1I, (100,100)), 10)
YSS1I = pygame.image.load(os.path.join('Accessories', 'spaceship_yellow.png'))
YSS1 = pygame.transform.rotate(pygame.transform.scale(YSS1I, (100,100)), 350)
YELLOW_HIT = pygame.USEREVENT + 1 ## Represents the code or number for the custom user events
RED_HIT = pygame.USEREVENT + 2
YELLOW_SPACESHIP_IMAGE = pygame.image.load(os.path.join('Accessories', 'Spaceships - 3.png')) ## Look inside folder for specified images
YELLOW_SPACESHIP = pygame.transform.rotate(pygame.transform.scale(YELLOW_SPACESHIP_IMAGE, (SPACESHIP_WIDTH, SPACESHIP_HEIGHT)), 90) 
ROCKS_WIDTH, ROCKS_HEIGHT = 20,20
ROCKS_IMAGE = pygame.image.load(os.path.join('Accessories', 'Rocks_med.png'))
ROCKS = pygame.transform.scale(ROCKS_IMAGE, (ROCKS_WIDTH, ROCKS_HEIGHT))
DEBRIS_WIDTH, DEBRIS_HEIGHT = 10,10
DEBRIS_IMAGE = pygame.image.load(os.path.join('Accessories', 'Baren.png'))
DEBRIS = pygame.transform.scale(DEBRIS_IMAGE, (DEBRIS_WIDTH, DEBRIS_HEIGHT))
PLANET_WIDTH, PLANET_HEIGHT = 20,20
PLANET_2_IMAGE = pygame.image.load(os.path.join('Accessories', 'Ice.png'))
PLANET2 = pygame.transform.scale(PLANET_2_IMAGE, (PLANET_WIDTH, PLANET_HEIGHT))
PLANET_3_IMAGE = pygame.image.load(os.path.join('Accessories', 'Lava.png'))
PLANET3 = pygame.transform.scale(PLANET_3_IMAGE, (PLANET_WIDTH, PLANET_HEIGHT))
PLANET_4_IMAGE = pygame.image.load(os.path.join('Accessories', 'Terran.png'))
PLANET4 = pygame.transform.scale(PLANET_4_IMAGE, (PLANET_WIDTH, PLANET_HEIGHT))

planets = [
    pygame.transform.scale(pygame.image.load(os.path.join('Accessories', 'Baren.png')), (PLANET_WIDTH, PLANET_HEIGHT)),
    pygame.transform.scale(pygame.image.load(os.path.join('Accessories', 'Ice.png')), (PLANET_WIDTH, PLANET_HEIGHT)),
    pygame.transform.scale(pygame.image.load(os.path.join('Accessories', 'Lava.png')), (PLANET_WIDTH, PLANET_HEIGHT)),
    pygame.transform.scale(pygame.image.load(os.path.join('Accessories', 'Terran.png')), (PLANET_WIDTH, PLANET_HEIGHT))
]

## pygame.transform.scale -> resizes an image, parameters to specify || pygame.transform.rotate -> rotates the image, second argument how much you want: for ex 90 degrees

RED_SPACESHIP_IMAGE = pygame.image.load(os.path.join('Accessories', 'Spaceships - 2.png')) ## os.path.join -> depending on what operating your on, separator may be differen
RED_SPACESHIP = pygame.transform.rotate(pygame.transform.scale(RED_SPACESHIP_IMAGE, (SPACESHIP_WIDTH, SPACESHIP_HEIGHT)), 270)
SPACE = pygame.transform.scale(pygame.image.load(os.path.join('Accessories', 'Starfield 5 - 1024x1024.png')), (WIDTH, HEIGHT))
COLOR_X, COLOR_Y = WIDTH//2 + 100, HEIGHT//2 
BACKGROUND_COLOR = SPACE.get_at((COLOR_X, COLOR_Y))
TITLE_FONT = pygame.font.Font(os.path.join('Accessories', 'VeniteAdoremus-rgRBA.ttf'), 75)
INSTRUCTION_FONT = pygame.font.SysFont('georgia', 30)
WATERMARK_FONT= pygame.font.SysFont('georgia', 15)
SPACE_FONT = pygame.font.SysFont('georgia', 30)
PRESS_FONT = pygame.font.SysFont('georgia', 30)
TO_FONT = pygame.font.SysFont('georgia', 30)
START_FONT = pygame.font.SysFont('georgia', 30)

def draw_start_screen():
    SCREEN.blit(STARTING_BACKGROUND, (0,0))
    SCREEN.blit(RSS1, (35, 45))
    SCREEN.blit(YSS1, (750, 45))
    title = TITLE_FONT.render("SPACE ", True, (255,0,0))
    title2 = TITLE_FONT.render("WARS", True, (255,255,0))
    SCREEN.blit(title, (WIDTH//2 - title.get_width()//2 - 150, HEIGHT//3))
    SCREEN.blit(title2, (WIDTH//2 - title2.get_width()//2 + 150, HEIGHT//3))
    instruction = INSTRUCTION_FONT.render("Press ", True, (255,255,255))
    SCREEN.blit(instruction, (WIDTH//2 - instruction.get_width()//2 - 125, HEIGHT//2))
    space = SPACE_FONT.render("SPACE ", True, (0,150,125))
    SCREEN.blit(space, (WIDTH//2 - space.get_width()//2 - 35, HEIGHT//2))
    to = TO_FONT.render("to ", True, (255,255,255))
    SCREEN.blit(to, (WIDTH//2 - to.get_width()//2 + 35, HEIGHT//2))
    start = START_FONT.render("Start!", True, (255,255,255))
    SCREEN.blit(start, (WIDTH//2 - start.get_width()//2 + 90, HEIGHT//2))
    watermark = WATERMARK_FONT.render("Made by Jird2 :)", True, (255,255,255))
    SCREEN.blit(watermark, (WIDTH//2 - watermark.get_width()//2, HEIGHT - 50))

  ##  instruction = INSTRUCTION_FONT.render("Press SPACE to Start!", True, (255,255,255))
   ## SCREEN.blit(instruction, (WIDTH//2 - instruction.get_width()//2, HEIGHT//2))
    pygame.display.update()

def draw_window(red, yellow, red_bullets, yellow_bullets, red_health, yellow_health):
    SCREEN.blit(SPACE, (0,0))
   ## pygame.draw.rect(SCREEN, BACKGROUND_COLOR, BORDER) # Don't necessarily need the color (invisible border)
   ## SCREEN.blit(red_health_text, (WIDTH - red_health_text.get_width() - 50, 10))
  ## SCREEN.blit(yellow_health_text, (10,10))
  
     # Draw planets along the top edge
    
    for i in range(0, WIDTH, PLANET_WIDTH):
        planet_index = (i // PLANET_WIDTH) % len(planets)
        SCREEN.blit(planets[planet_index], (i, 0))

    # Draw planets along the bottom edge
    for i in range(0, WIDTH, PLANET_WIDTH):
        planet_index = (i // PLANET_WIDTH) % len(planets)
        SCREEN.blit(planets[planet_index], (i, HEIGHT - PLANET_HEIGHT))

    # Draw planets along the left edge
    for i in range(0, HEIGHT, PLANET_HEIGHT):
        planet_index = (i // PLANET_HEIGHT) % len(planets)
        SCREEN.blit(planets[planet_index], (0, i))

    # Draw planets along the right edge
    for i in range(0, HEIGHT, PLANET_HEIGHT):
        planet_index = (i // PLANET_HEIGHT) % len(planets)
        SCREEN.blit(planets[planet_index], (WIDTH - PLANET_WIDTH, i))

    red_health_text = HEALTH_FONT.render("Health: " + str(red_health), 1, REDWINNER)
    yellow_health_text = HEALTH_FONT.render("Health: " + str(yellow_health), 1, REDWINNER)
    for i in range(red_health): 
        SCREEN.blit(FULL_HEART, ( WIDTH - red_health_text.get_width() - 90 + i * (HEART_WIDTH + 5), 25))
    for i in range(yellow_health):
        SCREEN.blit(FULL_HEART, (30+i*(HEART_WIDTH + 5), 25))
        
    SCREEN.blit(YELLOW_SPACESHIP, (yellow.x, yellow.y)) ## use blit() when you want to draw a surface onto a screen (texts/images)
    SCREEN.blit(RED_SPACESHIP, (red.x, red.y))  ## (WIDTH, HEIGHT)
   ## SCREEN.blit(FULL_HEART_IMAGE, (WIDTH, HEIGHT))
   ## SCREEN.blit(FULL_HEART_IMAGE, (WIDTH//2, HEIGHT//2 + 50))

    for bullet in red_bullets:
        pygame.draw.rect(SCREEN, REDWINNER, bullet)
    for bullet in yellow_bullets:
        pygame.draw.rect(SCREEN, YELLOWWINNER, bullet)
    pygame.display.update()
    
    
def yellow_handle_movement(keys_pressed, yellow):
    if keys_pressed[pygame.K_a] and yellow.x - SPACESHIP_MOVEMENT > 0:  # Move left
        yellow.x -= SPACESHIP_MOVEMENT
    if keys_pressed[pygame.K_d] and yellow.x + SPACESHIP_MOVEMENT + yellow.width < BORDER.x + 30:  # Move right
        yellow.x += SPACESHIP_MOVEMENT
    if keys_pressed[pygame.K_w] and yellow.y - SPACESHIP_MOVEMENT > 0:  # Move up
        yellow.y -= SPACESHIP_MOVEMENT
    if keys_pressed[pygame.K_s] and yellow.y + SPACESHIP_MOVEMENT + yellow.height < HEIGHT:  # Move down
        yellow.y += SPACESHIP_MOVEMENT

def red_handle_movement(keys_pressed, red):
    if keys_pressed[pygame.K_LEFT] and red.x - SPACESHIP_MOVEMENT > BORDER.x + BORDER.width - 2:  # Move left
        red.x -= SPACESHIP_MOVEMENT
    if keys_pressed[pygame.K_RIGHT] and red.x + SPACESHIP_MOVEMENT + red.width < WIDTH:  # Move right
        red.x += SPACESHIP_MOVEMENT
    if keys_pressed[pygame.K_UP] and red.y - SPACESHIP_MOVEMENT > 0:  # Move up
        red.y -= SPACESHIP_MOVEMENT
    if keys_pressed[pygame.K_DOWN] and red.y + SPACESHIP_MOVEMENT + red.height < HEIGHT:  # Move down
        red.y += SPACESHIP_MOVEMENT

def handle_bullets(yellow_bullets, red_bullets, yellow, red):
    hitbox_reduce =  5
    yellow_hitbox = pygame.Rect(yellow.x - 30 + hitbox_reduce, yellow.y + hitbox_reduce, yellow.width + 1 * hitbox_reduce, yellow.height - 1 * hitbox_reduce)
    red_hitbox = pygame.Rect(red.x + hitbox_reduce, red.y + hitbox_reduce, red.width + 1 * hitbox_reduce, red.height - 1 * hitbox_reduce)
    for bullet in yellow_bullets:
        bullet.x += BULLET_VELOC    
        if red_hitbox.colliderect(bullet): # If the bullet collides with yellow
            pygame.event.post(pygame.event.Event(RED_HIT))
            yellow_bullets.remove(bullet)
        elif bullet.x > WIDTH:
            yellow_bullets.remove(bullet)
        elif bullet.x < 0:
            red_bullets.remove(bullet)
    for bullet in red_bullets:
        bullet.x -= BULLET_VELOC
        if yellow_hitbox.colliderect(bullet): # If the bullet collides with yellow
            pygame.event.post(pygame.event.Event(YELLOW_HIT))
            red_bullets.remove(bullet)
            
def redwinner(text):     
    draw_text = WINNER_FONT.render(text, 1, REDWINNER)
    SCREEN.blit(draw_text, (WIDTH//2 - draw_text.get_width() // 2, HEIGHT//2 - draw_text.get_height()//2))
    pygame.display.update()
    pygame.time.delay(3000)
    
def yellowwinner(text):
    draw_text = WINNER_FONT.render(text, 1, YELLOWWINNER)
    SCREEN.blit(draw_text, (WIDTH//2 - draw_text.get_width() // 2, HEIGHT//2 - draw_text.get_height()//2))
    pygame.display.update()
    pygame.time.delay(3000)

def draw(text):
    draw_text = WINNER_FONT.render(text, 1, DRAW)
    SCREEN.blit(draw_text, (WIDTH//2 - draw_text.get_width() // 2, HEIGHT//2 - draw_text.get_height()//2))
    pygame.display.update()
    pygame.time.delay(3000)


def main():
    start_screen = True
    OPENING_SOUND.set_volume(0.15)
    OPENING_SOUND.play() # Play sound upon opening
    while start_screen:
        draw_start_screen()
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_ESCAPE:
                    pygame.quit()
                    return
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_SPACE:
                    OPENING_SOUND.stop()
                    GAME_SOUND.set_volume(0.15)
                    GAME_SOUND.play(-1)
                    start_screen = False  # Exit the start screen loop
 
    red = pygame.Rect(700, 300, SPACESHIP_WIDTH, SPACESHIP_HEIGHT)
    yellow = pygame.Rect(100, 300, SPACESHIP_WIDTH, SPACESHIP_HEIGHT)
    clock = pygame.time.Clock() ## Controls the speed of while loop -> 
                                ## Makes sure we run while loop 60 (FPS variable) times per second no matter what (unless computer can't reach 60 FPS) 
    red_health = 10
    yellow_health = 10
    red_bullets = []  ## Red bullet list       
    yellow_bullets = []  ## Yellow bullet list            
    run = True
    
    while run:
        clock.tick(FPS)
        for event in pygame.event.get():
         if event.type == pygame.QUIT:
            pygame.quit()
         if event.type == pygame.KEYDOWN: 
             if event.key == pygame.K_ESCAPE:
                 run = False
                 pygame.quit()
             elif event.key == pygame.K_LSHIFT and len(yellow_bullets) < MAX_BULLETS:
                 bullet = pygame.Rect(yellow.x + yellow.width, yellow.y + yellow.height//2 - 2, 10, 5) ## yellow.height/2 -> bullet will come directly from the middle of the spaceship
                 yellow_bullets.append(bullet)
                 BULLET_FIRE_SOUND.play()
                 BULLET_FIRE_SOUND.set_volume(0.25)
             elif event.key == pygame.K_RALT and len(red_bullets) < MAX_BULLETS:
                bullet = pygame.Rect(red.x, red.y + red.height//2 - 2, 10, 5) 
                red_bullets.append(bullet)
                BULLET_FIRE_SOUND.play()
                BULLET_FIRE_SOUND.set_volume(0.25)
                
         if event.type == RED_HIT:
            red_health -= 1
            BULLET_HIT_SOUND.play()
         if event.type == YELLOW_HIT:
            yellow_health -= 1
            BULLET_HIT_SOUND.play()

        winner_text = ""    
    
        if red_health <= 0:
            winner_text = "YELLOW WINS!"
            VICTORY_SOUND.play()
            GAME_SOUND.stop()
            yellowwinner(winner_text)
            pygame.quit()
        elif yellow_health <= 0:
            winner_text = "RED WINS!"
            VICTORY_SOUND.play()
            GAME_SOUND.stop()
            redwinner(winner_text)
            pygame.quit()
        elif yellow_health and red_health <= 0:
            winner_text = "DRAW!"
            VICTORY_SOUND.play()
            GAME_SOUND.stop()
            draw(winner_text)
            pygame.quit()
        elif winner_text != "":
            break ## Basically equivalent to pygame.quit() = game stops once function completes
        
        
        keys_pressed = pygame.key.get_pressed() 
        yellow_handle_movement(keys_pressed, yellow) ## Call the functions to move the spaceships
        red_handle_movement(keys_pressed, red)
        handle_bullets(yellow_bullets, red_bullets, yellow, red)
        draw_window(red, yellow, red_bullets, yellow_bullets, red_health, yellow_health) ## blit to screen
 
    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                return
            
        main()
if __name__ == "__main__":
    main()