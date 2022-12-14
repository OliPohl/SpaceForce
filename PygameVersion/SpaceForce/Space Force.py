import pygame
import numpy as np
import time
import random

##################################
#       Initializing Pygame      #
##################################

pygame.init()
pygame.font.init()
pygame.mixer.pre_init(44100, 16, 2, 4096)
pygame.mixer.init()
running = True

size_x = 1920
size_y = 1080
size = (size_x, size_y)
screen = pygame.display.set_mode(size)
pygame.display.set_caption('Space Force')

time = 0
FPS = 30
fpsClock = pygame.time.Clock()

##################################
#        Music and Sound         #
##################################
# music
pygame.mixer.music.load('Assets\Killer.wav')
pygame.mixer.music.set_volume(0.00)
pygame.mixer.music.play(loops=-1)


# sounds
laser = pygame.mixer.Sound('Assets\laser.wav')

pl_get_dmg_sound = pygame.mixer.Sound('Assets\pl_dmg.wav')

explosion_sound = pygame.mixer.Sound('Assets\explosion_sound.wav')

# settings

mute = pygame.image.load('Assets\mute.png')
mute = pygame.transform.scale(mute, (35,35))

volume1 = pygame.image.load('Assets\_volume1.png')
volume1 = pygame.transform.scale(volume1, (35,35))

volume2 = pygame.image.load('Assets\_volume2.png')
volume2 = pygame.transform.scale(volume2, (35,35))

volume3 = pygame.image.load('Assets\_volume3.png')
volume3 = pygame.transform.scale(volume3, (35,35))

volume4 = pygame.image.load('Assets\_volume4.png')
volume4 = pygame.transform.scale(volume4, (35,35))

player_name = '   '
player_name = str(np.genfromtxt('Assets\pl_name.txt',dtype='str'))

music_set = 0
effect_set = 0
music_set, effect_set = np.loadtxt('Assets\settings.txt', unpack=True)


img_check = pygame.image.load('Assets\img_check.png')
img_check = pygame.transform.scale(img_check, (45,45))

img_check1 = pygame.image.load('Assets\img_check1.png')
img_check1 = pygame.transform.scale(img_check1, (45,45))

##################################
#            Variables           #
##################################


hs_s_1 = 0
hs_n_1 = '  '

hs_s_2 = 0
hs_n_2 = '  '

hs_s_3 = 0
hs_n_3 = '  '

hs_s_4 = 0
hs_n_4 = '  '

hs_s_5 = 0
hs_n_5 = '  '

hs_s_1, hs_s_2, hs_s_3, hs_s_4, hs_s_5 = np.loadtxt('Assets\hss.txt', unpack=True)
hs_n_1, hs_n_2, hs_n_3, hs_n_4, hs_n_5 = np.genfromtxt('Assets\hsn.txt',dtype='str')

hs_s_1, hs_s_2, hs_s_3, hs_s_4, hs_s_5 = round(hs_s_1), round(hs_s_2), round(hs_s_3), round(hs_s_4), round(hs_s_5)
hs_n_1, hs_n_2, hs_n_3, hs_n_4, hs_n_5 = str(hs_n_1), str(hs_n_2), str(hs_n_3), str(hs_n_4), str(hs_n_5)

hs_1 = False
hs_2 = False
hs_3 = False
hs_4 = False
hs_5 = False

dev_commands = True

highscore = 0   # highscore
score = 0       # current score
hp = 3          # current life
pl_get_dmg = False      # player gets dmged
invulnerable_time = 0   # time invulnerable after getting damaged
bullets = True    # allowes bullets

# Phases
rd_cubes = False    # lets random cubes fly across the map
rd_walls = False     # Lets random walls spawn
rd_cubes_hard = False # lets random cubes fly across the map and makes them move
rd_walls_hard = False # Lets random walls spawn and makes them move
s_boss = False      # Lets you fight the small boss
b_boss = False      # Lets you fight the big boss
rd_walls2 = False

Round = 6       # Round 1
menu = True
settings_ = False
time_round = 0  # Round timer
time_round_max = 1200
time_button = 0
time_button2 = 0
time_hp = 0
bg_sp_multi = 2
esc_lock = False
death = False
next_key = True
player_name_len = 10
time_name = 0
next_key_back = 0

##################################
#        Colors and Fonts        #
##################################

background_color = (45, 45, 45)

BLACK = (20, 20, 20)
GRAY = (120, 120, 120)
D_GRAY = (45, 45, 45)
D_GRAY2 = (66, 66, 66)
D_GRAY3 = (159, 68, 92)
D_GRAY3_2 = (45, 79, 130)
D_GRAY4 = (149, 48, 82)
WHITE = (245, 230, 210)
RED = (205, 190, 177)

Pink = (214,0,255)
GREEN = (10,180,100)
BLUE = (33, 101, 118)
CYAN = 	(45, 79, 130)
MAGENTA = (189,0,255)

LIGHT_YELLOW = (220, 179, 110) # cplor progress bar
LIGHT_YELLOW2 = (240, 199, 130)

CUBE_COLOR1 = (251, 238, 223)  
CUBE_COLOR2 = (254, 247, 100)    
CUBE_COLOR3 = (239, 117, 191)    
CUBE_COLOR4 = (255, 146, 44)   
CUBE_COLOR5 = (236, 32, 79)     

COLOR_KEYS = (245, 230, 210)
COLOR_KEYS_TITLE = (159, 68, 92)
COLOR_KEYS_BG = (120, 120, 120)


WALL_COLOR1 = (94, 168, 161)       # Green

BUTTON = (149, 125, 173)
BUTTON2 = (210, 145, 188)

MUSIC_BUTTONS = (220, 179, 110)
MUSIC_BUTTONS_ACTIVE = (149, 48, 82)
MUSIC_BUTTONS_HOVER = (159, 68, 92)

BUTTON3 = (149, 48, 82)
BUTTON4 = (179, 88, 112)

BULLET_COLOR = (255, 255, 0)    # Yellow
SCORE_CLR = (199, 48, 72)



font_gamename = pygame.font.Font('Assets\saved by zero rg.otf', 40)
font_score = pygame.font.Font('Assets\saved by zero rg.otf', 30)
font_tacho = pygame.font.Font('Assets\saved by zero rg.otf', 15)
font_progress = pygame.font.Font('Assets\saved by zero rg.otf', 60)
font_nametag = pygame.font.Font('Assets\saved by zero rg.otf', 25)


##################################
#            Objects             #
##################################

# settings'Assets\
settings = pygame.image.load('Assets\settings.png')
settings = pygame.transform.scale(settings, (40,40))
death_bg = pygame.image.load('Assets\death_bg.png')
death_bg = pygame.transform.scale(death_bg, (840, 540))

hs_bg = pygame.image.load('Assets\hs_bg.png')
hs_bg = pygame.transform.scale(hs_bg, (840, 540))

# background
background = pygame.image.load('Assets\city_background.png')
background2 = background

bg_sp = 11
sp_bg = 10
bg_x = 0
bg_x2 = bg_x + 2600

# player data
pl_height = 50     # height of the player (hitbox)
pl_length = 100     # length of the player (hitbox)
pl_x = 145          # starting x position of the player
pl_y = 500          # starting y position of the player
sp_x = 10           # sidewards speed of the player
sp_y_up = 16           # upwards speed of the player
sp_y_down = sp_y_up
sp_x_save = sp_x
sp_y_up_save = sp_y_up
sp_y_down_save = sp_y_down
border = 15         # map boundary for the player
ship = pygame.image.load('Assets\ship.png')
ship_DMG = pygame.image.load('Assets\ship_DMG.png')


# header
header_y = 5

# bullets
bullet1_fly, bullet2_fly, bullet3_fly, bullet4_fly, bullet5_fly, bullet6_fly, bullet7_fly, bullet8_fly, bullet9_fly, bullet10_fly = False, False, False, False, False, False, False, False, False, False
bullet1_x, bullet2_x, bullet3_x, bullet4_x, bullet5_x, bullet6_x, bullet7_x, bullet8_x, bullet9_x, bullet10_x = -100, -100, -100, -100, -100, -100, -100, -100, -100, -100
bullet1_y, bullet2_y, bullet3_y, bullet4_y, bullet5_y, bullet6_y, bullet7_y, bullet8_y, bullet9_y, bullet10_y = -100, -100, -100, -100, -100, -100, -100, -100, -100, -100

bullet_len = 35
bullet_sp = 20
shooting = False

#explosion
explosion1 = pygame.image.load('Assets\explosion1.png')
explosion1 = pygame.transform.scale(explosion1, (100,100))
explosion2 = pygame.image.load('Assets\explosion2.png')
explosion2 = pygame.transform.scale(explosion2, (100,100))
explosion3 = pygame.image.load('Assets\explosion3.png')
explosion3 = pygame.transform.scale(explosion3, (100,100))

##################################
#             Level              #
##################################

# cubes
cube_size =  50
cube_hp1 = 1
cube_hp2 = 2
cube_hp3 = 3
cube_hp4 = 4
cube_hp5 = 5

cube1_hp, cube2_hp, cube3_hp, cube4_hp = cube_hp1, cube_hp1, cube_hp1, cube_hp1
cube5_hp, cube6_hp, cube7_hp, cube8_hp = cube_hp2, cube_hp2, cube_hp2, cube_hp2
cube9_hp, cube10_hp, cube11_hp, cube12_hp = cube_hp3, cube_hp3, cube_hp3, cube_hp3
cube13_hp, cube14_hp, cube15_hp, cube16_hp = cube_hp4, cube_hp4, cube_hp4, cube_hp4
cube17_hp, cube18_hp, cube19_hp, cube20_hp = cube_hp5, cube_hp5, cube_hp5, cube_hp5

cube1_x = random.randrange(1920, 3840, (cube_size))    
cube1_y = random.randrange(0, 945, (cube_size))
cube2_x = random.randrange(1920, 3840, (cube_size))    
cube2_y = random.randrange(0, 945, (cube_size))
cube3_x = random.randrange(1920, 3840, (cube_size))    
cube3_y = random.randrange(0, 945, (cube_size))
cube4_x = random.randrange(1920, 3840, (cube_size))    
cube4_y = random.randrange(0, 945, (cube_size))


cube5_x = random.randrange(1920, 3840, (cube_size))    
cube5_y = random.randrange(0, 945, (cube_size))
cube6_x = random.randrange(1920, 3840, (cube_size))    
cube6_y = random.randrange(0, 945, (cube_size))
cube7_x = random.randrange(1920, 3840, (cube_size))    
cube7_y = random.randrange(0, 945, (cube_size))
cube8_x = random.randrange(1920, 3840, (cube_size))    
cube8_y = random.randrange(0, 945, (cube_size))

cube9_x = random.randrange(1920, 3840, (cube_size))    
cube9_y = random.randrange(0, 945, (cube_size))
cube10_x = random.randrange(1920, 3840, (cube_size))    
cube10_y = random.randrange(0, 945, (cube_size))
cube11_x = random.randrange(1920, 3840, (cube_size))    
cube11_y = random.randrange(0, 945, (cube_size))
cube12_x = random.randrange(1920, 3840, (cube_size))    
cube12_y = random.randrange(0, 945, (cube_size))

cube13_x = random.randrange(1920, 3840, (cube_size))    
cube13_y = random.randrange(0, 945, (cube_size))
cube14_x = random.randrange(1920, 3840, (cube_size))    
cube14_y = random.randrange(0, 945, (cube_size))
cube15_x = random.randrange(1920, 3840, (cube_size))    
cube15_y = random.randrange(0, 945, (cube_size))
cube16_x = random.randrange(1920, 3840, (cube_size))    
cube16_y = random.randrange(0, 945, (cube_size))

cube17_x = random.randrange(1920, 3840, (cube_size))    
cube17_y = random.randrange(0, 945, (cube_size))
cube18_x = random.randrange(1920, 3840, (cube_size))    
cube18_y = random.randrange(0, 945, (cube_size))
cube19_x = random.randrange(1920, 3840, (cube_size))    
cube19_y = random.randrange(0, 945, (cube_size))
cube20_x = random.randrange(1920, 3840, (cube_size))    
cube20_y = random.randrange(0, 945, (cube_size))

cube1_x_rd = random.randrange(3, 7, (1))
cube2_x_rd = random.randrange(3, 7, (1))
cube3_x_rd = random.randrange(3, 7, (1))
cube4_x_rd = random.randrange(3, 7, (1))

cube5_x_rd = random.randrange(3, 7, (1))
cube6_x_rd = random.randrange(3, 7, (1))
cube7_x_rd = random.randrange(3, 7, (1))
cube8_x_rd = random.randrange(3, 7, (1))

cube9_x_rd = random.randrange(3, 7, (1))
cube10_x_rd = random.randrange(3, 7, (1))
cube11_x_rd = random.randrange(3, 7, (1))
cube12_x_rd = random.randrange(3, 7, (1))

cube13_x_rd = random.randrange(3, 7, (1))
cube14_x_rd = random.randrange(3, 7, (1))
cube15_x_rd = random.randrange(3, 7, (1))
cube16_x_rd = random.randrange(3, 7, (1))

cube17_x_rd = random.randrange(3, 7, (1))
cube18_x_rd = random.randrange(3, 7, (1))
cube19_x_rd = random.randrange(3, 7, (1))
cube20_x_rd = random.randrange(3, 7, (1))

cube1_y_rd = random.randrange(3, 7, (1))
cube2_y_rd = random.randrange(3, 7, (1))
cube3_y_rd = random.randrange(3, 7, (1))
cube4_y_rd = random.randrange(3, 7, (1))

cube5_y_rd = random.randrange(3, 7, (1))
cube6_y_rd = random.randrange(3, 7, (1))
cube7_y_rd = random.randrange(3, 7, (1))
cube8_y_rd = random.randrange(3, 7, (1))

cube9_y_rd = random.randrange(3, 7, (1))
cube10_y_rd = random.randrange(3, 7, (1))
cube11_y_rd = random.randrange(3, 7, (1))
cube12_y_rd = random.randrange(3, 7, (1))

cube13_y_rd = random.randrange(3, 7, (1))
cube14_y_rd = random.randrange(3, 7, (1))
cube15_y_rd = random.randrange(3, 7, (1))
cube16_y_rd = random.randrange(3, 7, (1))

cube17_y_rd = random.randrange(3, 7, (1))
cube18_y_rd = random.randrange(3, 7, (1))
cube19_y_rd = random.randrange(3, 7, (1))
cube20_y_rd = random.randrange(3, 7, (1))


time_rd_cubes = 0
time_rd_walls = 0
time_rd_walls2 = 0

# Walls
#pygame.draw.rect(screen, (WALL_COLOR1), ((wall1_x, wall1_y), (wall_height, wall_width)))
wall_height = 1030
wall_width = 100

wall1_x = 1920
wall1_y = random.randrange(-1010, -250, (150))

wall2_x = 2560
wall2_y = random.randrange(-1010, -250, (150))

wall3_x = 3200
wall3_y = random.randrange(-1010, -250, (150))

door2_str = 1
door2_hp = door2_str
sc_door2_reset = False


# rd_cubes_hard
cube1_y_move = 0
cube2_y_move = 0
cube3_y_move = 0
cube4_y_move = 0

cube5_y_move = 0
cube6_y_move = 0
cube7_y_move = 0
cube8_y_move = 0

cube9_y_move = 0
cube10_y_move = 0
cube11_y_move = 0
cube12_y_move = 0

cube13_y_move = 0
cube14_y_move = 0
cube15_y_move = 0
cube16_y_move = 0

cube17_y_move = 0
cube18_y_move = 0
cube19_y_move = 0
cube20_y_move = 0

time_cube = 0
cube_rs = True

# rd_walls_hard

wall1_y_move_up = 0
wall2_y_move_up = 0
wall3_y_move_up = 0

wall1_y_move_down = 0
wall2_y_move_down = 0
wall3_y_move_down = 0

time_wall = 0
wall_rs = True


# sboss
s_boss1_x = 2000
s_boss1_y = 0

s_boss2_x = 2000
s_boss2_y = 282

s_boss3_x = 2000
s_boss3_y = 562

s_boss4_x = 2000
s_boss4_y = 846

s_boss1_1_x = -180
s_boss2_1_x = -180
s_boss3_1_x = -180
s_boss4_1_x = -180

s_boss1_beam_pos = 0, - 1000
s_boss2_beam_pos = 0, - 1000
s_boss3_beam_pos = 0, - 1000
s_boss4_beam_pos = 0, - 1000

time_beam = 0
time_beam_outro = False
s_boss_end = False

s_boss1_y_rand = random.randrange(0, 90, (2))
s_boss2_y_rand = random.randrange(190, 372, (2))
s_boss3_y_rand = random.randrange(472, 654, (2))
s_boss4_y_rand = random.randrange(754, 846, (2))



# bboss
b_boss_finished = False
b_boss_hp = 390

b_boss_x = 2000
b_boss_y = 300
time_bboss = 0

img_bboss_face1 = pygame.image.load('Assets\img_bboss_face1.png')
img_bboss_face2 = pygame.image.load('Assets\img_bboss_face2.png')
img_bboss_face3 = pygame.image.load('Assets\img_bboss_face3.png')
img_bboss_face4 = pygame.image.load('Assets\img_bboss_face1.png')

wall4_x = -150
wall4_y = random.randrange(0, 900, (150))
                    
wall5_x = -790
wall5_y = random.randrange(0, 900, (150))
                    
wall6_x = -1430
wall6_y = random.randrange(0, 900, (150))

# phase 3
phase3 = False

b_boss_box_1_x = 500
b_boss_box_1_y = -100

b_boss_box_2_x = 1000
b_boss_box_2_y = -100

b_boss_box_1_1_y = 950
b_boss_box_2_1_y = 950

b_boss_beam_1_pos = -1000, -2000
b_boss_beam_2_pos = -1000, -2000

time_box_b_boss = 0
time_box_outro_b_boss = False
b_boss_end = False

b_boss_box_1_x_rand = random.randrange(0, 650, (5))
b_boss_box_2_x_rand = random.randrange(650, 1300, (5))
##################################
#              SCORE             #
##################################

sc_cubes1 = 20                              # 20
sc_cubes2 = round(sc_cubes1 * 2 * 1.1)      # 44
sc_cubes3 = round(sc_cubes2 * 1.5 * 1.1)    # 73
sc_cubes4 = round(sc_cubes3 * 1.33 * 1.1)   # 107
sc_cubes5 = round(sc_cubes4 * 1.25 * 1.1)   # 147





##################################
#            The Game            #
##################################

while running:
    for event in pygame.event.get():    # X to exit the game
        if event.type == pygame.QUIT: 
            np.savetxt('Assets\settings.txt', np.array([music_set, effect_set]))
            np.savetxt('Assets\pl_name.txt', [player_name], delimiter=" ", fmt="%s")
            np.savetxt('Assets\hss.txt', np.array([hs_s_1, hs_s_2, hs_s_3, hs_s_4, hs_s_5]))
            np.savetxt('Assets\hsn.txt', np.array([hs_n_1, hs_n_2, hs_n_3, hs_n_4, hs_n_5]), delimiter=" ", fmt="%s")
            running = False
            
            
    ##################################
    #            Keybinds            #
    ##################################  
    pressed = pygame.key.get_pressed()
    pos = pygame.mouse.get_pos()
    if pressed[pygame.K_w]:
        if pl_y > border + header_y + 5 + pl_height/2:
            pl_y -= sp_y_up
    if pressed[pygame.K_s]:
        if pl_y < size_y - border - 135 - pl_height/2:
            pl_y += sp_y_down
    if pressed[pygame.K_d]:
        if pl_x < size_x - border - pl_length:
            pl_x += sp_x
    if pressed[pygame.K_a]:
        if pl_x > border:
            pl_x -= sp_x
    if pressed[pygame.K_ESCAPE] and esc_lock == False:        
        menu = True
        settings_ = False
        
    ##################################
    #             MUSIC              #
    ##################################
        
    if music_set == 0:
        pygame.mixer.music.set_volume(0.00)
    elif music_set == 1:
        pygame.mixer.music.set_volume(0.01)  
    elif music_set == 2:
        pygame.mixer.music.set_volume(0.03)
    elif music_set == 3:
        pygame.mixer.music.set_volume(0.06)
    elif music_set == 4:
        pygame.mixer.music.set_volume(0.12)
        

    if effect_set == 0:
        laser.set_volume(0.00)
        pl_get_dmg_sound.set_volume(0.0)
        explosion_sound.set_volume(0.0)
    elif effect_set == 1:
        laser.set_volume(0.05)
        pl_get_dmg_sound.set_volume(0.08)  
        explosion_sound.set_volume (0.05) 
    elif effect_set == 2:
        laser.set_volume(0.1)
        pl_get_dmg_sound.set_volume(0.15)
        explosion_sound.set_volume(0.1)
    elif effect_set == 3:
        laser.set_volume(0.15)
        pl_get_dmg_sound.set_volume(0.25)
        explosion_sound.set_volume(0.15)
    elif effect_set == 4:
        laser.set_volume(0.2)
        pl_get_dmg_sound.set_volume(0.5)
        explosion_sound.set_volume(0.3)
        
    
    ##################################
    #         Hitbox Player          #
    ##################################
    hitbox_player = pygame.draw.rect(screen, (GREEN), ((pl_x + 1, pl_y - 30),(pl_length, pl_height- 10)))  # draws the player hitbox


    ##################################
    #           Background           #
    ##################################
    screen.fill(BLACK)
    screen.blit(background, (bg_x , 0))
    screen.blit(background2, (bg_x2 , 0))
    
    bg_x -= sp_bg
    bg_x2 -= sp_bg   
    if bg_x < -2600:
        bg_x = 2590
    if bg_x2 < -2600:
        bg_x2 = 2590


    ##################################
    #          Dev Commands          #
    ################################## 
    if dev_commands == True:
        if pressed[pygame.K_p]:
            b_boss_finished = True
        if pressed[pygame.K_7]:
            time_round -= 100
        if pressed[pygame.K_8]:
            time_round += 100
        if pressed[pygame.K_1]:
            rd_cubes_hard = False
            rd_walls = False
            rd_walls_hard = False
            s_boss = False
            b_boss = False
            time_round = 0
            Round = 1
        if pressed[pygame.K_2]:
            rd_cubes = False
            rd_cubes_hard = False
            rd_walls_hard = False
            s_boss = False
            b_boss = False
            time_round = 0
            Round = 2
        if pressed[pygame.K_3]:
            rd_cubes = False
            rd_cubes_hard = False
            rd_walls = False
            rd_walls_hard = False
            b_boss = False
            time_round = 0
            Round = 3
        if pressed[pygame.K_4]:
            rd_walls = False
            rd_walls_hard = False
            s_boss = False
            b_boss = False
            time_round = 0
            Round = 4
        if pressed[pygame.K_5]:
            Round = 5
            rd_cubes = False
            rd_cubes_hard = False
            s_boss = False
            b_boss = False
            time_round = 0
        if pressed[pygame.K_6]:
            rd_cubes = False
            rd_cubes_hard = False
            rd_walls = False
            rd_walls_hard = False
            s_boss = False
            time_round = 0
            Round = 6
        if pressed[pygame.K_9]:
            bg_sp -= 1
        if pressed[pygame.K_0]:
            bg_sp += 1
        if pressed[pygame.K_PLUS]:
            b_boss_hp -= 10
        if pressed[pygame.K_HASH]:
            if hp < 3:
                hp += 1
        
        #dev stats
        # txt_dev = font_score.render('wall1_x: ' + str(wall1_x), False, (WHITE))
        # screen.blit(txt_dev, (40 , 20))

        # txt_speed = font_score.render('wall1_y: ' + str(wall1_y), False, (WHITE))
        # screen.blit(txt_speed, (40 , 100))
        
        
        
    ##################################
    #             Rounds             #
    ##################################
    if rd_cubes == True:    # rd cubescube2_x = random.randrange(1920, 3840, (cube_size))
        
        if time_rd_cubes < 2 and menu == False and b_boss == False:
            time_rd_cubes += 1
        if time_rd_cubes == 1 and menu == False and b_boss == False:
            cube1_x = random.randrange(1920, 3840, (cube_size))    
            cube1_y = random.randrange(0, 945, (cube_size))
            cube2_x = random.randrange(1920, 3840, (cube_size))    
            cube2_y = random.randrange(0, 945, (cube_size))
            cube3_x = random.randrange(1920, 3840, (cube_size))    
            cube3_y = random.randrange(0, 945, (cube_size))
            cube4_x = random.randrange(1920, 3840, (cube_size))    
            cube4_y = random.randrange(0, 945, (cube_size))

            cube5_x = random.randrange(1920, 3840, (cube_size))    
            cube5_y = random.randrange(0, 945, (cube_size))
            cube6_x = random.randrange(1920, 3840, (cube_size))    
            cube6_y = random.randrange(0, 945, (cube_size))
            cube7_x = random.randrange(1920, 3840, (cube_size))    
            cube7_y = random.randrange(0, 945, (cube_size))
            cube8_x = random.randrange(1920, 3840, (cube_size))    
            cube8_y = random.randrange(0, 945, (cube_size))

            cube9_x = random.randrange(1920, 3840, (cube_size))    
            cube9_y = random.randrange(0, 945, (cube_size))
            cube10_x = random.randrange(1920, 3840, (cube_size))    
            cube10_y = random.randrange(0, 945, (cube_size))
            cube11_x = random.randrange(1920, 3840, (cube_size))    
            cube11_y = random.randrange(0, 945, (cube_size))
            cube12_x = random.randrange(1920, 3840, (cube_size))    
            cube12_y = random.randrange(0, 945, (cube_size))

            cube13_x = random.randrange(1920, 3840, (cube_size))    
            cube13_y = random.randrange(0, 945, (cube_size))
            cube14_x = random.randrange(1920, 3840, (cube_size))    
            cube14_y = random.randrange(0, 945, (cube_size))
            cube15_x = random.randrange(1920, 3840, (cube_size))    
            cube15_y = random.randrange(0, 945, (cube_size))
            cube16_x = random.randrange(1920, 3840, (cube_size))    
            cube16_y = random.randrange(0, 945, (cube_size))

            cube17_x = random.randrange(1920, 3840, (cube_size))    
            cube17_y = random.randrange(0, 945, (cube_size))
            cube18_x = random.randrange(1920, 3840, (cube_size))    
            cube18_y = random.randrange(0, 945, (cube_size))
            cube19_x = random.randrange(1920, 3840, (cube_size))    
            cube19_y = random.randrange(0, 945, (cube_size))
            cube20_x = random.randrange(1920, 3840, (cube_size))    
            cube20_y = random.randrange(0, 945, (cube_size))
            
            
        pygame.draw.rect(screen, (CUBE_COLOR1), ((cube1_x, cube1_y), (cube_size, cube_size)))
        pygame.draw.rect(screen, (CUBE_COLOR1), ((cube2_x, cube2_y), (cube_size, cube_size)))
        pygame.draw.rect(screen, (CUBE_COLOR1), ((cube3_x, cube3_y), (cube_size, cube_size)))
        pygame.draw.rect(screen, (CUBE_COLOR1), ((cube4_x, cube4_y), (cube_size, cube_size)))
        
        pygame.draw.rect(screen, (CUBE_COLOR2), ((cube5_x, cube5_y), (cube_size, cube_size)))
        pygame.draw.rect(screen, (CUBE_COLOR2), ((cube6_x, cube6_y), (cube_size, cube_size)))
        pygame.draw.rect(screen, (CUBE_COLOR2), ((cube7_x, cube7_y), (cube_size, cube_size)))
        pygame.draw.rect(screen, (CUBE_COLOR2), ((cube8_x, cube8_y), (cube_size, cube_size)))
        
        pygame.draw.rect(screen, (CUBE_COLOR3), ((cube9_x, cube9_y), (cube_size, cube_size)))
        pygame.draw.rect(screen, (CUBE_COLOR3), ((cube10_x, cube10_y), (cube_size, cube_size)))
        pygame.draw.rect(screen, (CUBE_COLOR3), ((cube11_x, cube11_y), (cube_size, cube_size)))
        pygame.draw.rect(screen, (CUBE_COLOR3), ((cube12_x, cube12_y), (cube_size, cube_size)))
        
        pygame.draw.rect(screen, (CUBE_COLOR4), ((cube13_x, cube13_y), (cube_size, cube_size)))
        pygame.draw.rect(screen, (CUBE_COLOR4), ((cube14_x, cube14_y), (cube_size, cube_size)))
        pygame.draw.rect(screen, (CUBE_COLOR4), ((cube15_x, cube15_y), (cube_size, cube_size)))
        pygame.draw.rect(screen, (CUBE_COLOR4), ((cube16_x, cube16_y), (cube_size, cube_size)))
        
        pygame.draw.rect(screen, (CUBE_COLOR5), ((cube17_x, cube17_y), (cube_size, cube_size)))
        pygame.draw.rect(screen, (CUBE_COLOR5), ((cube18_x, cube18_y), (cube_size, cube_size)))
        pygame.draw.rect(screen, (CUBE_COLOR5), ((cube19_x, cube19_y), (cube_size, cube_size)))
        pygame.draw.rect(screen, (CUBE_COLOR5), ((cube20_x, cube20_y), (cube_size, cube_size)))

        if menu == False and b_boss == False:
            cube1_x -= round(bg_sp * (cube1_x_rd/10 +1))
            cube2_x -= round(bg_sp * (cube2_x_rd/10 +1))
            cube3_x -= round(bg_sp * (cube3_x_rd/10 +1))
            cube4_x -= round(bg_sp * (cube4_x_rd/10 +1))
            
            cube5_x -= round(bg_sp * (cube5_x_rd/10 +1))
            cube6_x -= round(bg_sp * (cube6_x_rd/10 +1))
            cube7_x -= round(bg_sp * (cube7_x_rd/10 +1))
            cube8_x -= round(bg_sp * (cube8_x_rd/10 +1))
            
            cube9_x -= round(bg_sp * (cube9_x_rd/10 +1))
            cube10_x -= round(bg_sp * (cube10_x_rd/10 +1))
            cube11_x -= round(bg_sp * (cube11_x_rd/10 +1))
            cube12_x -= round(bg_sp * (cube12_x_rd/10 +1))
            
            cube13_x -= round(bg_sp * (cube13_x_rd/10 +1))
            cube14_x -= round(bg_sp * (cube14_x_rd/10 +1))
            cube15_x -= round(bg_sp * (cube15_x_rd/10 +1))
            cube16_x -= round(bg_sp * (cube16_x_rd/10 +1))
            
            cube17_x -= round(bg_sp * (cube17_x_rd/10 +1))
            cube18_x -= round(bg_sp * (cube18_x_rd/10 +1))
            cube19_x -= round(bg_sp * (cube19_x_rd/10 +1))
            cube20_x -= round(bg_sp * (cube20_x_rd/10 +1))
        
            if (cube1_x <= -cube_size or cube1_hp <= 0) and (cube_rs == True):
                cube1_hp = cube_hp1
                cube1_x_rd = random.randrange(3, 7, (1))
                cube1_x = random.randrange(1920, 3840, (cube_size))    
                cube1_y = random.randrange(0, 945, (cube_size))
            if (cube2_x <= -cube_size or cube2_hp <= 0) and (cube_rs == True):
                cube2_hp = cube_hp1
                cube2_x_rd = random.randrange(3, 7, (1))
                cube2_x = random.randrange(1920, 3840, (cube_size))    
                cube2_y = random.randrange(0, 945, (cube_size))
            if (cube3_x <= -cube_size or cube3_hp <= 0) and (cube_rs == True):
                cube3_hp = cube_hp1
                cube3_x_rd = random.randrange(3, 7, (1))
                cube3_x = random.randrange(1920, 3840, (cube_size))    
                cube3_y = random.randrange(0, 945, (cube_size))
            if (cube4_x <= -cube_size or cube4_hp <= 0) and (cube_rs == True):
                cube4_hp = cube_hp1
                cube4_x_rd = random.randrange(3, 7, (1))
                cube4_x = random.randrange(1920, 3840, (cube_size))    
                cube4_y = random.randrange(0, 945, (cube_size))
                
            if (cube5_x <= -cube_size or cube5_hp <= 0) and (cube_rs == True):
                cube5_hp = cube_hp2
                cube5_x_rd = random.randrange(3, 7, (1))
                cube5_x = random.randrange(1920, 3840, (cube_size))   
                cube5_y = random.randrange(0, 945, (cube_size))
            if (cube6_x <= -cube_size or cube6_hp <= 0) and (cube_rs == True):
                cube6_hp = cube_hp2
                cube6_x_rd = random.randrange(3, 7, (1))
                cube6_x = random.randrange(1920, 3840, (cube_size))   
                cube6_y = random.randrange(0, 945, (cube_size))
            if (cube7_x <= -cube_size or cube7_hp <= 0) and (cube_rs == True): 
                cube7_hp = cube_hp2
                cube7_x_rd = random.randrange(3, 7, (1))
                cube7_x = random.randrange(1920, 3840, (cube_size))   
                cube7_y = random.randrange(0, 945, (cube_size))
            if (cube8_x <= -cube_size or cube8_hp <= 0) and (cube_rs == True):
                cube8_hp = cube_hp2
                cube8_x_rd = random.randrange(3, 7, (1))
                cube8_x = random.randrange(1920, 3840, (cube_size))   
                cube8_y = random.randrange(0, 945, (cube_size))       
                
            if (cube9_x <= -cube_size or cube9_hp <= 0) and (cube_rs == True):
                cube9_hp = cube_hp3
                cube9_x_rd = random.randrange(3, 7, (1))
                cube9_x = random.randrange(1920, 3840, (cube_size))   
                cube9_y = random.randrange(0, 945, (cube_size))
            if (cube10_x <= -cube_size or cube10_hp <= 0) and (cube_rs == True):
                cube10_hp = cube_hp3
                cube10_x_rd = random.randrange(3, 7, (1))
                cube10_x = random.randrange(1920, 3840, (cube_size))   
                cube10_y = random.randrange(0, 945, (cube_size))
            if (cube11_x <= -cube_size or cube11_hp <= 0) and (cube_rs == True):
                cube11_hp = cube_hp3
                cube11_x_rd = random.randrange(3, 7, (1))
                cube11_x = random.randrange(1920, 3840, (cube_size))   
                cube11_y = random.randrange(0, 945, (cube_size))
            if (cube12_x <= -cube_size or cube12_hp <= 0) and (cube_rs == True):
                cube12_hp = cube_hp3
                cube12_x_rd = random.randrange(3, 7, (1))
                cube12_x = random.randrange(1920, 3840, (cube_size))   
                cube12_y = random.randrange(0, 945, (cube_size))     

            if (cube13_x <= -cube_size or cube13_hp <= 0) and (cube_rs == True):
                cube13_hp = cube_hp4
                cube13_x_rd = random.randrange(3, 7, (1))
                cube13_x = random.randrange(1920, 3840, (cube_size))   
                cube13_y = random.randrange(0, 945, (cube_size))
            if (cube14_x <= -cube_size or cube14_hp <= 0) and (cube_rs == True):
                cube14_hp = cube_hp4
                cube14_x_rd = random.randrange(3, 7, (1))
                cube14_x = random.randrange(1920, 3840, (cube_size))   
                cube14_y = random.randrange(0, 945, (cube_size))
            if (cube15_x <= -cube_size or cube15_hp <= 0) and (cube_rs == True):
                cube15_hp = cube_hp4
                cube15_x_rd = random.randrange(3, 7, (1))
                cube15_x = random.randrange(1920, 3840, (cube_size))   
                cube15_y = random.randrange(0, 945, (cube_size))
            if (cube16_x <= -cube_size or cube16_hp <= 0) and (cube_rs == True):
                cube16_hp = cube_hp4
                cube16_x_rd = random.randrange(3, 7, (1))
                cube16_x = random.randrange(1920, 3840, (cube_size))   
                cube16_y = random.randrange(0, 945, (cube_size))   
                
            if (cube17_x <= -cube_size or cube17_hp <= 0) and (cube_rs == True):
                cube17_hp = cube_hp5
                cube17_x_rd = random.randrange(3, 7, (1))
                cube17_x = random.randrange(1920, 3840, (cube_size))   
                cube17_y = random.randrange(0, 945, (cube_size))
            if (cube18_x <= -cube_size or cube18_hp <= 0) and (cube_rs == True):
                cube18_hp = cube_hp5
                cube18_x_rd = random.randrange(3, 7, (1))
                cube18_x = random.randrange(1920, 3840, (cube_size))   
                cube18_y = random.randrange(0, 945, (cube_size))
            if (cube19_x <= -cube_size or cube19_hp <= 0) and (cube_rs == True):
                cube19_hp = cube_hp5
                cube19_x_rd = random.randrange(3, 7, (1))
                cube19_x = random.randrange(1920, 3840, (cube_size))   
                cube19_y = random.randrange(0, 945, (cube_size))
            if (cube20_x <= -cube_size or cube20_hp <= 0) and (cube_rs == True):
                cube20_hp = cube_hp5
                cube20_x_rd = random.randrange(3, 7, (1))
                cube20_x = random.randrange(1920, 3840, (cube_size))   
                cube20_y = random.randrange(0, 945, (cube_size)) 
            
        # hitbox cubes to player
        if (hitbox_player[0] in range(cube1_x, (cube1_x + cube_size), 1) or hitbox_player[0] + pl_length in range(cube1_x, (cube1_x + cube_size), 1) or hitbox_player[0] + pl_length/2 in range(cube1_x, (cube1_x + cube_size), 1)) and (hitbox_player[1] in range(cube1_y, (cube1_y + cube_size), 1) or hitbox_player[1] + pl_height in range(cube1_y, (cube1_y + cube_size), 1)): # player get hit
            pl_get_dmg = True
            cube1_hp = 0
        if (hitbox_player[0] in range(cube2_x, (cube2_x + cube_size), 1) or hitbox_player[0] + pl_length in range(cube2_x, (cube2_x + cube_size), 1) or hitbox_player[0] + pl_length/2 in range(cube2_x, (cube2_x + cube_size), 1)) and (hitbox_player[1] in range(cube2_y, (cube2_y + cube_size), 1) or hitbox_player[1] + pl_height in range(cube2_y, (cube2_y + cube_size), 1)): # player get hit
            pl_get_dmg = True
            cube2_hp = 0 
        if (hitbox_player[0] in range(cube3_x, (cube3_x + cube_size), 1) or hitbox_player[0] + pl_length in range(cube3_x, (cube3_x + cube_size), 1) or hitbox_player[0] + pl_length/2 in range(cube3_x, (cube3_x + cube_size), 1)) and (hitbox_player[1] in range(cube3_y, (cube3_y + cube_size), 1) or hitbox_player[1] + pl_height in range(cube3_y, (cube3_y + cube_size), 1)): # player get hit
            pl_get_dmg = True
            cube3_hp = 0 
        if (hitbox_player[0] in range(cube4_x, (cube4_x + cube_size), 1) or hitbox_player[0] + pl_length in range(cube4_x, (cube4_x + cube_size), 1) or hitbox_player[0] + pl_length/2 in range(cube4_x, (cube4_x + cube_size), 1)) and (hitbox_player[1] in range(cube4_y, (cube4_y + cube_size), 1) or hitbox_player[1] + pl_height in range(cube4_y, (cube4_y + cube_size), 1)): # player get hit
            pl_get_dmg = True 
            cube4_hp = 0
            
        if (hitbox_player[0] in range(cube5_x, (cube5_x + cube_size), 1) or hitbox_player[0] + pl_length in range(cube5_x, (cube5_x + cube_size), 1) or hitbox_player[0] + pl_length/2 in range(cube5_x, (cube5_x + cube_size), 1)) and (hitbox_player[1] in range(cube5_y, (cube5_y + cube_size), 1) or hitbox_player[1] + pl_height in range(cube5_y, (cube5_y + cube_size), 1)): # player get hit
            pl_get_dmg = True 
            cube5_hp = 0
        if (hitbox_player[0] in range(cube6_x, (cube6_x + cube_size), 1) or hitbox_player[0] + pl_length in range(cube6_x, (cube6_x + cube_size), 1) or hitbox_player[0] + pl_length/2 in range(cube6_x, (cube6_x + cube_size), 1)) and (hitbox_player[1] in range(cube6_y, (cube6_y + cube_size), 1) or hitbox_player[1] + pl_height in range(cube6_y, (cube6_y + cube_size), 1)): # player get hit
            pl_get_dmg = True 
            cube6_hp = 0
        if (hitbox_player[0] in range(cube7_x, (cube7_x + cube_size), 1) or hitbox_player[0] + pl_length in range(cube7_x, (cube7_x + cube_size), 1) or hitbox_player[0] + pl_length/2 in range(cube7_x, (cube7_x + cube_size), 1)) and (hitbox_player[1] in range(cube7_y, (cube7_y + cube_size), 1) or hitbox_player[1] + pl_height in range(cube7_y, (cube7_y + cube_size), 1)): # player get hit
            pl_get_dmg = True
            cube7_hp = 0 
        if (hitbox_player[0] in range(cube8_x, (cube8_x + cube_size), 1) or hitbox_player[0] + pl_length in range(cube8_x, (cube8_x + cube_size), 1) or hitbox_player[0] + pl_length/2 in range(cube8_x, (cube8_x + cube_size), 1)) and (hitbox_player[1] in range(cube8_y, (cube8_y + cube_size), 1) or hitbox_player[1] + pl_height in range(cube8_y, (cube8_y + cube_size), 1)): # player get hit
            pl_get_dmg = True 
            cube8_hp = 0
            
        if (hitbox_player[0] in range(cube9_x, (cube9_x + cube_size), 1) or hitbox_player[0] + pl_length in range(cube9_x, (cube9_x + cube_size), 1) or hitbox_player[0] + pl_length/2 in range(cube9_x, (cube9_x + cube_size), 1)) and (hitbox_player[1] in range(cube9_y, (cube9_y + cube_size), 1) or hitbox_player[1] + pl_height in range(cube9_y, (cube9_y + cube_size), 1)): # player get hit
            pl_get_dmg = True
            cube9_hp = 0 
        if (hitbox_player[0] in range(cube10_x, (cube10_x + cube_size), 1) or hitbox_player[0] + pl_length in range(cube10_x, (cube10_x + cube_size), 1) or hitbox_player[0] + pl_length/2 in range(cube10_x, (cube10_x + cube_size), 1)) and (hitbox_player[1] in range(cube10_y, (cube10_y + cube_size), 1) or hitbox_player[1] + pl_height in range(cube10_y, (cube10_y + cube_size), 1)): # player get hit
            pl_get_dmg = True 
            cube10_hp = 0
        if (hitbox_player[0] in range(cube11_x, (cube11_x + cube_size), 1) or hitbox_player[0] + pl_length in range(cube11_x, (cube11_x + cube_size), 1) or hitbox_player[0] + pl_length/2 in range(cube11_x, (cube11_x + cube_size), 1)) and (hitbox_player[1] in range(cube11_y, (cube11_y + cube_size), 1) or hitbox_player[1] + pl_height in range(cube11_y, (cube11_y + cube_size), 1)): # player get hit
            pl_get_dmg = True
            cube11_hp = 0 
        if (hitbox_player[0] in range(cube12_x, (cube12_x + cube_size), 1) or hitbox_player[0] + pl_length in range(cube12_x, (cube12_x + cube_size), 1) or hitbox_player[0] + pl_length/2 in range(cube12_x, (cube12_x + cube_size), 1)) and (hitbox_player[1] in range(cube12_y, (cube12_y + cube_size), 1) or hitbox_player[1] + pl_height in range(cube12_y, (cube12_y + cube_size), 1)): # player get hit
            pl_get_dmg = True
            cube12_hp = 0 
            
        if (hitbox_player[0] in range(cube13_x, (cube13_x + cube_size), 1) or hitbox_player[0] + pl_length in range(cube13_x, (cube13_x + cube_size), 1) or hitbox_player[0] + pl_length/2 in range(cube13_x, (cube13_x + cube_size), 1)) and (hitbox_player[1] in range(cube13_y, (cube13_y + cube_size), 1) or hitbox_player[1] + pl_height in range(cube13_y, (cube13_y + cube_size), 1)): # player get hit
            pl_get_dmg = True
            cube13_hp = 0 
        if (hitbox_player[0] in range(cube14_x, (cube14_x + cube_size), 1) or hitbox_player[0] + pl_length in range(cube14_x, (cube14_x + cube_size), 1) or hitbox_player[0] + pl_length/2 in range(cube14_x, (cube14_x + cube_size), 1)) and (hitbox_player[1] in range(cube14_y, (cube14_y + cube_size), 1) or hitbox_player[1] + pl_height in range(cube14_y, (cube14_y + cube_size), 1)): # player get hit
            pl_get_dmg = True 
            cube14_hp = 0
        if (hitbox_player[0] in range(cube15_x, (cube15_x + cube_size), 1) or hitbox_player[0] + pl_length in range(cube15_x, (cube15_x + cube_size), 1) or hitbox_player[0] + pl_length/2 in range(cube15_x, (cube15_x + cube_size), 1)) and (hitbox_player[1] in range(cube15_y, (cube15_y + cube_size), 1) or hitbox_player[1] + pl_height in range(cube15_y, (cube15_y + cube_size), 1)): # player get hit
            pl_get_dmg = True
            cube15_hp = 0
        if (hitbox_player[0] in range(cube16_x, (cube16_x + cube_size), 1) or hitbox_player[0] + pl_length in range(cube16_x, (cube16_x + cube_size), 1) or hitbox_player[0] + pl_length/2 in range(cube16_x, (cube16_x + cube_size), 1)) and (hitbox_player[1] in range(cube16_y, (cube16_y + cube_size), 1) or hitbox_player[1] + pl_height in range(cube16_y, (cube16_y + cube_size), 1)): # player get hit
            pl_get_dmg = True 
            cube16_hp = 0
            
        if (hitbox_player[0] in range(cube17_x, (cube17_x + cube_size), 1) or hitbox_player[0] + pl_length in range(cube17_x, (cube17_x + cube_size), 1) or hitbox_player[0] + pl_length/2 in range(cube17_x, (cube17_x + cube_size), 1)) and (hitbox_player[1] in range(cube17_y, (cube17_y + cube_size), 1) or hitbox_player[1] + pl_height in range(cube17_y, (cube17_y + cube_size), 1)): # player get hit
            pl_get_dmg = True 
            cube17_hp = 0
        if (hitbox_player[0] in range(cube18_x, (cube18_x + cube_size), 1) or hitbox_player[0] + pl_length in range(cube18_x, (cube18_x + cube_size), 1) or hitbox_player[0] + pl_length/2 in range(cube18_x, (8 + cube_size), 1)) and (hitbox_player[1] in range(cube18_y, (cube18_y + cube_size), 1) or hitbox_player[1] + pl_height in range(cube18_y, (cube18_y + cube_size), 1)): # player get hit
            pl_get_dmg = True 
            cube18_hp = 0
        if (hitbox_player[0] in range(cube19_x, (cube19_x + cube_size), 1) or hitbox_player[0] + pl_length in range(cube19_x, (cube19_x + cube_size), 1) or hitbox_player[0] + pl_length/2 in range(cube19_x, (cube19_x + cube_size), 1)) and (hitbox_player[1] in range(cube19_y, (cube19_y + cube_size), 1) or hitbox_player[1] + pl_height in range(cube19_y, (cube19_y + cube_size), 1)): # player get hit
            pl_get_dmg = True 
            cube19_hp = 0
        if (hitbox_player[0] in range(cube20_x, (cube20_x + cube_size), 1) or hitbox_player[0] + pl_length in range(cube20_x, (cube20_x + cube_size), 1) or hitbox_player[0] + pl_length/2 in range(cube20_x, (cube20_x + cube_size), 1)) and (hitbox_player[1] in range(cube20_y, (cube20_y + cube_size), 1) or hitbox_player[1] + pl_height in range(cube20_y, (cube20_y + cube_size), 1)): # player get hit
            pl_get_dmg = True 
            cube20_hp = 0
    
        # hitbox bullet to cube        
        if bullet1_x in range(cube1_x, (cube1_x + cube_size)) and bullet1_y in range(cube1_y, (cube1_y + cube_size), 1): # rd cubes get shot
            bullet1_fly = False
            Bullet1_x = -100
            bullet1_y = -100
            cube1_hp -= 1
        if bullet2_x in range(cube1_x, (cube1_x + cube_size)) and bullet2_y in range(cube1_y, (cube1_y + cube_size), 1): # rd cubes get shot
            bullet2_fly = False
            Bullet2_x = -100
            bullet2_y = -100
            cube1_hp -= 1
        if bullet3_x in range(cube1_x, (cube1_x + cube_size)) and bullet3_y in range(cube1_y, (cube1_y + cube_size), 1): # rd cubes get shot
            bullet3_fly = False
            Bullet3_x = -100
            bullet3_y = -100
            cube1_hp -= 1
        if bullet4_x in range(cube1_x, (cube1_x + cube_size)) and bullet4_y in range(cube1_y, (cube1_y + cube_size), 1): # rd cubes get shot
            bullet4_fly = False
            Bullet4_x = -100
            bullet4_y = -100
            cube1_hp -= 1
        if bullet5_x in range(cube1_x, (cube1_x + cube_size)) and bullet5_y in range(cube1_y, (cube1_y + cube_size), 1): # rd cubes get shot
            bullet5_fly = False
            Bullet5_x = -100
            bullet5_y = -100
            cube1_hp -= 1
        if bullet6_x in range(cube1_x, (cube1_x + cube_size)) and bullet6_y in range(cube1_y, (cube1_y + cube_size), 1): # rd cubes get shot
            bullet6_fly = False
            Bullet6_x = -100
            bullet6_y = -100
            cube1_hp -= 1
        if bullet7_x in range(cube1_x, (cube1_x + cube_size)) and bullet7_y in range(cube1_y, (cube1_y + cube_size), 1): # rd cubes get shot
            bullet7_fly = False
            Bullet7_x = -100
            bullet7_y = -100
            cube1_hp -= 1
        if bullet8_x in range(cube1_x, (cube1_x + cube_size)) and bullet8_y in range(cube1_y, (cube1_y + cube_size), 1): # rd cubes get shot
            bullet8_fly = False
            Bullet8_x = -100
            bullet8_y = -100
            cube1_hp -= 1
        if bullet9_x in range(cube1_x, (cube1_x + cube_size)) and bullet9_y in range(cube1_y, (cube1_y + cube_size), 1): # rd cubes get shot
            bullet9_fly = False
            Bullet9_x = -100
            bullet9_y = -100
            cube1_hp -= 1
        if bullet10_x in range(cube1_x, (cube1_x + cube_size)) and bullet10_y in range(cube1_y, (cube1_y + cube_size), 1): # rd cubes get shot
            bullet10_fly = False
            Bullet10_x = -100
            bullet10_y = -100
            cube1_hp -= 1
        
        if bullet1_x in range(cube2_x, (cube2_x + cube_size)) and bullet1_y in range(cube2_y, (cube2_y + cube_size), 1): # rd cubes get shot
            bullet1_fly = False
            Bullet1_x = -100
            bullet1_y = -100
            cube2_hp -= 1
        if bullet2_x in range(cube2_x, (cube2_x + cube_size)) and bullet2_y in range(cube2_y, (cube2_y + cube_size), 1): # rd cubes get shot
            bullet2_fly = False
            Bullet2_x = -100
            bullet2_y = -100
            cube2_hp -= 1
        if bullet3_x in range(cube2_x, (cube2_x + cube_size)) and bullet3_y in range(cube2_y, (cube2_y + cube_size), 1): # rd cubes get shot
            bullet3_fly = False
            Bullet3_x = -100
            bullet3_y = -100
            cube2_hp -= 1
        if bullet4_x in range(cube2_x, (cube2_x + cube_size)) and bullet4_y in range(cube2_y, (cube2_y + cube_size), 1): # rd cubes get shot
            bullet4_fly = False
            Bullet4_x = -100
            bullet4_y = -100
            cube2_hp -= 1
        if bullet5_x in range(cube2_x, (cube2_x + cube_size)) and bullet5_y in range(cube2_y, (cube2_y + cube_size), 1): # rd cubes get shot
            bullet5_fly = False
            Bullet5_x = -100
            bullet5_y = -100
            cube2_hp -= 1
        if bullet6_x in range(cube2_x, (cube2_x + cube_size)) and bullet6_y in range(cube2_y, (cube2_y + cube_size), 1): # rd cubes get shot
            bullet6_fly = False
            Bullet6_x = -100
            bullet6_y = -100
            cube2_hp -= 1
        if bullet7_x in range(cube2_x, (cube2_x + cube_size)) and bullet7_y in range(cube2_y, (cube2_y + cube_size), 1): # rd cubes get shot
            bullet7_fly = False
            Bullet7_x = -100
            bullet7_y = -100
            cube2_hp -= 1
        if bullet8_x in range(cube2_x, (cube2_x + cube_size)) and bullet8_y in range(cube2_y, (cube2_y + cube_size), 1): # rd cubes get shot
            bullet8_fly = False
            Bullet8_x = -100
            bullet8_y = -100
            cube2_hp -= 1
        if bullet9_x in range(cube2_x, (cube2_x + cube_size)) and bullet9_y in range(cube2_y, (cube2_y + cube_size), 1): # rd cubes get shot
            bullet9_fly = False
            Bullet9_x = -100
            bullet9_y = -100
            cube2_hp -= 1
        if bullet10_x in range(cube2_x, (cube2_x + cube_size)) and bullet10_y in range(cube2_y, (cube2_y + cube_size), 1): # rd cubes get shot
            bullet10_fly = False
            Bullet10_x = -100
            bullet10_y = -100
            cube2_hp -= 1
        
        if bullet1_x in range(cube3_x, (cube3_x + cube_size)) and bullet1_y in range(cube3_y, (cube3_y + cube_size), 1): # rd cubes get shot
            bullet1_fly = False
            Bullet1_x = -100
            bullet1_y = -100
            cube3_hp -= 1
        if bullet2_x in range(cube3_x, (cube3_x + cube_size)) and bullet2_y in range(cube3_y, (cube3_y + cube_size), 1): # rd cubes get shot
            bullet2_fly = False
            Bullet2_x = -100
            bullet2_y = -100
            cube3_hp -= 1
        if bullet3_x in range(cube3_x, (cube3_x + cube_size)) and bullet3_y in range(cube3_y, (cube3_y + cube_size), 1): # rd cubes get shot
            bullet3_fly = False
            Bullet3_x = -100
            bullet3_y = -100
            cube3_hp -= 1
        if bullet4_x in range(cube3_x, (cube3_x + cube_size)) and bullet4_y in range(cube3_y, (cube3_y + cube_size), 1): # rd cubes get shot
            bullet4_fly = False
            Bullet4_x = -100
            bullet4_y = -100
            cube3_hp -= 1
        if bullet5_x in range(cube3_x, (cube3_x + cube_size)) and bullet5_y in range(cube3_y, (cube3_y + cube_size), 1): # rd cubes get shot
            bullet5_fly = False
            Bullet5_x = -100
            bullet5_y = -100
            cube3_hp -= 1
        if bullet6_x in range(cube3_x, (cube3_x + cube_size)) and bullet6_y in range(cube3_y, (cube3_y + cube_size), 1): # rd cubes get shot
            bullet6_fly = False
            Bullet6_x = -100
            bullet6_y = -100
            cube3_hp -= 1
        if bullet7_x in range(cube3_x, (cube3_x + cube_size)) and bullet7_y in range(cube3_y, (cube3_y + cube_size), 1): # rd cubes get shot
            bullet7_fly = False
            Bullet7_x = -100
            bullet7_y = -100
            cube3_hp -= 1
        if bullet8_x in range(cube3_x, (cube3_x + cube_size)) and bullet8_y in range(cube3_y, (cube3_y + cube_size), 1): # rd cubes get shot
            bullet8_fly = False
            Bullet8_x = -100
            bullet8_y = -100
            cube3_hp -= 1
        if bullet9_x in range(cube3_x, (cube3_x + cube_size)) and bullet9_y in range(cube3_y, (cube3_y + cube_size), 1): # rd cubes get shot
            bullet9_fly = False
            Bullet9_x = -100
            bullet9_y = -100
            cube3_hp -= 1
        if bullet10_x in range(cube3_x, (cube3_x + cube_size)) and bullet10_y in range(cube3_y, (cube3_y + cube_size), 1): # rd cubes get shot
            bullet10_fly = False
            Bullet10_x = -100
            bullet10_y = -100
            cube3_hp -= 1
        
        if bullet1_x in range(cube4_x, (cube4_x + cube_size)) and bullet1_y in range(cube4_y, (cube4_y + cube_size), 1): # rd cubes get shot
            bullet1_fly = False
            Bullet1_x = -100
            bullet1_y = -100
            cube4_hp -= 1
        if bullet2_x in range(cube4_x, (cube4_x + cube_size)) and bullet2_y in range(cube4_y, (cube4_y + cube_size), 1): # rd cubes get shot
            bullet2_fly = False
            Bullet2_x = -100
            bullet2_y = -100
            cube4_hp -= 1
        if bullet3_x in range(cube4_x, (cube4_x + cube_size)) and bullet3_y in range(cube4_y, (cube4_y + cube_size), 1): # rd cubes get shot
            bullet3_fly = False
            Bullet3_x = -100
            bullet3_y = -100
            cube4_hp -= 1
        if bullet4_x in range(cube4_x, (cube4_x + cube_size)) and bullet4_y in range(cube4_y, (cube4_y + cube_size), 1): # rd cubes get shot
            bullet4_fly = False
            Bullet4_x = -100
            bullet4_y = -100
            cube4_hp -= 1
        if bullet5_x in range(cube4_x, (cube4_x + cube_size)) and bullet5_y in range(cube4_y, (cube4_y + cube_size), 1): # rd cubes get shot
            bullet5_fly = False
            Bullet5_x = -100
            bullet5_y = -100
            cube4_hp -= 1
        if bullet6_x in range(cube4_x, (cube4_x + cube_size)) and bullet6_y in range(cube4_y, (cube4_y + cube_size), 1): # rd cubes get shot
            bullet6_fly = False
            Bullet6_x = -100
            bullet6_y = -100
            cube4_hp -= 1
        if bullet7_x in range(cube4_x, (cube4_x + cube_size)) and bullet7_y in range(cube4_y, (cube4_y + cube_size), 1): # rd cubes get shot
            bullet7_fly = False
            Bullet7_x = -100
            bullet7_y = -100
            cube4_hp -= 1
        if bullet8_x in range(cube4_x, (cube4_x + cube_size)) and bullet8_y in range(cube4_y, (cube4_y + cube_size), 1): # rd cubes get shot
            bullet8_fly = False
            Bullet8_x = -100
            bullet8_y = -100
            cube4_hp -= 1
        if bullet9_x in range(cube4_x, (cube4_x + cube_size)) and bullet9_y in range(cube4_y, (cube4_y + cube_size), 1): # rd cubes get shot
            bullet9_fly = False
            Bullet9_x = -100
            bullet9_y = -100
            cube4_hp -= 1
        if bullet10_x in range(cube4_x, (cube4_x + cube_size)) and bullet10_y in range(cube4_y, (cube4_y + cube_size), 1): # rd cubes get shot
            bullet10_fly = False
            Bullet10_x = -100
            bullet10_y = -100
            cube4_hp -= 1
        
        if bullet1_x in range(cube5_x, (cube5_x + cube_size)) and bullet1_y in range(cube5_y, (cube5_y + cube_size), 1): # rd cubes get shot
            bullet1_fly = False
            Bullet1_x = -100
            bullet1_y = -100
            cube5_hp -= 1
        if bullet2_x in range(cube5_x, (cube5_x + cube_size)) and bullet2_y in range(cube5_y, (cube5_y + cube_size), 1): # rd cubes get shot
            bullet2_fly = False
            Bullet2_x = -100
            bullet2_y = -100
            cube5_hp -= 1
        if bullet3_x in range(cube5_x, (cube5_x + cube_size)) and bullet3_y in range(cube5_y, (cube5_y + cube_size), 1): # rd cubes get shot
            bullet3_fly = False
            Bullet3_x = -100
            bullet3_y = -100
            cube5_hp -= 1
        if bullet4_x in range(cube5_x, (cube5_x + cube_size)) and bullet4_y in range(cube5_y, (cube5_y + cube_size), 1): # rd cubes get shot
            bullet4_fly = False
            Bullet4_x = -100
            bullet4_y = -100
            cube5_hp -= 1
        if bullet5_x in range(cube5_x, (cube5_x + cube_size)) and bullet5_y in range(cube5_y, (cube5_y + cube_size), 1): # rd cubes get shot
            bullet5_fly = False
            Bullet5_x = -100
            bullet5_y = -100
            cube5_hp -= 1
        if bullet6_x in range(cube5_x, (cube5_x + cube_size)) and bullet6_y in range(cube5_y, (cube5_y + cube_size), 1): # rd cubes get shot
            bullet6_fly = False
            Bullet6_x = -100
            Bullet6_y = -100
            cube5_hp -= 1
        if bullet7_x in range(cube5_x, (cube5_x + cube_size)) and bullet7_y in range(cube5_y, (cube5_y + cube_size), 1): # rd cubes get shot
            bullet7_fly = False
            Bullet7_x = -100
            bullet7_y = -100
            cube5_hp -= 1
        if bullet8_x in range(cube5_x, (cube5_x + cube_size)) and bullet8_y in range(cube5_y, (cube5_y + cube_size), 1): # rd cubes get shot
            bullet8_fly = False
            Bullet8_x = -100
            bullet8_y = -100
            cube5_hp -= 1
        if bullet9_x in range(cube5_x, (cube5_x + cube_size)) and bullet9_y in range(cube5_y, (cube5_y + cube_size), 1): # rd cubes get shot
            bullet9_fly = False
            Bullet9_x = -100
            bullet9_y = -100
            cube5_hp -= 1
        if bullet10_x in range(cube5_x, (cube5_x + cube_size)) and bullet10_y in range(cube5_y, (cube5_y + cube_size), 1): # rd cubes get shot
            bullet10_fly = False
            Bullet10_x = -100
            bullet10_y = -100
            cube5_hp -= 1
        
        if bullet1_x in range(cube6_x, (cube6_x + cube_size)) and bullet1_y in range(cube6_y, (cube6_y + cube_size), 1): # rd cubes get shot
            bullet1_fly = False
            Bullet1_x = -100
            bullet1_y = -100
            cube6_hp -= 1
        if bullet2_x in range(cube6_x, (cube6_x + cube_size)) and bullet2_y in range(cube6_y, (cube6_y + cube_size), 1): # rd cubes get shot
            bullet2_fly = False
            Bullet2_x = -100
            bullet2_y = -100
            cube6_hp -= 1
        if bullet3_x in range(cube6_x, (cube6_x + cube_size)) and bullet3_y in range(cube6_y, (cube6_y + cube_size), 1): # rd cubes get shot
            bullet3_fly = False
            Bullet3_x = -100
            bullet3_y = -100
            cube6_hp -= 1
        if bullet4_x in range(cube6_x, (cube6_x + cube_size)) and bullet4_y in range(cube6_y, (cube6_y + cube_size), 1): # rd cubes get shot
            bullet4_fly = False
            Bullet4_x = -100
            bullet4_y = -100
            cube6_hp -= 1
        if bullet5_x in range(cube6_x, (cube6_x + cube_size)) and bullet5_y in range(cube6_y, (cube6_y + cube_size), 1): # rd cubes get shot
            bullet5_fly = False
            Bullet5_x = -100
            bullet5_y = -100
            cube6_hp -= 1
        if bullet6_x in range(cube6_x, (cube6_x + cube_size)) and bullet6_y in range(cube6_y, (cube6_y + cube_size), 1): # rd cubes get shot
            bullet6_fly = False
            Bullet6_x = -100
            bullet6_y = -100
            cube6_hp -= 1
        if bullet7_x in range(cube6_x, (cube6_x + cube_size)) and bullet7_y in range(cube6_y, (cube6_y + cube_size), 1): # rd cubes get shot
            bullet7_fly = False
            Bullet7_x = -100
            bullet7_y = -100
            cube6_hp -= 1
        if bullet8_x in range(cube6_x, (cube6_x + cube_size)) and bullet8_y in range(cube6_y, (cube6_y + cube_size), 1): # rd cubes get shot
            bullet8_fly = False
            Bullet8_x = -100
            bullet8_y = -100
            cube6_hp -= 1
        if bullet9_x in range(cube6_x, (cube6_x + cube_size)) and bullet9_y in range(cube6_y, (cube6_y + cube_size), 1): # rd cubes get shot
            bullet9_fly = False
            Bullet9_x = -100
            bullet9_y = -100
            cube6_hp -= 1
        if bullet10_x in range(cube6_x, (cube6_x + cube_size)) and bullet10_y in range(cube6_y, (cube6_y + cube_size), 1): # rd cubes get shot
            bullet10_fly = False
            Bullet10_x = -100
            bullet10_y = -100
            cube6_hp -= 1
        
        if bullet1_x in range(cube7_x, (cube7_x + cube_size)) and bullet1_y in range(cube7_y, (cube7_y + cube_size), 1): # rd cubes get shot
            bullet1_fly = False
            Bullet1_x = -100
            bullet1_y = -100
            cube7_hp -= 1
        if bullet2_x in range(cube7_x, (cube7_x + cube_size)) and bullet2_y in range(cube7_y, (cube7_y + cube_size), 1): # rd cubes get shot
            bullet2_fly = False
            Bullet2_x = -100
            bullet2_y = -100
            cube7_hp -= 1
        if bullet3_x in range(cube7_x, (cube7_x + cube_size)) and bullet3_y in range(cube7_y, (cube7_y + cube_size), 1): # rd cubes get shot
            bullet3_fly = False
            Bullet3_x = -100
            bullet3_y = -100
            cube7_hp -= 1
        if bullet4_x in range(cube7_x, (cube7_x + cube_size)) and bullet4_y in range(cube7_y, (cube7_y + cube_size), 1): # rd cubes get shot
            bullet4_fly = False
            Bullet4_x = -100
            bullet4_y = -100
            cube7_hp -= 1
        if bullet5_x in range(cube7_x, (cube7_x + cube_size)) and bullet5_y in range(cube7_y, (cube7_y + cube_size), 1): # rd cubes get shot
            bullet5_fly = False
            Bullet5_x = -100
            bullet5_y = -100
            cube7_hp -= 1
        if bullet6_x in range(cube7_x, (cube7_x + cube_size)) and bullet6_y in range(cube7_y, (cube7_y + cube_size), 1): # rd cubes get shot
            bullet6_fly = False
            Bullet6_x = -100
            bullet6_y = -100
            cube7_hp -= 1
        if bullet7_x in range(cube7_x, (cube7_x + cube_size)) and bullet7_y in range(cube7_y, (cube7_y + cube_size), 1): # rd cubes get shot
            bullet7_fly = False
            Bullet7_x = -100
            bullet7_y = -100
            cube7_hp -= 1
        if bullet8_x in range(cube7_x, (cube7_x + cube_size)) and bullet8_y in range(cube7_y, (cube7_y + cube_size), 1): # rd cubes get shot
            bullet8_fly = False
            Bullet8_x = -100
            bullet8_y = -100
            cube7_hp -= 1
        if bullet9_x in range(cube7_x, (cube7_x + cube_size)) and bullet9_y in range(cube7_y, (cube7_y + cube_size), 1): # rd cubes get shot
            bullet9_fly = False
            Bullet9_x = -100
            bullet9_y = -100
            cube7_hp -= 1
        if bullet10_x in range(cube7_x, (cube7_x + cube_size)) and bullet10_y in range(cube7_y, (cube7_y + cube_size), 1): # rd cubes get shot
            bullet10_fly = False
            Bullet10_x = -100
            bullet10_y = -100
            cube7_hp -= 1
        
        if bullet1_x in range(cube8_x, (cube8_x + cube_size)) and bullet1_y in range(cube8_y, (cube8_y + cube_size), 1): # rd cubes get shot
            bullet1_fly = False
            Bullet1_x = -100
            bullet1_y = -100
            cube8_hp -= 1
        if bullet2_x in range(cube8_x, (cube8_x + cube_size)) and bullet2_y in range(cube8_y, (cube8_y + cube_size), 1): # rd cubes get shot
            bullet2_fly = False
            Bullet2_x = -100
            bullet2_y = -100
            cube8_hp -= 1
        if bullet3_x in range(cube8_x, (cube8_x + cube_size)) and bullet3_y in range(cube8_y, (cube8_y + cube_size), 1): # rd cubes get shot
            bullet3_fly = False
            Bullet3_x = -100
            bullet3_y = -100
            cube8_hp -= 1
        if bullet4_x in range(cube8_x, (cube8_x + cube_size)) and bullet4_y in range(cube8_y, (cube8_y + cube_size), 1): # rd cubes get shot
            bullet4_fly = False
            Bullet4_x = -100
            bullet4_y = -100
            cube8_hp -= 1
        if bullet5_x in range(cube8_x, (cube8_x + cube_size)) and bullet5_y in range(cube8_y, (cube8_y + cube_size), 1): # rd cubes get shot
            bullet5_fly = False
            Bullet5_x = -100
            bullet5_y = -100
            cube8_hp -= 1
        if bullet6_x in range(cube8_x, (cube8_x + cube_size)) and bullet6_y in range(cube8_y, (cube8_y + cube_size), 1): # rd cubes get shot
            bullet6_fly = False
            Bullet6_x = -100
            bullet6_y = -100
            cube8_hp -= 1
        if bullet7_x in range(cube8_x, (cube8_x + cube_size)) and bullet7_y in range(cube8_y, (cube8_y + cube_size), 1): # rd cubes get shot
            bullet7_fly = False
            Bullet7_x = -100
            bullet7_y = -100
            cube8_hp -= 1
        if bullet8_x in range(cube8_x, (cube8_x + cube_size)) and bullet8_y in range(cube8_y, (cube8_y + cube_size), 1): # rd cubes get shot
            bullet8_fly = False
            Bullet8_x = -100
            bullet8_y = -100
            cube8_hp -= 1
        if bullet9_x in range(cube8_x, (cube8_x + cube_size)) and bullet9_y in range(cube8_y, (cube8_y + cube_size), 1): # rd cubes get shot
            bullet9_fly = False
            Bullet9_x = -100
            bullet9_y = -100
            cube8_hp -= 1
        if bullet10_x in range(cube8_x, (cube8_x + cube_size)) and bullet10_y in range(cube8_y, (cube8_y + cube_size), 1): # rd cubes get shot
            bullet10_fly = False
            Bullet10_x = -100
            bullet10_y = -100
            cube8_hp -= 1
            
        if bullet1_x in range(cube9_x, (cube9_x + cube_size)) and bullet1_y in range(cube9_y, (cube9_y + cube_size), 1): # rd cubes get shot
            bullet1_fly = False
            Bullet1_x = -100
            bullet1_y = -100
            cube9_hp -= 1
        if bullet2_x in range(cube9_x, (cube9_x + cube_size)) and bullet2_y in range(cube9_y, (cube9_y + cube_size), 1): # rd cubes get shot
            bullet2_fly = False
            Bullet2_x = -100
            bullet2_y = -100
            cube9_hp -= 1
        if bullet3_x in range(cube9_x, (cube9_x + cube_size)) and bullet3_y in range(cube9_y, (cube9_y + cube_size), 1): # rd cubes get shot
            bullet3_fly = False
            Bullet3_x = -100
            bullet3_y = -100
            cube9_hp -= 1
        if bullet4_x in range(cube9_x, (cube9_x + cube_size)) and bullet4_y in range(cube9_y, (cube9_y + cube_size), 1): # rd cubes get shot
            bullet4_fly = False
            Bullet4_x = -100
            bullet4_y = -100
            cube9_hp -= 1
        if bullet5_x in range(cube9_x, (cube9_x + cube_size)) and bullet5_y in range(cube9_y, (cube9_y + cube_size), 1): # rd cubes get shot
            bullet5_fly = False
            Bullet5_x = -100
            bullet5_y = -100
            cube9_hp -= 1
        if bullet6_x in range(cube9_x, (cube9_x + cube_size)) and bullet6_y in range(cube9_y, (cube9_y + cube_size), 1): # rd cubes get shot
            bullet6_fly = False
            Bullet6_x = -100
            bullet6_y = -100
            cube9_hp -= 1
        if bullet7_x in range(cube9_x, (cube9_x + cube_size)) and bullet7_y in range(cube9_y, (cube9_y + cube_size), 1): # rd cubes get shot
            bullet7_fly = False
            Bullet7_x = -100
            bullet7_y = -100
            cube9_hp -= 1
        if bullet8_x in range(cube9_x, (cube9_x + cube_size)) and bullet8_y in range(cube9_y, (cube9_y + cube_size), 1): # rd cubes get shot
            bullet8_fly = False
            Bullet8_x = -100
            bullet8_y = -100
            cube9_hp -= 1
        if bullet9_x in range(cube9_x, (cube9_x + cube_size)) and bullet9_y in range(cube9_y, (cube9_y + cube_size), 1): # rd cubes get shot
            bullet9_fly = False
            Bullet9_x = -100
            bullet9_y = -100
            cube9_hp -= 1
        if bullet10_x in range(cube9_x, (cube9_x + cube_size)) and bullet10_y in range(cube9_y, (cube9_y + cube_size), 1): # rd cubes get shot
            bullet10_fly = False
            Bullet10_x = -100
            bullet10_y = -100
            cube9_hp -= 1
            
        if bullet1_x in range(cube10_x, (cube10_x + cube_size)) and bullet1_y in range(cube10_y, (cube10_y + cube_size), 1): # rd cubes get shot
            bullet1_fly = False
            Bullet1_x = -100
            bullet1_y = -100
            cube10_hp -= 1
        if bullet2_x in range(cube10_x, (cube10_x + cube_size)) and bullet2_y in range(cube10_y, (cube10_y + cube_size), 1): # rd cubes get shot
            bullet2_fly = False
            Bullet2_x = -100
            bullet2_y = -100
            cube10_hp -= 1
        if bullet3_x in range(cube10_x, (cube10_x + cube_size)) and bullet3_y in range(cube10_y, (cube10_y + cube_size), 1): # rd cubes get shot
            bullet3_fly = False
            Bullet3_x = -100
            bullet3_y = -100
            cube10_hp -= 1
        if bullet4_x in range(cube10_x, (cube10_x + cube_size)) and bullet4_y in range(cube10_y, (cube10_y + cube_size), 1): # rd cubes get shot
            bullet4_fly = False
            Bullet4_x = -100
            bullet4_y = -100
            cube10_hp -= 1
        if bullet5_x in range(cube10_x, (cube10_x + cube_size)) and bullet5_y in range(cube10_y, (cube10_y + cube_size), 1): # rd cubes get shot
            bullet5_fly = False
            Bullet5_x = -100
            bullet5_y = -100
            cube10_hp -= 1
        if bullet6_x in range(cube10_x, (cube10_x + cube_size)) and bullet6_y in range(cube10_y, (cube10_y + cube_size), 1): # rd cubes get shot
            bullet6_fly = False
            Bullet6_x = -100
            bullet6_y = -100
            cube10_hp -= 1
        if bullet7_x in range(cube10_x, (cube10_x + cube_size)) and bullet7_y in range(cube10_y, (cube10_y + cube_size), 1): # rd cubes get shot
            bullet7_fly = False
            Bullet7_x = -100
            bullet7_y = -100
            cube10_hp -= 1
        if bullet8_x in range(cube10_x, (cube10_x + cube_size)) and bullet8_y in range(cube10_y, (cube10_y + cube_size), 1): # rd cubes get shot
            bullet8_fly = False
            Bullet8_x = -100
            bullet8_y = -100
            cube10_hp -= 1
        if bullet9_x in range(cube10_x, (cube10_x + cube_size)) and bullet9_y in range(cube10_y, (cube10_y + cube_size), 1): # rd cubes get shot
            bullet9_fly = False
            Bullet9_x = -100
            bullet9_y = -100
            cube10_hp -= 1
        if bullet10_x in range(cube10_x, (cube10_x + cube_size)) and bullet10_y in range(cube10_y, (cube10_y + cube_size), 1): # rd cubes get shot
            bullet10_fly = False
            Bullet10_x = -100
            bullet10_y = -100
            cube10_hp -= 1
        
        if bullet1_x in range(cube11_x, (cube11_x + cube_size)) and bullet1_y in range(cube11_y, (cube11_y + cube_size), 1): # rd cubes get shot
            bullet1_fly = False
            Bullet1_x = -100
            bullet1_y = -100
            cube11_hp -= 1
        if bullet2_x in range(cube11_x, (cube11_x + cube_size)) and bullet2_y in range(cube11_y, (cube11_y + cube_size), 1): # rd cubes get shot
            bullet2_fly = False
            Bullet2_x = -100
            bullet2_y = -100
            cube11_hp -= 1
        if bullet3_x in range(cube11_x, (cube11_x + cube_size)) and bullet3_y in range(cube11_y, (cube11_y + cube_size), 1): # rd cubes get shot
            bullet3_fly = False
            Bullet3_x = -100
            bullet3_y = -100
            cube11_hp -= 1
        if bullet4_x in range(cube11_x, (cube11_x + cube_size)) and bullet4_y in range(cube11_y, (cube11_y + cube_size), 1): # rd cubes get shot
            bullet4_fly = False
            Bullet4_x = -100
            bullet4_y = -100
            cube11_hp -= 1
        if bullet5_x in range(cube11_x, (cube11_x + cube_size)) and bullet5_y in range(cube11_y, (cube11_y + cube_size), 1): # rd cubes get shot
            bullet5_fly = False
            Bullet5_x = -100
            bullet5_y = -100
            cube11_hp -= 1
        if bullet6_x in range(cube11_x, (cube11_x + cube_size)) and bullet6_y in range(cube11_y, (cube11_y + cube_size), 1): # rd cubes get shot
            bullet6_fly = False
            Bullet6_x = -100
            bullet6_y = -100
            cube11_hp -= 1
        if bullet7_x in range(cube11_x, (cube11_x + cube_size)) and bullet7_y in range(cube11_y, (cube11_y + cube_size), 1): # rd cubes get shot
            bullet7_fly = False
            Bullet7_x = -100
            bullet7_y = -100
            cube11_hp -= 1
        if bullet8_x in range(cube11_x, (cube11_x + cube_size)) and bullet8_y in range(cube11_y, (cube11_y + cube_size), 1): # rd cubes get shot
            bullet8_fly = False
            Bullet8_x = -100
            bullet8_y = -100
            cube11_hp -= 1
        if bullet9_x in range(cube11_x, (cube11_x + cube_size)) and bullet9_y in range(cube11_y, (cube11_y + cube_size), 1): # rd cubes get shot
            bullet9_fly = False
            Bullet9_x = -100
            bullet9_y = -100
            cube11_hp -= 1
        if bullet10_x in range(cube11_x, (cube11_x + cube_size)) and bullet10_y in range(cube11_y, (cube11_y + cube_size), 1): # rd cubes get shot
            bullet10_fly = False
            Bullet10_x = -100
            bullet10_y = -100
            cube11_hp -= 1
        
        
        if bullet1_x in range(cube12_x, (cube12_x + cube_size)) and bullet1_y in range(cube12_y, (cube12_y + cube_size), 1): # rd cubes get shot
            bullet1_fly = False
            Bullet1_x = -100
            bullet1_y = -100
            cube12_hp -= 1
        if bullet2_x in range(cube12_x, (cube12_x + cube_size)) and bullet2_y in range(cube12_y, (cube12_y + cube_size), 1): # rd cubes get shot
            bullet2_fly = False
            Bullet2_x = -100
            bullet2_y = -100
            cube12_hp -= 1
        if bullet3_x in range(cube12_x, (cube12_x + cube_size)) and bullet3_y in range(cube12_y, (cube12_y + cube_size), 1): # rd cubes get shot
            bullet3_fly = False
            Bullet3_x = -100
            bullet3_y = -100
            cube12_hp -= 1
        if bullet4_x in range(cube12_x, (cube12_x + cube_size)) and bullet4_y in range(cube12_y, (cube12_y + cube_size), 1): # rd cubes get shot
            bullet4_fly = False
            Bullet4_x = -100
            bullet4_y = -100
            cube12_hp -= 1
        if bullet5_x in range(cube12_x, (cube12_x + cube_size)) and bullet5_y in range(cube12_y, (cube12_y + cube_size), 1): # rd cubes get shot
            bullet5_fly = False
            Bullet5_x = -100
            bullet5_y = -100
            cube12_hp -= 1
        if bullet6_x in range(cube12_x, (cube12_x + cube_size)) and bullet6_y in range(cube12_y, (cube12_y + cube_size), 1): # rd cubes get shot
            bullet6_fly = False
            Bullet6_x = -100
            bullet6_y = -100
            cube12_hp -= 1
        if bullet7_x in range(cube12_x, (cube12_x + cube_size)) and bullet7_y in range(cube12_y, (cube12_y + cube_size), 1): # rd cubes get shot
            bullet7_fly = False
            Bullet7_x = -100
            bullet7_y = -100
            cube12_hp -= 1
        if bullet8_x in range(cube12_x, (cube12_x + cube_size)) and bullet8_y in range(cube12_y, (cube12_y + cube_size), 1): # rd cubes get shot
            bullet8_fly = False
            Bullet8_x = -100
            bullet8_y = -100
            cube12_hp -= 1
        if bullet9_x in range(cube12_x, (cube12_x + cube_size)) and bullet9_y in range(cube12_y, (cube12_y + cube_size), 1): # rd cubes get shot
            bullet9_fly = False
            Bullet9_x = -100
            bullet9_y = -100
            cube12_hp -= 1
        if bullet10_x in range(cube12_x, (cube12_x + cube_size)) and bullet10_y in range(cube12_y, (cube12_y + cube_size), 1): # rd cubes get shot
            bullet10_fly = False
            Bullet10_x = -100
            bullet10_y = -100
            cube12_hp -= 1
        
        if bullet1_x in range(cube13_x, (cube13_x + cube_size)) and bullet1_y in range(cube13_y, (cube13_y + cube_size), 1): # rd cubes get shot
            bullet1_fly = False
            Bullet1_x = -100
            bullet1_y = -100
            cube13_hp -= 1
        if bullet2_x in range(cube13_x, (cube13_x + cube_size)) and bullet2_y in range(cube13_y, (cube13_y + cube_size), 1): # rd cubes get shot
            bullet2_fly = False
            Bullet2_x = -100
            bullet2_y = -100
            cube13_hp -= 1
        if bullet3_x in range(cube13_x, (cube13_x + cube_size)) and bullet3_y in range(cube13_y, (cube13_y + cube_size), 1): # rd cubes get shot
            bullet3_fly = False
            Bullet3_x = -100
            bullet3_y = -100
            cube13_hp -= 1
        if bullet4_x in range(cube13_x, (cube13_x + cube_size)) and bullet4_y in range(cube13_y, (cube13_y + cube_size), 1): # rd cubes get shot
            bullet4_fly = False
            Bullet4_x = -100
            bullet4_y = -100
            cube13_hp -= 1
        if bullet5_x in range(cube13_x, (cube13_x + cube_size)) and bullet5_y in range(cube13_y, (cube13_y + cube_size), 1): # rd cubes get shot
            bullet5_fly = False
            Bullet5_x = -100
            bullet5_y = -100
            cube13_hp -= 1
        if bullet6_x in range(cube13_x, (cube13_x + cube_size)) and bullet6_y in range(cube13_y, (cube13_y + cube_size), 1): # rd cubes get shot
            bullet6_fly = False
            Bullet6_x = -100
            bullet6_y = -100
            cube13_hp -= 1
        if bullet7_x in range(cube13_x, (cube13_x + cube_size)) and bullet7_y in range(cube13_y, (cube13_y + cube_size), 1): # rd cubes get shot
            bullet7_fly = False
            Bullet7_x = -100
            bullet7_y = -100
            cube13_hp -= 1
        if bullet8_x in range(cube13_x, (cube13_x + cube_size)) and bullet8_y in range(cube13_y, (cube13_y + cube_size), 1): # rd cubes get shot
            bullet8_fly = False
            Bullet8_x = -100
            bullet8_y = -100
            cube13_hp -= 1
        if bullet9_x in range(cube13_x, (cube13_x + cube_size)) and bullet9_y in range(cube13_y, (cube13_y + cube_size), 1): # rd cubes get shot
            bullet9_fly = False
            Bullet9_x = -100
            bullet9_y = -100
            cube13_hp -= 1
        if bullet10_x in range(cube13_x, (cube13_x + cube_size)) and bullet10_y in range(cube13_y, (cube13_y + cube_size), 1): # rd cubes get shot
            bullet10_fly = False
            Bullet10_x = -100
            bullet10_y = -100
            cube13_hp -= 1
        
        if bullet1_x in range(cube14_x, (cube14_x + cube_size)) and bullet1_y in range(cube14_y, (cube14_y + cube_size), 1): # rd cubes get shot
            bullet1_fly = False
            Bullet1_x = -100
            bullet1_y = -100
            cube14_hp -= 1
        if bullet2_x in range(cube14_x, (cube14_x + cube_size)) and bullet2_y in range(cube14_y, (cube14_y + cube_size), 1): # rd cubes get shot
            bullet2_fly = False
            Bullet2_x = -100
            bullet2_y = -100
            cube14_hp -= 1
        if bullet3_x in range(cube14_x, (cube14_x + cube_size)) and bullet3_y in range(cube14_y, (cube14_y + cube_size), 1): # rd cubes get shot
            bullet3_fly = False
            Bullet3_x = -100
            bullet3_y = -100
            cube14_hp -= 1
        if bullet4_x in range(cube14_x, (cube14_x + cube_size)) and bullet4_y in range(cube14_y, (cube14_y + cube_size), 1): # rd cubes get shot
            bullet4_fly = False
            Bullet4_x = -100
            bullet4_y = -100
            cube14_hp -= 1
        if bullet5_x in range(cube14_x, (cube14_x + cube_size)) and bullet5_y in range(cube14_y, (cube14_y + cube_size), 1): # rd cubes get shot
            bullet5_fly = False
            Bullet5_x = -100
            bullet5_y = -100
            cube14_hp -= 1
        if bullet6_x in range(cube14_x, (cube14_x + cube_size)) and bullet6_y in range(cube14_y, (cube14_y + cube_size), 1): # rd cubes get shot
            bullet6_fly = False
            Bullet6_x = -100
            bullet6_y = -100
            cube14_hp -= 1
        if bullet7_x in range(cube14_x, (cube14_x + cube_size)) and bullet7_y in range(cube14_y, (cube14_y + cube_size), 1): # rd cubes get shot
            bullet7_fly = False
            Bullet7_x = -100
            bullet7_y = -100
            cube14_hp -= 1
        if bullet8_x in range(cube14_x, (cube14_x + cube_size)) and bullet8_y in range(cube14_y, (cube14_y + cube_size), 1): # rd cubes get shot
            bullet8_fly = False
            Bullet8_x = -100
            bullet8_y = -100
            cube14_hp -= 1
        if bullet9_x in range(cube14_x, (cube14_x + cube_size)) and bullet9_y in range(cube14_y, (cube14_y + cube_size), 1): # rd cubes get shot
            bullet9_fly = False
            Bullet9_x = -100
            bullet9_y = -100
            cube14_hp -= 1
        if bullet10_x in range(cube14_x, (cube14_x + cube_size)) and bullet10_y in range(cube14_y, (cube14_y + cube_size), 1): # rd cubes get shot
            bullet10_fly = False
            Bullet10_x = -100
            bullet10_y = -100
            cube14_hp -= 1
        
        if bullet1_x in range(cube15_x, (cube15_x + cube_size)) and bullet1_y in range(cube15_y, (cube15_y + cube_size), 1): # rd cubes get shot
            bullet1_fly = False
            Bullet1_x = -100
            bullet1_y = -100
            cube15_hp -= 1
        if bullet2_x in range(cube15_x, (cube15_x + cube_size)) and bullet2_y in range(cube15_y, (cube15_y + cube_size), 1): # rd cubes get shot
            bullet2_fly = False
            Bullet2_x = -100
            bullet2_y = -100
            cube15_hp -= 1
        if bullet3_x in range(cube15_x, (cube15_x + cube_size)) and bullet3_y in range(cube15_y, (cube15_y + cube_size), 1): # rd cubes get shot
            bullet3_fly = False
            Bullet3_x = -100
            bullet3_y = -100
            cube15_hp -= 1
        if bullet4_x in range(cube15_x, (cube15_x + cube_size)) and bullet4_y in range(cube15_y, (cube15_y + cube_size), 1): # rd cubes get shot
            bullet4_fly = False
            Bullet4_x = -100
            bullet4_y = -100
            cube15_hp -= 1
        if bullet5_x in range(cube15_x, (cube15_x + cube_size)) and bullet5_y in range(cube15_y, (cube15_y + cube_size), 1): # rd cubes get shot
            bullet5_fly = False
            Bullet5_x = -100
            bullet5_y = -100
            cube15_hp -= 1
        if bullet6_x in range(cube15_x, (cube15_x + cube_size)) and bullet6_y in range(cube15_y, (cube15_y + cube_size), 1): # rd cubes get shot
            bullet6_fly = False
            Bullet6_x = -100
            bullet6_y = -100
            cube15_hp -= 1
        if bullet7_x in range(cube15_x, (cube15_x + cube_size)) and bullet7_y in range(cube15_y, (cube15_y + cube_size), 1): # rd cubes get shot
            bullet7_fly = False
            Bullet7_x = -100
            bullet7_y = -100
            cube15_hp -= 1
        if bullet8_x in range(cube15_x, (cube15_x + cube_size)) and bullet8_y in range(cube15_y, (cube15_y + cube_size), 1): # rd cubes get shot
            bullet8_fly = False
            Bullet8_x = -100
            bullet8_y = -100
            cube15_hp -= 1
        if bullet9_x in range(cube15_x, (cube15_x + cube_size)) and bullet9_y in range(cube15_y, (cube15_y + cube_size), 1): # rd cubes get shot
            bullet9_fly = False
            Bullet9_x = -100
            bullet9_y = -100
            cube15_hp -= 1
        if bullet10_x in range(cube15_x, (cube15_x + cube_size)) and bullet10_y in range(cube15_y, (cube15_y + cube_size), 1): # rd cubes get shot
            bullet10_fly = False
            Bullet10_x = -100
            bullet10_y = -100
            cube15_hp -= 1
        
        if bullet1_x in range(cube16_x, (cube16_x + cube_size)) and bullet1_y in range(cube16_y, (cube16_y + cube_size), 1): # rd cubes get shot
            bullet1_fly = False
            Bullet1_x = -100
            bullet1_y = -100
            cube16_hp -= 1
        if bullet2_x in range(cube16_x, (cube16_x + cube_size)) and bullet2_y in range(cube16_y, (cube16_y + cube_size), 1): # rd cubes get shot
            bullet2_fly = False
            Bullet2_x = -100
            bullet2_y = -100
            cube16_hp -= 1
        if bullet3_x in range(cube16_x, (cube16_x + cube_size)) and bullet3_y in range(cube16_y, (cube16_y + cube_size), 1): # rd cubes get shot
            bullet3_fly = False
            Bullet3_x = -100
            bullet3_y = -100
            cube16_hp -= 1
        if bullet4_x in range(cube16_x, (cube16_x + cube_size)) and bullet4_y in range(cube16_y, (cube16_y + cube_size), 1): # rd cubes get shot
            bullet4_fly = False
            Bullet4_x = -100
            bullet4_y = -100
            cube16_hp -= 1
        if bullet5_x in range(cube16_x, (cube16_x + cube_size)) and bullet5_y in range(cube16_y, (cube16_y + cube_size), 1): # rd cubes get shot
            bullet5_fly = False
            Bullet5_x = -100
            bullet5_y = -100
            cube16_hp -= 1
        if bullet6_x in range(cube16_x, (cube16_x + cube_size)) and bullet6_y in range(cube16_y, (cube16_y + cube_size), 1): # rd cubes get shot
            bullet6_fly = False
            Bullet6_x = -100
            bullet6_y = -100
            cube16_hp -= 1
        if bullet7_x in range(cube16_x, (cube16_x + cube_size)) and bullet7_y in range(cube16_y, (cube16_y + cube_size), 1): # rd cubes get shot
            bullet7_fly = False
            Bullet7_x = -100
            bullet7_y = -100
            cube16_hp -= 1
        if bullet8_x in range(cube16_x, (cube16_x + cube_size)) and bullet8_y in range(cube16_y, (cube16_y + cube_size), 1): # rd cubes get shot
            bullet8_fly = False
            Bullet8_x = -100
            bullet8_y = -100
            cube16_hp -= 1
        if bullet9_x in range(cube16_x, (cube16_x + cube_size)) and bullet9_y in range(cube16_y, (cube16_y + cube_size), 1): # rd cubes get shot
            bullet9_fly = False
            Bullet9_x = -100
            bullet9_y = -100
            cube16_hp -= 1
        if bullet10_x in range(cube16_x, (cube16_x + cube_size)) and bullet10_y in range(cube16_y, (cube16_y + cube_size), 1): # rd cubes get shot
            bullet10_fly = False
            Bullet10_x = -100
            bullet10_y = -100
            cube16_hp -= 1
        
        if bullet1_x in range(cube17_x, (cube17_x + cube_size)) and bullet1_y in range(cube17_y, (cube17_y + cube_size), 1): # rd cubes get shot
            bullet1_fly = False
            Bullet1_x = -100
            bullet1_y = -100
            cube17_hp -= 1
        if bullet2_x in range(cube17_x, (cube17_x + cube_size)) and bullet2_y in range(cube17_y, (cube17_y + cube_size), 1): # rd cubes get shot
            bullet2_fly = False
            Bullet2_x = -100
            bullet2_y = -100
            cube17_hp -= 1
        if bullet3_x in range(cube17_x, (cube17_x + cube_size)) and bullet3_y in range(cube17_y, (cube17_y + cube_size), 1): # rd cubes get shot
            bullet3_fly = False
            Bullet3_x = -100
            bullet3_y = -100
            cube17_hp -= 1
        if bullet4_x in range(cube17_x, (cube17_x + cube_size)) and bullet4_y in range(cube17_y, (cube17_y + cube_size), 1): # rd cubes get shot
            bullet4_fly = False
            Bullet4_x = -100
            bullet4_y = -100
            cube17_hp -= 1
        if bullet5_x in range(cube17_x, (cube17_x + cube_size)) and bullet5_y in range(cube17_y, (cube17_y + cube_size), 1): # rd cubes get shot
            bullet5_fly = False
            Bullet5_x = -100
            bullet5_y = -100
            cube17_hp -= 1
        if bullet6_x in range(cube17_x, (cube17_x + cube_size)) and bullet6_y in range(cube17_y, (cube17_y + cube_size), 1): # rd cubes get shot
            bullet6_fly = False
            Bullet6_x = -100
            bullet6_y = -100
            cube17_hp -= 1
        if bullet7_x in range(cube17_x, (cube17_x + cube_size)) and bullet7_y in range(cube17_y, (cube17_y + cube_size), 1): # rd cubes get shot
            bullet7_fly = False
            Bullet7_x = -100
            bullet7_y = -100
            cube17_hp -= 1
        if bullet8_x in range(cube17_x, (cube17_x + cube_size)) and bullet8_y in range(cube17_y, (cube17_y + cube_size), 1): # rd cubes get shot
            bullet8_fly = False
            Bullet8_x = -100
            bullet8_y = -100
            cube17_hp -= 1
        if bullet9_x in range(cube17_x, (cube17_x + cube_size)) and bullet9_y in range(cube17_y, (cube17_y + cube_size), 1): # rd cubes get shot
            bullet9_fly = False
            Bullet9_x = -100
            bullet9_y = -100
            cube17_hp -= 1
        if bullet10_x in range(cube17_x, (cube17_x + cube_size)) and bullet10_y in range(cube17_y, (cube17_y + cube_size), 1): # rd cubes get shot
            bullet10_fly = False
            Bullet10_x = -100
            bullet10_y = -100
            cube17_hp -= 1
        
        if bullet1_x in range(cube18_x, (cube18_x + cube_size)) and bullet1_y in range(cube18_y, (cube18_y + cube_size), 1): # rd cubes get shot
            bullet1_fly = False
            Bullet1_x = -100
            bullet1_y = -100
            cube18_hp -= 1
        if bullet2_x in range(cube18_x, (cube18_x + cube_size)) and bullet2_y in range(cube18_y, (cube18_y + cube_size), 1): # rd cubes get shot
            bullet2_fly = False
            Bullet2_x = -100
            bullet2_y = -100
            cube18_hp -= 1
        if bullet3_x in range(cube18_x, (cube18_x + cube_size)) and bullet3_y in range(cube18_y, (cube18_y + cube_size), 1): # rd cubes get shot
            bullet3_fly = False
            Bullet3_x = -100
            bullet3_y = -100
            cube18_hp -= 1
        if bullet4_x in range(cube18_x, (cube18_x + cube_size)) and bullet4_y in range(cube18_y, (cube18_y + cube_size), 1): # rd cubes get shot
            bullet4_fly = False
            Bullet4_x = -100
            bullet4_y = -100
            cube18_hp -= 1
        if bullet5_x in range(cube18_x, (cube18_x + cube_size)) and bullet5_y in range(cube18_y, (cube18_y + cube_size), 1): # rd cubes get shot
            bullet5_fly = False
            Bullet5_x = -100
            bullet5_y = -100
            cube18_hp -= 1
        if bullet6_x in range(cube18_x, (cube18_x + cube_size)) and bullet6_y in range(cube18_y, (cube18_y + cube_size), 1): # rd cubes get shot
            bullet6_fly = False
            Bullet6_x = -100
            bullet6_y = -100
            cube18_hp -= 1
        if bullet7_x in range(cube18_x, (cube18_x + cube_size)) and bullet7_y in range(cube18_y, (cube18_y + cube_size), 1): # rd cubes get shot
            bullet7_fly = False
            Bullet7_x = -100
            bullet7_y = -100
            cube18_hp -= 1
        if bullet8_x in range(cube18_x, (cube18_x + cube_size)) and bullet8_y in range(cube18_y, (cube18_y + cube_size), 1): # rd cubes get shot
            bullet8_fly = False
            Bullet8_x = -100
            bullet8_y = -100
            cube18_hp -= 1
        if bullet9_x in range(cube18_x, (cube18_x + cube_size)) and bullet9_y in range(cube18_y, (cube18_y + cube_size), 1): # rd cubes get shot
            bullet9_fly = False
            Bullet9_x = -100
            bullet9_y = -100
            cube18_hp -= 1
        if bullet10_x in range(cube18_x, (cube18_x + cube_size)) and bullet10_y in range(cube18_y, (cube18_y + cube_size), 1): # rd cubes get shot
            bullet10_fly = False
            Bullet10_x = -100
            bullet10_y = -100
            cube18_hp -= 1
        
        if bullet1_x in range(cube19_x, (cube19_x + cube_size)) and bullet1_y in range(cube19_y, (cube19_y + cube_size), 1): # rd cubes get shot
            bullet1_fly = False
            Bullet1_x = -100
            bullet1_y = -100
            cube19_hp -= 1
        if bullet2_x in range(cube19_x, (cube19_x + cube_size)) and bullet2_y in range(cube19_y, (cube19_y + cube_size), 1): # rd cubes get shot
            bullet2_fly = False
            Bullet2_x = -100
            bullet2_y = -100
            cube19_hp -= 1
        if bullet3_x in range(cube19_x, (cube19_x + cube_size)) and bullet3_y in range(cube19_y, (cube19_y + cube_size), 1): # rd cubes get shot
            bullet3_fly = False
            Bullet3_x = -100
            bullet3_y = -100
            cube19_hp -= 1
        if bullet4_x in range(cube19_x, (cube19_x + cube_size)) and bullet4_y in range(cube19_y, (cube19_y + cube_size), 1): # rd cubes get shot
            bullet4_fly = False
            Bullet4_x = -100
            bullet4_y = -100
            cube19_hp -= 1
        if bullet5_x in range(cube19_x, (cube19_x + cube_size)) and bullet5_y in range(cube19_y, (cube19_y + cube_size), 1): # rd cubes get shot
            bullet5_fly = False
            Bullet5_x = -100
            bullet5_y = -100
            cube19_hp -= 1
        if bullet6_x in range(cube19_x, (cube19_x + cube_size)) and bullet6_y in range(cube19_y, (cube19_y + cube_size), 1): # rd cubes get shot
            bullet6_fly = False
            Bullet6_x = -100
            bullet6_y = -100
            cube19_hp -= 1
        if bullet7_x in range(cube19_x, (cube19_x + cube_size)) and bullet7_y in range(cube19_y, (cube19_y + cube_size), 1): # rd cubes get shot
            bullet7_fly = False
            Bullet7_x = -100
            bullet7_y = -100
            cube19_hp -= 1
        if bullet8_x in range(cube19_x, (cube19_x + cube_size)) and bullet8_y in range(cube19_y, (cube19_y + cube_size), 1): # rd cubes get shot
            bullet8_fly = False
            Bullet8_x = -100
            bullet8_y = -100
            cube19_hp -= 1
        if bullet9_x in range(cube19_x, (cube19_x + cube_size)) and bullet9_y in range(cube19_y, (cube19_y + cube_size), 1): # rd cubes get shot
            bullet9_fly = False
            Bullet9_x = -100
            bullet9_y = -100
            cube19_hp -= 1
        if bullet10_x in range(cube19_x, (cube19_x + cube_size)) and bullet10_y in range(cube19_y, (cube19_y + cube_size), 1): # rd cubes get shot
            bullet10_fly = False
            Bullet10_x = -100
            bullet10_y = -100
            cube19_hp -= 1
        
        if bullet1_x in range(cube20_x, (cube20_x + cube_size)) and bullet1_y in range(cube20_y, (cube20_y + cube_size), 1): # rd cubes get shot
            bullet1_fly = False
            Bullet1_x = -100
            bullet1_y = -100
            cube20_hp -= 1
        if bullet2_x in range(cube20_x, (cube20_x + cube_size)) and bullet2_y in range(cube20_y, (cube20_y + cube_size), 1): # rd cubes get shot
            bullet2_fly = False
            Bullet2_x = -100
            bullet2_y = -100
            cube20_hp -= 1
        if bullet3_x in range(cube20_x, (cube20_x + cube_size)) and bullet3_y in range(cube20_y, (cube20_y + cube_size), 1): # rd cubes get shot
            bullet3_fly = False
            Bullet3_x = -100
            bullet3_y = -100
            cube20_hp -= 1
        if bullet4_x in range(cube20_x, (cube20_x + cube_size)) and bullet4_y in range(cube20_y, (cube20_y + cube_size), 1): # rd cubes get shot
            bullet4_fly = False
            Bullet4_x = -100
            bullet4_y = -100
            cube20_hp -= 1
        if bullet5_x in range(cube20_x, (cube20_x + cube_size)) and bullet5_y in range(cube20_y, (cube20_y + cube_size), 1): # rd cubes get shot
            bullet5_fly = False
            Bullet5_x = -100
            bullet5_y = -100
            cube20_hp -= 1
        if bullet6_x in range(cube20_x, (cube20_x + cube_size)) and bullet6_y in range(cube20_y, (cube20_y + cube_size), 1): # rd cubes get shot
            bullet6_fly = False
            Bullet6_x = -100
            bullet6_y = -100
            cube20_hp -= 1
        if bullet7_x in range(cube20_x, (cube20_x + cube_size)) and bullet7_y in range(cube20_y, (cube20_y + cube_size), 1): # rd cubes get shot
            bullet7_fly = False
            Bullet7_x = -100
            bullet7_y = -100
            cube20_hp -= 1
        if bullet8_x in range(cube20_x, (cube20_x + cube_size)) and bullet8_y in range(cube20_y, (cube20_y + cube_size), 1): # rd cubes get shot
            bullet8_fly = False
            Bullet8_x = -100
            bullet8_y = -100
            cube20_hp -= 1
        if bullet9_x in range(cube20_x, (cube20_x + cube_size)) and bullet9_y in range(cube20_y, (cube20_y + cube_size), 1): # rd cubes get shot
            bullet9_fly = False
            Bullet9_x = -100
            bullet9_y = -100
            cube20_hp -= 1
        if bullet10_x in range(cube20_x, (cube20_x + cube_size)) and bullet10_y in range(cube20_y, (cube20_y + cube_size), 1): # rd cubes get shot
            bullet10_fly = False
            Bullet10_x = -100
            bullet10_y = -100
            cube20_hp -= 1
        
    
    if rd_cubes_hard == True:
        if menu == False:
            time_cube += 1
            
            cube1_y += cube1_y_move
            cube2_y += cube2_y_move
            cube3_y += cube3_y_move
            cube4_y += cube4_y_move
            
            cube5_y += cube5_y_move
            cube6_y += cube6_y_move
            cube7_y += cube7_y_move
            cube8_y += cube8_y_move
            
            cube9_y += cube9_y_move
            cube10_y += cube10_y_move
            cube11_y += cube11_y_move
            cube12_y += cube12_y_move
            
            cube13_y += cube13_y_move
            cube14_y += cube14_y_move
            cube15_y += cube15_y_move
            cube16_y += cube16_y_move
            
            cube17_y += cube17_y_move
            cube18_y += cube18_y_move
            cube19_y += cube19_y_move
            cube20_y += cube20_y_move
        
        if time_cube in range(0, 20,1):
            cube1_y_move = 4
            cube2_y_move = 4
            cube3_y_move = -4
            cube4_y_move = -4
            
            cube5_y_move = 4
            cube6_y_move = 4
            cube7_y_move = -4
            cube8_y_move = -4
            
            cube9_y_move = 4
            cube10_y_move = 4
            cube11_y_move = -4
            cube12_y_move = -4
            
            cube13_y_move = 4
            cube14_y_move = 4
            cube15_y_move = -4
            cube16_y_move = -4
            
            cube17_y_move = 4
            cube18_y_move = 4
            cube19_y_move = -4
            cube20_y_move = -4
            
        elif time_cube in range(20, 40,1):
            cube1_y_move = -4
            cube2_y_move = -4 
            cube3_y_move = 4
            cube4_y_move = 4
            
            cube5_y_move = -4
            cube6_y_move = -4 
            cube7_y_move = 4
            cube8_y_move = 4
            
            cube9_y_move = -4
            cube10_y_move = -4 
            cube11_y_move = 4
            cube12_y_move = 4

            cube13_y_move = -4
            cube14_y_move = -4 
            cube15_y_move = 4
            cube16_y_move = 4
            
            cube17_y_move = -4
            cube18_y_move = -4 
            cube19_y_move = 4
            cube20_y_move = 4
            
        elif time_cube > 40:
            time_cube = 0
    
        
    if rd_walls == True:    # rd walls
        if time_rd_walls < 2 and menu == False and b_boss == False:
            time_rd_walls += 1
        if time_rd_walls == 1 and menu == False and b_boss == False:
            wall1_x = 1920
            wall1_y = random.randrange(-1010, -250, (150))
            
            wall2_x = 2560
            wall2_y = random.randrange(-1010, -250, (150))
            
            wall3_x = 3200
            wall3_y = random.randrange(-1010, -250, (150))
            
            door2_str = 1
            
            
        pygame.draw.rect(screen, (WALL_COLOR1), ((wall1_x, wall1_y), (wall_width, wall_height)))        
        pygame.draw.rect(screen, (WALL_COLOR1), ((wall1_x, (wall1_y + 1180)), (wall_width, wall_height)))
        if menu == False and hp > 0:
            wall1_x -= bg_sp
            if (wall1_x <= -wall_width) and (wall_rs == True):
                wall1_x = 1920
                wall1_y = random.randrange(-1010, -250, (150))    

        pygame.draw.rect(screen, (WALL_COLOR1), ((wall2_x, wall2_y), (wall_width, wall_height)))
        pygame.draw.rect(screen, (WALL_COLOR1), ((wall2_x, (wall2_y + 1180)), (wall_width, wall_height)))
        if menu == False and hp > 0:
            wall2_x -= bg_sp
        if (wall2_x <= -wall_width) and (wall_rs == True):
            if door2_str == 2:
                door2_str = 1
            else:
                door2_str += 1
            door2_hp = door2_str
            sc_door2_reset = False
            wall2_x = 1920
            wall2_y = random.randrange(-1010, -250, (150))
            if wall1_x == 1920:
                wall2_x += 640

                    
        pygame.draw.rect(screen, (WALL_COLOR1), ((wall3_x, wall3_y), (wall_width, wall_height)))
        pygame.draw.rect(screen, (WALL_COLOR1), ((wall3_x, (wall3_y + 1180)), (wall_width, wall_height)))
        if menu == False and hp > 0:
            wall3_x -= bg_sp
        if (wall3_x <= -wall_width) and (wall_rs == True):
            wall3_x = 1920
            wall3_y = random.randrange(-1010, -250, (150))
            if wall1_x == 1920:
                wall3_x += 640 *2
            
            # door on wall 2    
        if door2_str == 1 and door2_hp > 0:
            pygame.draw.rect(screen, (CUBE_COLOR1), (((wall2_x + 35), (wall2_y + 1030)), (50, 150)))
        if door2_str == 2 and door2_hp > 0:
            pygame.draw.rect(screen, (CUBE_COLOR2), (((wall2_x + 35), (wall2_y + 1030)), (50, 150)))
        if door2_str == 3 and door2_hp > 0:
            pygame.draw.rect(screen, (CUBE_COLOR3), (((wall2_x + 35), (wall2_y + 1030)), (50, 150)))
                
                
            # hitbox door to player and bullet to door
        if door2_hp > 0:
            if (hitbox_player[0] in range((wall2_x + 35), ((wall2_x + 35) + 150), 1) or hitbox_player[0] + pl_length in range((wall2_x + 35), ((wall2_x + 35) + 150), 1)) and (hitbox_player[1] in range((wall2_y + 1030), ((wall2_y + 1030) + 50), 1) or hitbox_player[1] + pl_height in range((wall2_y + 1030), ((wall2_y + 1030) + 50), 1)): # player get hit
                pl_get_dmg = True
                door2_hp = 0
            if (hitbox_player[0] in range((wall2_x + 35), ((wall2_x + 35) + 150), 1) or hitbox_player[0] + pl_length in range((wall2_x + 35), ((wall2_x + 35) + 150), 1)) and (hitbox_player[1] in range((wall2_y + 1080), ((wall2_y + 1080) + 50), 1) or hitbox_player[1] + pl_height in range((wall2_y + 1080), ((wall2_y + 1080) + 50), 1)): # player get hit
                pl_get_dmg = True
                door2_hp = 0 
                
            if bullet1_x in range((wall2_x + 35), (wall2_x + 85)) and bullet1_y in range((wall2_y + 1030), (wall2_y + 1180), 1): 
                door2_hp -= 1
                bullet1_fly = False
                Bullet1_x = -100
                bullet1_y = -100
            if bullet2_x in range((wall2_x + 35), (wall2_x + 85)) and bullet2_y in range((wall2_y + 1030), (wall2_y + 1180), 1): 
                door2_hp -= 1
                bullet2_fly = False
                Bullet2_x = -100
                bullet2_y = -100
            if bullet3_x in range((wall2_x + 35), (wall2_x + 85)) and bullet3_y in range((wall2_y + 1030), (wall2_y + 1180), 1):
                door2_hp -= 1
                bullet3_fly = False
                Bullet3_x = -100
                bullet3_y = -100
            if bullet4_x in range((wall2_x + 35), (wall2_x + 85)) and bullet4_y in range((wall2_y + 1030), (wall2_y + 1180), 1): 
                door2_hp -= 1
                bullet4_fly = False
                Bullet4_x = -100
                bullet4_y = -100
            if bullet5_x in range((wall2_x + 35), (wall2_x + 85)) and bullet5_y in range((wall2_y + 1030), (wall2_y + 1180), 1): 
                door2_hp -= 1
                bullet5_fly = False
                Bullet5_x = -100
                bullet5_y = -100
            if bullet6_x in range((wall2_x + 35), (wall2_x + 85)) and bullet6_y in range((wall2_y + 1030), (wall2_y + 1180), 1): 
                door2_hp -= 1
                bullet6_fly = False
                Bullet6_x = -100
                bullet6_y = -100
            if bullet7_x in range((wall2_x + 35), (wall2_x + 85)) and bullet7_y in range((wall2_y + 1030), (wall2_y + 1180), 1):
                door2_hp -= 1
                bullet7_fly = False
                Bullet7_x = -100
                bullet7_y = -100
            if bullet8_x in range((wall2_x + 35), (wall2_x + 85)) and bullet8_y in range((wall2_y + 1030), (wall2_y + 1180), 1): 
                door2_hp -= 1
                bullet8_fly = False
                Bullet8_x = -100
                bullet8_y = -100
            if bullet9_x in range((wall2_x + 35), (wall2_x + 85)) and bullet9_y in range((wall2_y + 1030), (wall2_y + 1180), 1):
                door2_hp -= 1
                bullet9_fly = False
                Bullet9_x = -100
                bullet9_y = -100
            if bullet10_x in range((wall2_x + 35), (wall2_x + 85)) and bullet10_y in range((wall2_y + 1030), (wall2_y + 1180), 1): 
                door2_hp -= 1
                bullet10_fly = False
                Bullet10_x = -100
                bullet10_y = -100
                

        # bullet to wall
        if bullet1_x in range(wall1_x, (wall1_x + 150)) and bullet1_y in range(wall1_y, (wall1_y + 1030), 1): 
            bullet1_fly = False
            Bullet1_x = -100
            bullet1_y = -100
        if bullet2_x in range(wall1_x, (wall1_x + 150)) and bullet2_y in range(wall1_y, (wall1_y + 1030), 1): 
            bullet2_fly = False
            Bullet2_x = -100
            bullet2_y = -100
        if bullet3_x in range(wall1_x, (wall1_x + 150)) and bullet3_y in range(wall1_y, (wall1_y + 1030), 1): 
            bullet3_fly = False
            Bullet3_x = -100
            bullet3_y = -100
        if bullet4_x in range(wall1_x, (wall1_x + 150)) and bullet4_y in range(wall1_y, (wall1_y + 1030), 1): 
            bullet4_fly = False
            Bullet4_x = -100
            bullet4_y = -100
        if bullet5_x in range(wall1_x, (wall1_x + 150)) and bullet5_y in range(wall1_y, (wall1_y + 1030), 1): 
            bullet5_fly = False
            Bullet5_x = -100
            bullet5_y = -100
        if bullet6_x in range(wall1_x, (wall1_x + 150)) and bullet6_y in range(wall1_y, (wall1_y + 1030), 1): 
            bullet6_fly = False
            Bullet6_x = -100
            bullet6_y = -100
        if bullet7_x in range(wall1_x, (wall1_x + 150)) and bullet7_y in range(wall1_y, (wall1_y + 1030), 1): 
            bullet7_fly = False
            Bullet7_x = -100
            bullet7_y = -100
        if bullet8_x in range(wall1_x, (wall1_x + 150)) and bullet8_y in range(wall1_y, (wall1_y + 1030), 1): 
            bullet8_fly = False
            Bullet8_x = -100
            bullet8_y = -100
        if bullet9_x in range(wall1_x, (wall1_x + 150)) and bullet9_y in range(wall1_y, (wall1_y + 1030), 1): 
            bullet9_fly = False
            Bullet9_x = -100
            bullet9_y = -100
        if bullet10_x in range(wall1_x, (wall1_x + 150)) and bullet10_y in range(wall1_y, (wall1_y + 1030), 1): 
            bullet10_fly = False
            Bullet10_x = -100
            bullet10_y = -100
            
        if bullet1_x in range(wall1_x, (wall1_x + 150)) and bullet1_y in range((wall1_y + 1180), (wall1_y + 2210), 1): 
            bullet1_fly = False
            Bullet1_x = -100
            bullet1_y = -100
        if bullet2_x in range(wall1_x, (wall1_x + 150)) and bullet2_y in range((wall1_y + 1180), (wall1_y + 2210), 1): 
            bullet2_fly = False
            Bullet2_x = -100
            bullet2_y = -100
        if bullet3_x in range(wall1_x, (wall1_x + 150)) and bullet3_y in range((wall1_y + 1180), (wall1_y + 2210), 1): 
            bullet3_fly = False
            Bullet3_x = -100
            bullet3_y = -100
        if bullet4_x in range(wall1_x, (wall1_x + 150)) and bullet4_y in range((wall1_y + 1180), (wall1_y + 2210), 1): 
            bullet4_fly = False
            Bullet4_x = -100
            bullet4_y = -100
        if bullet5_x in range(wall1_x, (wall1_x + 150)) and bullet5_y in range((wall1_y + 1180), (wall1_y + 2210), 1): 
            bullet5_fly = False
            Bullet5_x = -100
            bullet5_y = -100
        if bullet6_x in range(wall1_x, (wall1_x + 150)) and bullet6_y in range((wall1_y + 1180), (wall1_y + 2210), 1): 
            bullet6_fly = False
            Bullet6_x = -100
            bullet6_y = -100
        if bullet7_x in range(wall1_x, (wall1_x + 150)) and bullet7_y in range((wall1_y + 1180), (wall1_y + 2210), 1): 
            bullet7_fly = False
            Bullet7_x = -100
            bullet7_y = -100
        if bullet8_x in range(wall1_x, (wall1_x + 150)) and bullet8_y in range((wall1_y + 1180), (wall1_y + 2210), 1): 
            bullet8_fly = False
            Bullet8_x = -100
            bullet8_y = -100
        if bullet9_x in range(wall1_x, (wall1_x + 150)) and bullet9_y in range((wall1_y + 1180), (wall1_y + 2210), 1): 
            bullet9_fly = False
            Bullet9_x = -100
            bullet9_y = -100
        if bullet10_x in range(wall1_x, (wall1_x + 150)) and bullet10_y in range((wall1_y + 1180), (wall1_y + 2210), 1): 
            bullet10_fly = False
            Bullet10_x = -100
            bullet10_y = -100
            
        if bullet1_x in range(wall2_x, (wall2_x + 150)) and bullet1_y in range(wall2_y, (wall2_y + 1030), 1): 
            bullet1_fly = False
            Bullet1_x = -100
            bullet1_y = -100
        if bullet2_x in range(wall2_x, (wall2_x + 150)) and bullet2_y in range(wall2_y, (wall2_y + 1030), 1): 
            bullet2_fly = False
            Bullet2_x = -100
            bullet2_y = -100
        if bullet3_x in range(wall2_x, (wall2_x + 150)) and bullet3_y in range(wall2_y, (wall2_y + 1030), 1): 
            bullet3_fly = False
            Bullet3_x = -100
            bullet3_y = -100
        if bullet4_x in range(wall2_x, (wall2_x + 150)) and bullet4_y in range(wall2_y, (wall2_y + 1030), 1): 
            bullet4_fly = False
            Bullet4_x = -100
            bullet4_y = -100
        if bullet5_x in range(wall2_x, (wall2_x + 150)) and bullet5_y in range(wall2_y, (wall2_y + 1030), 1): 
            bullet5_fly = False
            Bullet5_x = -100
            bullet5_y = -100
        if bullet6_x in range(wall2_x, (wall2_x + 150)) and bullet6_y in range(wall2_y, (wall2_y + 1030), 1): 
            bullet6_fly = False
            Bullet6_x = -100
            bullet6_y = -100
        if bullet7_x in range(wall2_x, (wall2_x + 150)) and bullet7_y in range(wall2_y, (wall2_y + 1030), 1): 
            bullet7_fly = False
            Bullet7_x = -100
            bullet7_y = -100
        if bullet8_x in range(wall2_x, (wall2_x + 150)) and bullet8_y in range(wall2_y, (wall2_y + 1030), 1): 
            bullet8_fly = False
            Bullet8_x = -100
            bullet8_y = -100
        if bullet9_x in range(wall2_x, (wall2_x + 150)) and bullet9_y in range(wall2_y, (wall2_y + 1030), 1): 
            bullet9_fly = False
            Bullet9_x = -100
            bullet9_y = -100
        if bullet10_x in range(wall2_x, (wall2_x + 150)) and bullet10_y in range(wall2_y, (wall2_y + 1030), 1): 
            bullet10_fly = False
            Bullet10_x = -100
            bullet10_y = -100
            
        if bullet1_x in range(wall2_x, (wall2_x + 150)) and bullet1_y in range((wall2_y + 1180), (wall2_y + 2210), 1): 
            bullet1_fly = False
            Bullet1_x = -100
            bullet1_y = -100
        if bullet2_x in range(wall2_x, (wall2_x + 150)) and bullet2_y in range((wall2_y + 1180), (wall2_y + 2210), 1): 
            bullet2_fly = False
            Bullet2_x = -100
            bullet2_y = -100
        if bullet3_x in range(wall2_x, (wall2_x + 150)) and bullet3_y in range((wall2_y + 1180), (wall2_y + 2210), 1): 
            bullet3_fly = False
            Bullet3_x = -100
            bullet3_y = -100
        if bullet4_x in range(wall2_x, (wall2_x + 150)) and bullet4_y in range((wall2_y + 1180), (wall2_y + 2210), 1): 
            bullet4_fly = False
            Bullet4_x = -100
            bullet4_y = -100
        if bullet5_x in range(wall2_x, (wall2_x + 150)) and bullet5_y in range((wall2_y + 1180), (wall2_y + 2210), 1): 
            bullet5_fly = False
            Bullet5_x = -100
            bullet5_y = -100
        if bullet6_x in range(wall2_x, (wall2_x + 150)) and bullet6_y in range((wall2_y + 1180), (wall2_y + 2210), 1): 
            bullet6_fly = False
            Bullet6_x = -100
            bullet6_y = -100
        if bullet7_x in range(wall2_x, (wall2_x + 150)) and bullet7_y in range((wall2_y + 1180), (wall2_y + 2210), 1): 
            bullet7_fly = False
            Bullet7_x = -100
            bullet7_y = -100
        if bullet8_x in range(wall2_x, (wall2_x + 150)) and bullet8_y in range((wall2_y + 1180), (wall2_y + 2210), 1): 
            bullet8_fly = False
            Bullet8_x = -100
            bullet8_y = -100
        if bullet9_x in range(wall2_x, (wall2_x + 150)) and bullet9_y in range((wall2_y + 1180), (wall2_y + 2210), 1): 
            bullet9_fly = False
            Bullet9_x = -100
            bullet9_y = -100
        if bullet10_x in range(wall2_x, (wall2_x + 150)) and bullet10_y in range((wall2_y + 1180), (wall2_y + 2210), 1): 
            bullet10_fly = False
            Bullet10_x = -100
            bullet10_y = -100
            
        if bullet1_x in range(wall3_x, (wall3_x + 150)) and bullet1_y in range(wall3_y, (wall3_y + 1030), 1): 
            bullet1_fly = False
            Bullet1_x = -100
            bullet1_y = -100
        if bullet2_x in range(wall3_x, (wall3_x + 150)) and bullet2_y in range(wall3_y, (wall3_y + 1030), 1): 
            bullet2_fly = False
            Bullet2_x = -100
            bullet2_y = -100
        if bullet3_x in range(wall3_x, (wall3_x + 150)) and bullet3_y in range(wall3_y, (wall3_y + 1030), 1): 
            bullet3_fly = False
            Bullet3_x = -100
            bullet3_y = -100
        if bullet4_x in range(wall3_x, (wall3_x + 150)) and bullet4_y in range(wall3_y, (wall3_y + 1030), 1): 
            bullet4_fly = False
            Bullet4_x = -100
            bullet4_y = -100
        if bullet5_x in range(wall3_x, (wall3_x + 150)) and bullet5_y in range(wall3_y, (wall3_y + 1030), 1): 
            bullet5_fly = False
            Bullet5_x = -100
            bullet5_y = -100
        if bullet6_x in range(wall3_x, (wall3_x + 150)) and bullet6_y in range(wall3_y, (wall3_y + 1030), 1): 
            bullet6_fly = False
            Bullet6_x = -100
            bullet6_y = -100
        if bullet7_x in range(wall3_x, (wall3_x + 150)) and bullet7_y in range(wall3_y, (wall3_y + 1030), 1): 
            bullet7_fly = False
            Bullet7_x = -100
            bullet7_y = -100
        if bullet8_x in range(wall3_x, (wall3_x + 150)) and bullet8_y in range(wall3_y, (wall3_y + 1030), 1): 
            bullet8_fly = False
            Bullet8_x = -100
            bullet8_y = -100
        if bullet9_x in range(wall3_x, (wall3_x + 150)) and bullet9_y in range(wall3_y, (wall3_y + 1030), 1): 
            bullet9_fly = False
            Bullet9_x = -100
            bullet9_y = -100
        if bullet10_x in range(wall3_x, (wall3_x + 150)) and bullet10_y in range(wall3_y, (wall3_y + 1030), 1): 
            bullet10_fly = False
            Bullet10_x = -100
            bullet10_y = -100
            
        if bullet1_x in range(wall3_x, (wall3_x + 150)) and bullet1_y in range((wall3_y + 1180), (wall3_y + 2210), 1): 
            bullet1_fly = False
            Bullet1_x = -100
            bullet1_y = -100
        if bullet2_x in range(wall3_x, (wall3_x + 150)) and bullet2_y in range((wall3_y + 1180), (wall3_y + 2210), 1): 
            bullet2_fly = False
            Bullet2_x = -100
            bullet2_y = -100
        if bullet3_x in range(wall3_x, (wall3_x + 150)) and bullet3_y in range((wall3_y + 1180), (wall3_y + 2210), 1): 
            bullet3_fly = False
            Bullet3_x = -100
            bullet3_y = -100
        if bullet4_x in range(wall3_x, (wall3_x + 150)) and bullet4_y in range((wall3_y + 1180), (wall3_y + 2210), 1): 
            bullet4_fly = False
            Bullet4_x = -100
            bullet4_y = -100
        if bullet5_x in range(wall3_x, (wall3_x + 150)) and bullet5_y in range((wall3_y + 1180), (wall3_y + 2210), 1): 
            bullet5_fly = False
            Bullet5_x = -100
            bullet5_y = -100
        if bullet6_x in range(wall3_x, (wall3_x + 150)) and bullet6_y in range((wall3_y + 1180), (wall3_y + 2210), 1): 
            bullet6_fly = False
            Bullet6_x = -100
            bullet6_y = -100
        if bullet7_x in range(wall3_x, (wall3_x + 150)) and bullet7_y in range((wall3_y + 1180), (wall3_y + 2210), 1): 
            bullet7_fly = False
            Bullet7_x = -100
            bullet7_y = -100
        if bullet8_x in range(wall3_x, (wall3_x + 150)) and bullet8_y in range((wall3_y + 1180), (wall3_y + 2210), 1): 
            bullet8_fly = False
            Bullet8_x = -100
            bullet8_y = -100
        if bullet9_x in range(wall3_x, (wall3_x + 150)) and bullet9_y in range((wall3_y + 1180), (wall3_y + 2210), 1): 
            bullet9_fly = False
            Bullet9_x = -100
            bullet9_y = -100
        if bullet10_x in range(wall3_x, (wall3_x + 150)) and bullet10_y in range((wall3_y + 1180), (wall3_y + 2210), 1): 
            bullet10_fly = False
            Bullet10_x = -100
            bullet10_y = -100            

        
        # walls press the player to the left
        # wall 1
        if (hitbox_player[0] + pl_length) in range(wall1_x, (wall1_x + 150 + pl_length)) and hitbox_player[1] in range(wall1_y, (wall1_y + 1030), 1):
            sp_y_up = 0
        if hitbox_player[1] in range(wall1_y, (wall1_y + 1030), 1) and (hitbox_player[0] + pl_length) in range(wall1_x, (wall1_x + 30)):
            pl_x -= bg_sp
            sp_x = 0
            
        if (hitbox_player[0] + pl_length) in range(wall1_x, (wall1_x + 150 + pl_length)) and hitbox_player[1] in range((wall1_y + 1180 - pl_height), (wall1_y + 2210), 1):
            sp_y_down = 0
        if hitbox_player[1] in range((wall1_y + 1180 - pl_height), (wall1_y + 2210 - pl_height), 1) and (hitbox_player[0] + pl_length) in range(wall1_x, (wall1_x + 30)):
            pl_x -= bg_sp
            sp_x = 0
            
        # wall 2
        if (hitbox_player[0] + pl_length) in range(wall2_x, (wall2_x + 150 + pl_length)) and hitbox_player[1] in range(wall2_y, (wall2_y + 1030), 1):
            sp_y_up = 0
        if hitbox_player[1] in range(wall2_y, (wall2_y + 1030), 1) and (hitbox_player[0] + pl_length) in range(wall2_x, (wall2_x + 30)):
            pl_x -= bg_sp
            sp_x = 0
            
        if (hitbox_player[0] + pl_length) in range(wall2_x, (wall2_x + 150 + pl_length)) and hitbox_player[1] in range((wall2_y + 1180 - pl_height), (wall2_y + 2210), 1):
            sp_y_down = 0
        if hitbox_player[1] in range((wall2_y + 1180 - pl_height), (wall2_y + 2210 - pl_height), 1) and (hitbox_player[0] + pl_length) in range(wall2_x, (wall2_x + 30)):
            pl_x -= bg_sp
            sp_x = 0
            
        # wall 3
        if (hitbox_player[0] + pl_length) in range(wall3_x, (wall3_x + 150 + pl_length)) and hitbox_player[1] in range(wall3_y, (wall3_y + 1030), 1):
            sp_y_up = 0
        if hitbox_player[1] in range(wall3_y, (wall3_y + 1030), 1) and (hitbox_player[0] + pl_length) in range(wall3_x, (wall3_x + 30)):
            pl_x -= bg_sp
            sp_x = 0
            
        if (hitbox_player[0] + pl_length) in range(wall3_x, (wall3_x + 150 + pl_length)) and hitbox_player[1] in range((wall3_y + 1180 - pl_height), (wall3_y + 2210), 1):
            sp_y_down = 0
        if hitbox_player[1] in range((wall3_y + 1180 - pl_height), (wall3_y + 2210 - pl_height), 1) and (hitbox_player[0] + pl_length) in range(wall3_x, (wall3_x + 30)):
            pl_x -= bg_sp
            sp_x = 0
            
            
        # resets wall x if not in wall
        if (not (hitbox_player[1] in range(wall1_y, (wall1_y + 1030), 1) and (hitbox_player[0] + pl_length) in range(wall1_x, (wall1_x + 30))) 
            and not (hitbox_player[1] in range((wall1_y + 1180 - pl_height), (wall1_y + 2210 - pl_height), 1) and (hitbox_player[0] + pl_length) in range(wall1_x, (wall1_x + 30)))
            and not (hitbox_player[1] in range(wall2_y, (wall2_y + 1030), 1) and (hitbox_player[0] + pl_length) in range(wall2_x, (wall2_x + 30)))
            and not (hitbox_player[1] in range((wall2_y + 1180 - pl_height), (wall2_y + 2210 - pl_height), 1) and (hitbox_player[0] + pl_length) in range(wall2_x, (wall2_x + 30)))
            and not (hitbox_player[1] in range(wall3_y, (wall3_y + 1030), 1) and (hitbox_player[0] + pl_length) in range(wall3_x, (wall3_x + 30))) 
            and not (hitbox_player[1] in range((wall3_y + 1180 - pl_height), (wall3_y + 2210 - pl_height), 1) and (hitbox_player[0] + pl_length) in range(wall3_x, (wall3_x + 30)))
            ):
            sp_x = sp_x_save
            
        # resets wall y up if not in wall
        if (not ((hitbox_player[0] + pl_length) in range(wall1_x, (wall1_x + 150 + pl_length)) and hitbox_player[1] in range(wall1_y, (wall1_y + 1030), 1))
            and not ((hitbox_player[0] + pl_length) in range(wall2_x, (wall2_x + 150 + pl_length)) and hitbox_player[1] in range(wall2_y, (wall2_y + 1030), 1))
            and not ((hitbox_player[0] + pl_length) in range(wall3_x, (wall3_x + 150 + pl_length)) and hitbox_player[1] in range(wall3_y, (wall3_y + 1030), 1))
            ):
            sp_y_up = sp_y_up_save
            
        # resets wall y down if not in wall
        if (not ((hitbox_player[0] + pl_length) in range(wall1_x, (wall1_x + 150 + pl_length)) and hitbox_player[1] in range((wall1_y + 1180 - pl_height), (wall1_y + 2210), 1))
            and not ((hitbox_player[0] + pl_length) in range(wall2_x, (wall2_x + 150 + pl_length)) and hitbox_player[1] in range((wall2_y + 1180 - pl_height), (wall2_y + 2210), 1))
            and not ((hitbox_player[0] + pl_length) in range(wall3_x, (wall3_x + 150 + pl_length)) and hitbox_player[1] in range((wall3_y + 1180 - pl_height), (wall3_y + 2210), 1))
            ):
            sp_y_down = sp_y_down_save
            
            
    if rd_walls_hard == True:
        if menu == False:
            time_wall += 1

            if wall1_y > -1010:
                wall1_y += wall1_y_move_down
            if wall2_y > -1010:
                wall2_y += wall2_y_move_down   
            if wall3_y > -1010:
                wall3_y += wall3_y_move_down
                
            if wall1_y < -260:
                wall1_y += wall1_y_move_up
            if wall2_y < -260:
                wall2_y += wall2_y_move_up 
            if wall3_y < -260:
                wall3_y += wall3_y_move_up
            
            if time_wall in range(0, 30,1):
                wall1_y_move_up = 6
                wall2_y_move_down = -6
                wall3_y_move_up = 6
                
                wall1_y_move_down = 0
                wall2_y_move_up = 0
                wall3_y_move_down = 0
            
            elif time_wall in range(30, 60,1):
                wall1_y_move_down = -6
                wall2_y_move_up = 6
                wall3_y_move_down = -6
                
                wall1_y_move_up = 0
                wall2_y_move_down = 0
                wall3_y_move_up = 0
            elif time_wall > 60:
                time_wall = 0
            
        # wall1 movebox    
        if ((hitbox_player[0] + pl_length) in range(wall1_x, (wall1_x + 150 + pl_length)) 
            and hitbox_player[1] in range(wall1_y, (wall1_y + 1030), 1)
            ):
            if (hitbox_player[0] + pl_length) in range((wall1_x + 20), (wall1_x + 150 + pl_length)):
                pl_y += wall1_y_move_up
            
        if ((hitbox_player[0] + pl_length) in range(wall1_x, (wall1_x + 150 + pl_length)) 
            and hitbox_player[1] in range((wall1_y + 1180 - pl_height), (wall1_y + 2210), 1)
            ):
            if (hitbox_player[0] + pl_length) in range((wall1_x + 20), (wall1_x + 150 + pl_length)):
                pl_y += wall1_y_move_down
               
        # wall2 movebox       
        if ((hitbox_player[0] + pl_length) in range(wall2_x, (wall2_x + 150 + pl_length)) 
            and hitbox_player[1] in range(wall2_y, (wall2_y + 1030), 1)
            ):
            if (hitbox_player[0] + pl_length) in range((wall2_x + 20), (wall2_x + 150 + pl_length)):
                pl_y += wall2_y_move_up
            
        if ((hitbox_player[0] + pl_length) in range(wall2_x, (wall2_x + 150 + pl_length)) 
            and hitbox_player[1] in range((wall2_y + 1180 - pl_height), (wall2_y + 2210), 1)
            ):
            if (hitbox_player[0] + pl_length) in range((wall2_x + 20), (wall2_x + 150 + pl_length)):
                pl_y += wall2_y_move_down
            
        # wall3 movebox
        if ((hitbox_player[0] + pl_length) in range(wall3_x, (wall3_x + 150 + pl_length)) 
            and hitbox_player[1] in range(wall3_y, (wall3_y + 1030), 1)
            ):
            if (hitbox_player[0] + pl_length) in range((wall3_x + 20), (wall3_x + 150 + pl_length)):
                pl_y += wall3_y_move_up
            
        if ((hitbox_player[0] + pl_length) in range(wall3_x, (wall3_x + 150 + pl_length)) 
            and hitbox_player[1] in range((wall3_y + 1180 - pl_height), (wall3_y + 2210), 1)
            ):
            if (hitbox_player[0] + pl_length) in range((wall3_x + 20), (wall3_x + 150 + pl_length)):
                pl_y += wall3_y_move_down

    if s_boss == True:       
        # fires the beams
        if menu == False and not s_boss1_x > 1820 and time_beam_outro == False:
            time_beam += bg_sp
            
            if time_beam < 750:
                if s_boss1_y_rand > s_boss1_y:
                    s_boss1_y += 2
                elif s_boss1_y_rand < s_boss1_y:
                    s_boss1_y -= 2
                    
                if s_boss2_y_rand > s_boss2_y:
                    s_boss2_y += 2
                elif s_boss2_y_rand < s_boss2_y:
                    s_boss2_y -= 2
                    
                if s_boss3_y_rand > s_boss3_y:
                    s_boss3_y += 2
                elif s_boss3_y_rand < s_boss3_y:
                    s_boss3_y -= 2
                    
                if s_boss4_y_rand > s_boss4_y:
                    s_boss4_y += 2
                elif s_boss4_y_rand < s_boss4_y:
                    s_boss4_y -= 2

            if time_beam > 1400:
                s_boss1_beam_pos = 0, - 1000
                s_boss2_beam_pos = 0, - 1000
                s_boss3_beam_pos = 0, - 1000
                s_boss4_beam_pos = 0, - 1000
                s_boss1_y_rand = random.randrange(0, 90, (2))
                s_boss2_y_rand = random.randrange(190, 372, (2))
                s_boss3_y_rand = random.randrange(472, 654, (2))
                s_boss4_y_rand = random.randrange(754, 846, (2))
                time_beam = 0
                if time_round > time_round_max:
                    time_beam_outro = True
            elif time_beam in range(750 ,1400 ,1):
                s_boss1_beam_pos = pygame.draw.rect(screen, (CUBE_COLOR5), ((s_boss1_1_x, s_boss1_y), (1920, 100)))
                s_boss2_beam_pos = pygame.draw.rect(screen, (CUBE_COLOR5), ((s_boss2_1_x, s_boss2_y), (1920, 100)))
                s_boss3_beam_pos = pygame.draw.rect(screen, (CUBE_COLOR5), ((s_boss3_1_x, s_boss3_y), (1920, 100)))
                s_boss4_beam_pos = pygame.draw.rect(screen, (CUBE_COLOR5), ((s_boss4_1_x, s_boss4_y), (1920, 100)))
            elif time_beam in range(450, 600 ,1):
                pygame.draw.rect(screen, (GRAY), ((s_boss1_1_x, s_boss1_y), (1920, 100)))
                pygame.draw.rect(screen, (GRAY), ((s_boss2_1_x, s_boss2_y), (1920, 100)))
                pygame.draw.rect(screen, (GRAY), ((s_boss3_1_x, s_boss3_y), (1920, 100)))
                pygame.draw.rect(screen, (GRAY), ((s_boss4_1_x, s_boss4_y), (1920, 100)))
            elif time_beam in range(150, 300 ,1):
                pygame.draw.rect(screen, (GRAY), ((s_boss1_1_x, s_boss1_y), (1920, 100)))
                pygame.draw.rect(screen, (GRAY), ((s_boss2_1_x, s_boss2_y), (1920, 100)))
                pygame.draw.rect(screen, (GRAY), ((s_boss3_1_x, s_boss3_y), (1920, 100)))
                pygame.draw.rect(screen, (GRAY), ((s_boss4_1_x, s_boss4_y), (1920, 100)))
                        
        s_boss1_pos = pygame.draw.rect(screen, (LIGHT_YELLOW), ((s_boss1_x, s_boss1_y), (100, 100)))    
        s_boss2_pos = pygame.draw.rect(screen, (LIGHT_YELLOW), ((s_boss2_x, s_boss2_y), (100, 100)))  
        s_boss3_pos = pygame.draw.rect(screen, (LIGHT_YELLOW), ((s_boss3_x, s_boss3_y), (100, 100)))  
        s_boss4_pos = pygame.draw.rect(screen, (LIGHT_YELLOW), ((s_boss4_x, s_boss4_y), (100, 100)))    
        
        s_boss1_1_pos = pygame.draw.rect(screen, (LIGHT_YELLOW), ((s_boss1_1_x, s_boss1_y), (100, 100)))    
        s_boss2_1_pos = pygame.draw.rect(screen, (LIGHT_YELLOW), ((s_boss2_1_x, s_boss2_y), (100, 100)))  
        s_boss3_1_pos = pygame.draw.rect(screen, (LIGHT_YELLOW), ((s_boss3_1_x, s_boss3_y), (100, 100)))  
        s_boss4_1_pos = pygame.draw.rect(screen, (LIGHT_YELLOW), ((s_boss4_1_x, s_boss4_y), (100, 100)))    
        
        # intro Animation
        if menu == False and hp > 0 and time_beam_outro == False:
            if s_boss1_x > 1820:
                s_boss1_x -= 2
                s_boss2_x -= 2
                s_boss3_x -= 2
                s_boss4_x -= 2
                
                s_boss1_1_x += 2
                s_boss2_1_x += 2
                s_boss3_1_x += 2
                s_boss4_1_x += 2
                
        # outro Animation
        if menu == False and hp > 0 and time_beam_outro == True:
            if s_boss1_x < 2000:
                s_boss1_x += 2
                s_boss2_x += 2
                s_boss3_x += 2
                s_boss4_x += 2
                
                s_boss1_1_x -= 2
                s_boss2_1_x -= 2
                s_boss3_1_x -= 2
                s_boss4_1_x -= 2
            elif s_boss1_x >= 2000:
                s_boss_end = True

            
        # dmg to player
        if menu == False:
            if (hitbox_player[0] + pl_length in range(s_boss1_pos[0], (s_boss1_pos[0] + 100)) and ((hitbox_player[1] in range((s_boss1_pos[1]), (s_boss1_pos[1] + 100), 1) or hitbox_player[1] + pl_height in range((s_boss1_pos[1]), (s_boss1_pos[1] + 100))))
                or hitbox_player[0] + pl_length in range(s_boss2_pos[0], (s_boss2_pos[0] + 100)) and ((hitbox_player[1] in range((s_boss2_pos[1]), (s_boss2_pos[1] + 100), 1) or hitbox_player[1] + pl_height in range((s_boss2_pos[1]), (s_boss2_pos[1] + 100))))
                or hitbox_player[0] + pl_length in range(s_boss3_pos[0], (s_boss3_pos[0] + 100)) and ((hitbox_player[1] in range((s_boss3_pos[1]), (s_boss3_pos[1] + 100), 1) or hitbox_player[1] + pl_height in range((s_boss3_pos[1]), (s_boss3_pos[1] + 100))))
                or hitbox_player[0] + pl_length in range(s_boss4_pos[0], (s_boss4_pos[0] + 100)) and ((hitbox_player[1] in range((s_boss4_pos[1]), (s_boss4_pos[1] + 100), 1) or hitbox_player[1] + pl_height in range((s_boss4_pos[1]), (s_boss4_pos[1] + 100))))
                
                or hitbox_player[0] in range(s_boss1_1_pos[0], (s_boss1_1_pos[0] + 100)) and ((hitbox_player[1] in range((s_boss1_1_pos[1]), (s_boss1_1_pos[1] + 100), 1) or hitbox_player[1] + pl_height in range((s_boss1_1_pos[1]), (s_boss1_1_pos[1] + 100))))
                or hitbox_player[0] in range(s_boss2_1_pos[0], (s_boss2_1_pos[0] + 100)) and ((hitbox_player[1] in range((s_boss2_1_pos[1]), (s_boss2_1_pos[1] + 100), 1) or hitbox_player[1] + pl_height in range((s_boss2_1_pos[1]), (s_boss2_1_pos[1] + 100))))
                or hitbox_player[0] in range(s_boss3_1_pos[0], (s_boss3_1_pos[0] + 100)) and ((hitbox_player[1] in range((s_boss3_1_pos[1]), (s_boss3_1_pos[1] + 100), 1) or hitbox_player[1] + pl_height in range((s_boss3_1_pos[1]), (s_boss3_1_pos[1] + 100))))
                or hitbox_player[0] in range(s_boss4_1_pos[0], (s_boss4_1_pos[0] + 100)) and ((hitbox_player[1] in range((s_boss4_1_pos[1]), (s_boss4_1_pos[1] + 100), 1) or hitbox_player[1] + pl_height in range((s_boss4_1_pos[1]), (s_boss4_1_pos[1] + 100))))
                
                or hitbox_player[0] in range(s_boss1_beam_pos[0], (s_boss1_beam_pos[0] + 1920)) and ((hitbox_player[1] in range((s_boss1_beam_pos[1]), (s_boss1_beam_pos[1] + 100), 1) or hitbox_player[1] + pl_height in range((s_boss1_beam_pos[1]), (s_boss1_beam_pos[1] + 100))))
                or hitbox_player[0] in range(s_boss2_beam_pos[0], (s_boss2_beam_pos[0] + 1920)) and ((hitbox_player[1] in range((s_boss2_beam_pos[1]), (s_boss2_beam_pos[1] + 100), 1) or hitbox_player[1] + pl_height in range((s_boss2_beam_pos[1]), (s_boss2_beam_pos[1] + 100))))
                or hitbox_player[0] in range(s_boss3_beam_pos[0], (s_boss3_beam_pos[0] + 1920)) and ((hitbox_player[1] in range((s_boss3_beam_pos[1]), (s_boss3_beam_pos[1] + 100), 1) or hitbox_player[1] + pl_height in range((s_boss3_beam_pos[1]), (s_boss3_beam_pos[1] + 100))))
                or hitbox_player[0] in range(s_boss4_beam_pos[0], (s_boss4_beam_pos[0] + 1920)) and ((hitbox_player[1] in range((s_boss4_beam_pos[1]), (s_boss4_beam_pos[1] + 100), 1) or hitbox_player[1] + pl_height in range((s_boss4_beam_pos[1]), (s_boss4_beam_pos[1] + 100))))

            ): # player get hit
                hp = 0
       
        # bullets to sboss
        if bullet1_x in range(s_boss1_pos[0], (s_boss1_pos[0] + 100)) and bullet1_y in range((s_boss1_pos[1]), (s_boss1_pos[1] + 100), 1): 
            bullet1_fly = False
            Bullet1_x = -100
            bullet1_y = -100
        if bullet2_x in range(s_boss1_pos[0], (s_boss1_pos[0] + 100))and bullet2_y in range((s_boss1_pos[1]), (s_boss1_pos[1] + 100), 1): 
            bullet2_fly = False
            Bullet2_x = -100
            bullet2_y = -100
        if bullet3_x in range(s_boss1_pos[0], (s_boss1_pos[0] + 100))and bullet3_y in range((s_boss1_pos[1]), (s_boss1_pos[1] + 100), 1): 
            bullet3_fly = False
            Bullet3_x = -100
            bullet3_y = -100
        if bullet4_x in range(s_boss1_pos[0], (s_boss1_pos[0] + 100))and bullet4_y in range((s_boss1_pos[1]), (s_boss1_pos[1] + 100), 1): 
            bullet4_fly = False
            Bullet4_x = -100
            bullet4_y = -100
        if bullet5_x in range(s_boss1_pos[0], (s_boss1_pos[0] + 100))and bullet5_y in range((s_boss1_pos[1]), (s_boss1_pos[1] + 100), 1): 
            bullet5_fly = False
            Bullet5_x = -100
            bullet5_y = -100
        if bullet6_x in range(s_boss1_pos[0], (s_boss1_pos[0] + 100))and bullet6_y in range((s_boss1_pos[1]), (s_boss1_pos[1] + 100), 1): 
            bullet6_fly = False
            Bullet6_x = -100
            bullet6_y = -100
        if bullet7_x in range(s_boss1_pos[0], (s_boss1_pos[0] + 100))and bullet7_y in range((s_boss1_pos[1]), (s_boss1_pos[1] + 100), 1): 
            bullet7_fly = False
            Bullet7_x = -100
            bullet7_y = -100
        if bullet8_x in range(s_boss1_pos[0], (s_boss1_pos[0] + 100))and bullet8_y in range((s_boss1_pos[1]), (s_boss1_pos[1] + 100), 1): 
            bullet8_fly = False
            Bullet8_x = -100
            bullet8_y = -100
        if bullet9_x in range(s_boss1_pos[0], (s_boss1_pos[0] + 100))and bullet9_y in range((s_boss1_pos[1]), (s_boss1_pos[1] + 100), 1): 
            bullet9_fly = False
            Bullet9_x = -100
            bullet9_y = -100
        if bullet10_x in range(s_boss1_pos[0], (s_boss1_pos[0] + 100))and bullet10_y in range((s_boss1_pos[1]), (s_boss1_pos[1] + 100), 1): 
            bullet10_fly = False
            Bullet10_x = -100
            bullet10_y = -100 
            
        if bullet1_x in range(s_boss2_pos[0], (s_boss2_pos[0] + 100)) and bullet1_y in range((s_boss2_pos[1]), (s_boss2_pos[1] + 100), 1): 
            bullet1_fly = False
            Bullet1_x = -100
            bullet1_y = -100
        if bullet2_x in range(s_boss2_pos[0], (s_boss2_pos[0] + 100))and bullet2_y in range((s_boss2_pos[1]), (s_boss2_pos[1] + 100), 1): 
            bullet2_fly = False
            Bullet2_x = -100
            bullet2_y = -100
        if bullet3_x in range(s_boss2_pos[0], (s_boss2_pos[0] + 100))and bullet3_y in range((s_boss2_pos[1]), (s_boss2_pos[1] + 100), 1): 
            bullet3_fly = False
            Bullet3_x = -100
            bullet3_y = -100
        if bullet4_x in range(s_boss2_pos[0], (s_boss2_pos[0] + 100))and bullet4_y in range((s_boss2_pos[1]), (s_boss2_pos[1] + 100), 1): 
            bullet4_fly = False
            Bullet4_x = -100
            bullet4_y = -100
        if bullet5_x in range(s_boss2_pos[0], (s_boss2_pos[0] + 100))and bullet5_y in range((s_boss2_pos[1]), (s_boss2_pos[1] + 100), 1): 
            bullet5_fly = False
            Bullet5_x = -100
            bullet5_y = -100
        if bullet6_x in range(s_boss2_pos[0], (s_boss2_pos[0] + 100))and bullet6_y in range((s_boss2_pos[1]), (s_boss2_pos[1] + 100), 1): 
            bullet6_fly = False
            Bullet6_x = -100
            bullet6_y = -100
        if bullet7_x in range(s_boss2_pos[0], (s_boss2_pos[0] + 100))and bullet7_y in range((s_boss2_pos[1]), (s_boss2_pos[1] + 100), 1): 
            bullet7_fly = False
            Bullet7_x = -100
            bullet7_y = -100
        if bullet8_x in range(s_boss2_pos[0], (s_boss2_pos[0] + 100))and bullet8_y in range((s_boss2_pos[1]), (s_boss2_pos[1] + 100), 1): 
            bullet8_fly = False
            Bullet8_x = -100
            bullet8_y = -100
        if bullet9_x in range(s_boss2_pos[0], (s_boss2_pos[0] + 100))and bullet9_y in range((s_boss2_pos[1]), (s_boss2_pos[1] + 100), 1): 
            bullet9_fly = False
            Bullet9_x = -100
            bullet9_y = -100
        if bullet10_x in range(s_boss2_pos[0], (s_boss2_pos[0] + 100))and bullet10_y in range((s_boss2_pos[1]), (s_boss2_pos[1] + 100), 1): 
            bullet10_fly = False
            Bullet10_x = -100
            bullet10_y = -100 
            
        if bullet1_x in range(s_boss3_pos[0], (s_boss3_pos[0] + 100)) and bullet1_y in range((s_boss3_pos[1]), (s_boss3_pos[1] + 100), 1): 
            bullet1_fly = False
            Bullet1_x = -100
            bullet1_y = -100
        if bullet2_x in range(s_boss3_pos[0], (s_boss3_pos[0] + 100))and bullet2_y in range((s_boss3_pos[1]), (s_boss3_pos[1] + 100), 1): 
            bullet2_fly = False
            Bullet2_x = -100
            bullet2_y = -100
        if bullet3_x in range(s_boss3_pos[0], (s_boss3_pos[0] + 100))and bullet3_y in range((s_boss3_pos[1]), (s_boss3_pos[1] + 100), 1): 
            bullet3_fly = False
            Bullet3_x = -100
            bullet3_y = -100
        if bullet4_x in range(s_boss3_pos[0], (s_boss3_pos[0] + 100))and bullet4_y in range((s_boss3_pos[1]), (s_boss3_pos[1] + 100), 1): 
            bullet4_fly = False
            Bullet4_x = -100
            bullet4_y = -100
        if bullet5_x in range(s_boss3_pos[0], (s_boss3_pos[0] + 100))and bullet5_y in range((s_boss3_pos[1]), (s_boss3_pos[1] + 100), 1): 
            bullet5_fly = False
            Bullet5_x = -100
            bullet5_y = -100
        if bullet6_x in range(s_boss3_pos[0], (s_boss3_pos[0] + 100))and bullet6_y in range((s_boss3_pos[1]), (s_boss3_pos[1] + 100), 1): 
            bullet6_fly = False
            Bullet6_x = -100
            bullet6_y = -100
        if bullet7_x in range(s_boss3_pos[0], (s_boss3_pos[0] + 100))and bullet7_y in range((s_boss3_pos[1]), (s_boss3_pos[1] + 100), 1): 
            bullet7_fly = False
            Bullet7_x = -100
            bullet7_y = -100
        if bullet8_x in range(s_boss3_pos[0], (s_boss3_pos[0] + 100))and bullet8_y in range((s_boss3_pos[1]), (s_boss3_pos[1] + 100), 1): 
            bullet8_fly = False
            Bullet8_x = -100
            bullet8_y = -100
        if bullet9_x in range(s_boss3_pos[0], (s_boss3_pos[0] + 100))and bullet9_y in range((s_boss3_pos[1]), (s_boss3_pos[1] + 100), 1): 
            bullet9_fly = False
            Bullet9_x = -100
            bullet9_y = -100
        if bullet10_x in range(s_boss3_pos[0], (s_boss3_pos[0] + 100))and bullet10_y in range((s_boss3_pos[1]), (s_boss3_pos[1] + 100), 1): 
            bullet10_fly = False
            Bullet10_x = -100
            bullet10_y = -100 
            
        if bullet1_x in range(s_boss4_pos[0], (s_boss4_pos[0] + 100)) and bullet1_y in range((s_boss4_pos[1]), (s_boss4_pos[1] + 100), 1): 
            bullet1_fly = False
            Bullet1_x = -100
            bullet1_y = -100
        if bullet2_x in range(s_boss4_pos[0], (s_boss4_pos[0] + 100))and bullet2_y in range((s_boss4_pos[1]), (s_boss4_pos[1] + 100), 1): 
            bullet2_fly = False
            Bullet2_x = -100
            bullet2_y = -100
        if bullet3_x in range(s_boss4_pos[0], (s_boss4_pos[0] + 100))and bullet3_y in range((s_boss4_pos[1]), (s_boss4_pos[1] + 100), 1): 
            bullet3_fly = False
            Bullet3_x = -100
            bullet3_y = -100
        if bullet4_x in range(s_boss4_pos[0], (s_boss4_pos[0] + 100))and bullet4_y in range((s_boss4_pos[1]), (s_boss4_pos[1] + 100), 1): 
            bullet4_fly = False
            Bullet4_x = -100
            bullet4_y = -100
        if bullet5_x in range(s_boss4_pos[0], (s_boss4_pos[0] + 100))and bullet5_y in range((s_boss4_pos[1]), (s_boss4_pos[1] + 100), 1): 
            bullet5_fly = False
            Bullet5_x = -100
            bullet5_y = -100
        if bullet6_x in range(s_boss4_pos[0], (s_boss4_pos[0] + 100))and bullet6_y in range((s_boss4_pos[1]), (s_boss4_pos[1] + 100), 1): 
            bullet6_fly = False
            Bullet6_x = -100
            bullet6_y = -100
        if bullet7_x in range(s_boss4_pos[0], (s_boss4_pos[0] + 100))and bullet7_y in range((s_boss4_pos[1]), (s_boss4_pos[1] + 100), 1): 
            bullet7_fly = False
            Bullet7_x = -100
            bullet7_y = -100
        if bullet8_x in range(s_boss4_pos[0], (s_boss4_pos[0] + 100))and bullet8_y in range((s_boss4_pos[1]), (s_boss4_pos[1] + 100), 1): 
            bullet8_fly = False
            Bullet8_x = -100
            bullet8_y = -100
        if bullet9_x in range(s_boss4_pos[0], (s_boss4_pos[0] + 100))and bullet9_y in range((s_boss4_pos[1]), (s_boss4_pos[1] + 100), 1): 
            bullet9_fly = False
            Bullet9_x = -100
            bullet9_y = -100
        if bullet10_x in range(s_boss4_pos[0], (s_boss4_pos[0] + 100))and bullet10_y in range((s_boss4_pos[1]), (s_boss4_pos[1] + 100), 1): 
            bullet10_fly = False
            Bullet10_x = -100
            bullet10_y = -100 
       
       # bullet to beam
        if bullet1_x in range(s_boss1_beam_pos[0], (s_boss1_beam_pos[0] + 1920)) and bullet1_y in range((s_boss1_beam_pos[1]), (s_boss1_beam_pos[1] + 100), 1): 
            bullet1_fly = False
            Bullet1_x = -100
            bullet1_y = -100
        if bullet2_x in range(s_boss1_beam_pos[0], (s_boss1_beam_pos[0] + 1920))and bullet2_y in range((s_boss1_beam_pos[1]), (s_boss1_beam_pos[1] + 100), 1): 
            bullet2_fly = False
            Bullet2_x = -100
            bullet2_y = -100
        if bullet3_x in range(s_boss1_beam_pos[0], (s_boss1_beam_pos[0] + 1920))and bullet3_y in range((s_boss1_beam_pos[1]), (s_boss1_beam_pos[1] + 100), 1): 
            bullet3_fly = False
            Bullet3_x = -100
            bullet3_y = -100
        if bullet4_x in range(s_boss1_beam_pos[0], (s_boss1_beam_pos[0] + 1920))and bullet4_y in range((s_boss1_beam_pos[1]), (s_boss1_beam_pos[1] + 100), 1): 
            bullet4_fly = False
            Bullet4_x = -100
            bullet4_y = -100
        if bullet5_x in range(s_boss1_beam_pos[0], (s_boss1_beam_pos[0] + 1920))and bullet5_y in range((s_boss1_beam_pos[1]), (s_boss1_beam_pos[1] + 100), 1): 
            bullet5_fly = False
            Bullet5_x = -100
            bullet5_y = -100
        if bullet6_x in range(s_boss1_beam_pos[0], (s_boss1_beam_pos[0] + 1920))and bullet6_y in range((s_boss1_beam_pos[1]), (s_boss1_beam_pos[1] + 100), 1): 
            bullet6_fly = False
            Bullet6_x = -100
            bullet6_y = -100
        if bullet7_x in range(s_boss1_beam_pos[0], (s_boss1_beam_pos[0] + 1920))and bullet7_y in range((s_boss1_beam_pos[1]), (s_boss1_beam_pos[1] + 100), 1): 
            bullet7_fly = False
            Bullet7_x = -100
            bullet7_y = -100
        if bullet8_x in range(s_boss1_beam_pos[0], (s_boss1_beam_pos[0] + 1920))and bullet8_y in range((s_boss1_beam_pos[1]), (s_boss1_beam_pos[1] + 100), 1): 
            bullet8_fly = False
            Bullet8_x = -100
            bullet8_y = -100
        if bullet9_x in range(s_boss1_beam_pos[0], (s_boss1_beam_pos[0] + 1920))and bullet9_y in range((s_boss1_beam_pos[1]), (s_boss1_beam_pos[1] + 100), 1): 
            bullet9_fly = False
            Bullet9_x = -100
            bullet9_y = -100
        if bullet10_x in range(s_boss1_beam_pos[0], (s_boss1_beam_pos[0] + 1920))and bullet10_y in range((s_boss1_beam_pos[1]), (s_boss1_beam_pos[1] + 100), 1): 
            bullet10_fly = False
            Bullet10_x = -100
            bullet10_y = -100 
            
        if bullet1_x in range(s_boss2_beam_pos[0], (s_boss2_beam_pos[0] + 1920)) and bullet1_y in range((s_boss2_beam_pos[1]), (s_boss2_beam_pos[1] + 100), 1): 
            bullet1_fly = False
            Bullet1_x = -100
            bullet1_y = -100
        if bullet2_x in range(s_boss2_beam_pos[0], (s_boss2_beam_pos[0] + 1920))and bullet2_y in range((s_boss2_beam_pos[1]), (s_boss2_beam_pos[1] + 100), 1): 
            bullet2_fly = False
            Bullet2_x = -100
            bullet2_y = -100
        if bullet3_x in range(s_boss2_beam_pos[0], (s_boss2_beam_pos[0] + 1920))and bullet3_y in range((s_boss2_beam_pos[1]), (s_boss2_beam_pos[1] + 100), 1): 
            bullet3_fly = False
            Bullet3_x = -100
            bullet3_y = -100
        if bullet4_x in range(s_boss2_beam_pos[0], (s_boss2_beam_pos[0] + 1920))and bullet4_y in range((s_boss2_beam_pos[1]), (s_boss2_beam_pos[1] + 100), 1): 
            bullet4_fly = False
            Bullet4_x = -100
            bullet4_y = -100
        if bullet5_x in range(s_boss2_beam_pos[0], (s_boss2_beam_pos[0] + 1920))and bullet5_y in range((s_boss2_beam_pos[1]), (s_boss2_beam_pos[1] + 100), 1): 
            bullet5_fly = False
            Bullet5_x = -100
            bullet5_y = -100
        if bullet6_x in range(s_boss2_beam_pos[0], (s_boss2_beam_pos[0] + 1920))and bullet6_y in range((s_boss2_beam_pos[1]), (s_boss2_beam_pos[1] + 100), 1): 
            bullet6_fly = False
            Bullet6_x = -100
            bullet6_y = -100
        if bullet7_x in range(s_boss2_beam_pos[0], (s_boss2_beam_pos[0] + 1920))and bullet7_y in range((s_boss2_beam_pos[1]), (s_boss2_beam_pos[1] + 100), 1): 
            bullet7_fly = False
            Bullet7_x = -100
            bullet7_y = -100
        if bullet8_x in range(s_boss2_beam_pos[0], (s_boss2_beam_pos[0] + 1920))and bullet8_y in range((s_boss2_beam_pos[1]), (s_boss2_beam_pos[1] + 100), 1): 
            bullet8_fly = False
            Bullet8_x = -100
            bullet8_y = -100
        if bullet9_x in range(s_boss2_beam_pos[0], (s_boss2_beam_pos[0] + 1920))and bullet9_y in range((s_boss2_beam_pos[1]), (s_boss2_beam_pos[1] + 100), 1): 
            bullet9_fly = False
            Bullet9_x = -100
            bullet9_y = -100
        if bullet10_x in range(s_boss2_beam_pos[0], (s_boss2_beam_pos[0] + 1920))and bullet10_y in range((s_boss2_beam_pos[1]), (s_boss2_beam_pos[1] + 100), 1): 
            bullet10_fly = False
            Bullet10_x = -100
            bullet10_y = -100 
     
        if bullet1_x in range(s_boss3_beam_pos[0], (s_boss3_beam_pos[0] + 1920)) and bullet1_y in range((s_boss3_beam_pos[1]), (s_boss3_beam_pos[1] + 100), 1): 
            bullet1_fly = False
            Bullet1_x = -100
            bullet1_y = -100
        if bullet2_x in range(s_boss3_beam_pos[0], (s_boss3_beam_pos[0] + 1920))and bullet2_y in range((s_boss3_beam_pos[1]), (s_boss3_beam_pos[1] + 100), 1): 
            bullet2_fly = False
            Bullet2_x = -100
            bullet2_y = -100
        if bullet3_x in range(s_boss3_beam_pos[0], (s_boss3_beam_pos[0] + 1920))and bullet3_y in range((s_boss3_beam_pos[1]), (s_boss3_beam_pos[1] + 100), 1): 
            bullet3_fly = False
            Bullet3_x = -100
            bullet3_y = -100
        if bullet4_x in range(s_boss3_beam_pos[0], (s_boss3_beam_pos[0] + 1920))and bullet4_y in range((s_boss3_beam_pos[1]), (s_boss3_beam_pos[1] + 100), 1): 
            bullet4_fly = False
            Bullet4_x = -100
            bullet4_y = -100
        if bullet5_x in range(s_boss3_beam_pos[0], (s_boss3_beam_pos[0] + 1920))and bullet5_y in range((s_boss3_beam_pos[1]), (s_boss3_beam_pos[1] + 100), 1): 
            bullet5_fly = False
            Bullet5_x = -100
            bullet5_y = -100
        if bullet6_x in range(s_boss3_beam_pos[0], (s_boss3_beam_pos[0] + 1920))and bullet6_y in range((s_boss3_beam_pos[1]), (s_boss3_beam_pos[1] + 100), 1): 
            bullet6_fly = False
            Bullet6_x = -100
            bullet6_y = -100
        if bullet7_x in range(s_boss3_beam_pos[0], (s_boss3_beam_pos[0] + 1920))and bullet7_y in range((s_boss3_beam_pos[1]), (s_boss3_beam_pos[1] + 100), 1): 
            bullet7_fly = False
            Bullet7_x = -100
            bullet7_y = -100
        if bullet8_x in range(s_boss3_beam_pos[0], (s_boss3_beam_pos[0] + 1920))and bullet8_y in range((s_boss3_beam_pos[1]), (s_boss3_beam_pos[1] + 100), 1): 
            bullet8_fly = False
            Bullet8_x = -100
            bullet8_y = -100
        if bullet9_x in range(s_boss3_beam_pos[0], (s_boss3_beam_pos[0] + 1920))and bullet9_y in range((s_boss3_beam_pos[1]), (s_boss3_beam_pos[1] + 100), 1): 
            bullet9_fly = False
            Bullet9_x = -100
            bullet9_y = -100
        if bullet10_x in range(s_boss3_beam_pos[0], (s_boss3_beam_pos[0] + 1920))and bullet10_y in range((s_boss3_beam_pos[1]), (s_boss3_beam_pos[1] + 100), 1): 
            bullet10_fly = False
            Bullet10_x = -100
            bullet10_y = -100 
            
        if bullet1_x in range(s_boss4_beam_pos[0], (s_boss4_beam_pos[0] + 1920)) and bullet1_y in range((s_boss4_beam_pos[1]), (s_boss4_beam_pos[1] + 100), 1): 
            bullet1_fly = False
            Bullet1_x = -100
            bullet1_y = -100
        if bullet2_x in range(s_boss4_beam_pos[0], (s_boss4_beam_pos[0] + 1920))and bullet2_y in range((s_boss4_beam_pos[1]), (s_boss4_beam_pos[1] + 100), 1): 
            bullet2_fly = False
            Bullet2_x = -100
            bullet2_y = -100
        if bullet3_x in range(s_boss4_beam_pos[0], (s_boss4_beam_pos[0] + 1920))and bullet3_y in range((s_boss4_beam_pos[1]), (s_boss4_beam_pos[1] + 100), 1): 
            bullet3_fly = False
            Bullet3_x = -100
            bullet3_y = -100
        if bullet4_x in range(s_boss4_beam_pos[0], (s_boss4_beam_pos[0] + 1920))and bullet4_y in range((s_boss4_beam_pos[1]), (s_boss4_beam_pos[1] + 100), 1): 
            bullet4_fly = False
            Bullet4_x = -100
            bullet4_y = -100
        if bullet5_x in range(s_boss4_beam_pos[0], (s_boss4_beam_pos[0] + 1920))and bullet5_y in range((s_boss4_beam_pos[1]), (s_boss4_beam_pos[1] + 100), 1): 
            bullet5_fly = False
            Bullet5_x = -100
            bullet5_y = -100
        if bullet6_x in range(s_boss4_beam_pos[0], (s_boss4_beam_pos[0] + 1920))and bullet6_y in range((s_boss4_beam_pos[1]), (s_boss4_beam_pos[1] + 100), 1): 
            bullet6_fly = False
            Bullet6_x = -100
            bullet6_y = -100
        if bullet7_x in range(s_boss4_beam_pos[0], (s_boss4_beam_pos[0] + 1920))and bullet7_y in range((s_boss4_beam_pos[1]), (s_boss4_beam_pos[1] + 100), 1): 
            bullet7_fly = False
            Bullet7_x = -100
            bullet7_y = -100
        if bullet8_x in range(s_boss4_beam_pos[0], (s_boss4_beam_pos[0] + 1920))and bullet8_y in range((s_boss4_beam_pos[1]), (s_boss4_beam_pos[1] + 100), 1): 
            bullet8_fly = False
            Bullet8_x = -100
            bullet8_y = -100
        if bullet9_x in range(s_boss4_beam_pos[0], (s_boss4_beam_pos[0] + 1920))and bullet9_y in range((s_boss4_beam_pos[1]), (s_boss4_beam_pos[1] + 100), 1): 
            bullet9_fly = False
            Bullet9_x = -100
            bullet9_y = -100
        if bullet10_x in range(s_boss4_beam_pos[0], (s_boss4_beam_pos[0] + 1920))and bullet10_y in range((s_boss4_beam_pos[1]), (s_boss4_beam_pos[1] + 100), 1): 
            bullet10_fly = False
            Bullet10_x = -100
            bullet10_y = -100 
       
    if b_boss == True:
        if rd_walls2 == True:
            pygame.draw.rect(screen, (WALL_COLOR1), ((wall4_x, wall4_y), (wall_width, 200)))  
            pygame.draw.rect(screen, (WALL_COLOR1), ((wall5_x, wall5_y), (wall_width, 200)))  
            pygame.draw.rect(screen, (WALL_COLOR1), ((wall6_x, wall6_y), (wall_width, 200)))  
        b_boss_pos = pygame.draw.rect(screen, (CUBE_COLOR5), ((b_boss_x, b_boss_y), (450, 450)))
        
        if b_boss_hp > 260:
            screen.blit(img_bboss_face3, (b_boss_x, b_boss_y))
            if b_boss_x <= 1420:
                rd_cubes = True
                rd_cubes_hard = False
        elif b_boss_hp > 130:
            screen.blit(img_bboss_face1, (b_boss_x, b_boss_y))
            rd_walls2 = True
        elif b_boss_hp > 1:
            screen.blit(img_bboss_face2, (b_boss_x, b_boss_y))
            phase3 = True
        else:
            screen.blit(img_bboss_face4, (b_boss_x, b_boss_y))
        
        # hp bar
        pygame.draw.rect(screen, (GRAY), ((b_boss_x + 25, b_boss_y - 75), (400, 40)))
        pygame.draw.rect(screen, (D_GRAY), ((b_boss_x + 30, b_boss_y - 70), (390, 30)))
        if b_boss_hp > 0:
            pygame.draw.rect(screen, (GREEN), ((b_boss_x + 30, b_boss_y - 70), (b_boss_hp, 30)))
            
        txt_overlord = font_nametag.render('overlord', False, (WHITE))
        screen.blit(txt_overlord, ((b_boss_x + 133, b_boss_y - 70)))            
        
        
        # Animation
        if menu == False and hp > 0:
            if b_boss_x > 1420:
                b_boss_x -= 2
                cube1_x = random.randrange(0, 1400, (cube_size))    
                cube1_y = random.randrange(-2000, -50, (cube_size))
                cube2_x = random.randrange(0, 1400, (cube_size))    
                cube2_y = random.randrange(-2000, -50, (cube_size))
                cube3_x = random.randrange(0, 1400, (cube_size))    
                cube3_y = random.randrange(-2000, -50, (cube_size))
                cube4_x = random.randrange(0, 1400, (cube_size))    
                cube4_y = random.randrange(-2000, -50, (cube_size))
                
                cube5_x = random.randrange(0, 1400, (cube_size))    
                cube5_y = random.randrange(-2000, -50, (cube_size))
                cube6_x = random.randrange(0, 1400, (cube_size))    
                cube6_y = random.randrange(-2000, -50, (cube_size))
                cube7_x = random.randrange(0, 1400, (cube_size))    
                cube7_y = random.randrange(-2000, -50, (cube_size))
                cube8_x = random.randrange(0, 1400, (cube_size))    
                cube8_y = random.randrange(-2000, -50, (cube_size))
                
                cube9_x = random.randrange(0, 1400, (cube_size))    
                cube9_y = random.randrange(-2000, -50, (cube_size))
                cube10_x = random.randrange(0, 1400, (cube_size))    
                cube10_y = random.randrange(-2000, -50, (cube_size))
                cube11_x = random.randrange(0, 1400, (cube_size))    
                cube11_y = random.randrange(-2000, -50, (cube_size))
                cube12_x = random.randrange(0, 1400, (cube_size))    
                cube12_y = random.randrange(-2000, -50, (cube_size))
                
                cube13_x = random.randrange(0, 1400, (cube_size))    
                cube13_y = random.randrange(-2000, -50, (cube_size))
                cube14_x = random.randrange(0, 1400, (cube_size))    
                cube14_y = random.randrange(-2000, -50, (cube_size))
                cube15_x = random.randrange(0, 1400, (cube_size))    
                cube15_y = random.randrange(-2000, -50, (cube_size))
                cube16_x = random.randrange(0, 1400, (cube_size))    
                cube16_y = random.randrange(-2000, -50, (cube_size))
                
                cube17_x = random.randrange(0, 1400, (cube_size))    
                cube17_y = random.randrange(-2000, -50, (cube_size))
                cube18_x = random.randrange(0, 1400, (cube_size))    
                cube18_y = random.randrange(-2000, -50, (cube_size))
                cube19_x = random.randrange(0, 1400, (cube_size))    
                cube19_y = random.randrange(-2000, -50, (cube_size))
                cube20_x = random.randrange(0, 1400, (cube_size))    
                cube20_y = random.randrange(-2000, -50, (cube_size))
                
                
            time_bboss += 1
            if time_bboss == 61:
                time_bboss = 0
            elif time_bboss > 31:
                b_boss_y += 0.2
            elif time_bboss > 1:
                b_boss_y -= 0.2

        # Phase 3 Beams
        if phase3 == True:
            if menu == False and not b_boss_box_1_y < 0:
                time_box_b_boss += bg_sp
                
                if time_box_b_boss < 750:
                    if b_boss_box_1_x_rand > b_boss_box_1_x:
                        b_boss_box_1_x += 5
                    elif b_boss_box_1_x_rand < b_boss_box_1_x:
                        b_boss_box_1_x -= 5
                        
                    if b_boss_box_2_x_rand > b_boss_box_2_x:
                        b_boss_box_2_x += 5
                    elif b_boss_box_2_x_rand < b_boss_box_2_x:
                        b_boss_box_2_x -= 5

                if time_box_b_boss > 1400:
                    b_boss_beam_1_pos = -1000, -2000
                    b_boss_beam_2_pos = -1000, -2000
                    
                    b_boss_box_1_x_rand = random.randrange(0, 650, (5))
                    b_boss_box_2_x_rand = random.randrange(650, 1300, (5))
                    
                    time_box_b_boss = 0
                elif time_box_b_boss in range(750 ,1400 ,1):
                    b_boss_beam_1_pos = pygame.draw.rect(screen, (CUBE_COLOR5), ((b_boss_box_1_x, b_boss_box_1_y), (100, 1080)))
                    b_boss_beam_2_pos = pygame.draw.rect(screen, (CUBE_COLOR5), ((b_boss_box_2_x, b_boss_box_2_y), (100, 1080)))
                elif time_box_b_boss in range(450, 600 ,1):
                    pygame.draw.rect(screen, (GRAY), ((b_boss_box_1_x, b_boss_box_1_y), (100, 1080)))
                    pygame.draw.rect(screen, (GRAY), ((b_boss_box_2_x, b_boss_box_2_y), (100, 1080)))
                elif time_box_b_boss in range(150, 300 ,1):
                    pygame.draw.rect(screen, (GRAY), ((b_boss_box_1_x, b_boss_box_1_y), (100, 1080)))
                    pygame.draw.rect(screen, (GRAY), ((b_boss_box_2_x, b_boss_box_2_y), (100, 1080)))
                            
            b_boss_box_1_pos = pygame.draw.rect(screen, (LIGHT_YELLOW), ((b_boss_box_1_x, b_boss_box_1_y), (100, 100)))   
            b_boss_box_2_pos = pygame.draw.rect(screen, (LIGHT_YELLOW), ((b_boss_box_2_x, b_boss_box_2_y), (100, 100))) 

            b_boss_box_1_1_pos = pygame.draw.rect(screen, (LIGHT_YELLOW), ((b_boss_box_1_x, b_boss_box_1_1_y), (100, 100)))  
            b_boss_box_2_1_pos = pygame.draw.rect(screen, (LIGHT_YELLOW), ((b_boss_box_2_x, b_boss_box_2_1_y), (100, 100)))
    
            # intro Animation
            if menu == False and hp > 0:
                if b_boss_box_1_y < 0:
                    b_boss_box_1_y += 2
                    b_boss_box_2_y += 2
                    
                    b_boss_box_1_1_y -= 2
                    b_boss_box_2_1_y -= 2
                    
            # dmg to player
            if menu == False:
                if ((hitbox_player[0] in range(b_boss_box_1_pos[0], (b_boss_box_1_pos[0] + 100)) or hitbox_player[0] + pl_length in range(b_boss_box_1_pos[0], (b_boss_box_1_pos[0] + 100))) and ((hitbox_player[1] in range((b_boss_box_1_pos[1]), (b_boss_box_1_pos[1] + 100), 1)))
                    or (hitbox_player[0] in range(b_boss_box_2_pos[0], (b_boss_box_2_pos[0] + 100)) or hitbox_player[0] + pl_length in range(b_boss_box_2_pos[0], (b_boss_box_2_pos[0] + 100))) and ((hitbox_player[1] in range((b_boss_box_2_pos[1]), (b_boss_box_2_pos[1] + 100), 1)))
                    
                    or (hitbox_player[0] in range(b_boss_box_1_1_pos[0], (b_boss_box_1_1_pos[0] + 100)) or hitbox_player[0] + pl_length in range(b_boss_box_1_1_pos[0], (b_boss_box_1_1_pos[0] + 100))) and ((hitbox_player[1] + pl_height in range((b_boss_box_1_1_pos[1]), (b_boss_box_1_1_pos[1] + 100), 1)))
                    or (hitbox_player[0] in range(b_boss_box_2_1_pos[0], (b_boss_box_2_1_pos[0] + 100)) or hitbox_player[0] + pl_length in range(b_boss_box_2_1_pos[0], (b_boss_box_2_1_pos[0] + 100))) and ((hitbox_player[1] + pl_height  in range((b_boss_box_2_1_pos[1]), (b_boss_box_2_1_pos[1] + 100), 1)))
                    
                    or (hitbox_player[0] in range(b_boss_beam_1_pos[0], (b_boss_beam_1_pos[0] + 100)) or hitbox_player[0] + pl_length in range(b_boss_beam_1_pos[0], (b_boss_beam_1_pos[0] + 100))) and ((hitbox_player[1] in range((b_boss_beam_1_pos[1]), (b_boss_beam_1_pos[1] + 1080), 1)))
                    or (hitbox_player[0] in range(b_boss_beam_2_pos[0], (b_boss_beam_2_pos[0] + 100)) or hitbox_player[0] + pl_length in range(b_boss_beam_2_pos[0], (b_boss_beam_2_pos[0] + 100))) and ((hitbox_player[1] in range((b_boss_beam_2_pos[1]), (b_boss_beam_2_pos[1] + 1080), 1)))
                ): # player get hit
                    hp = 0
        
            # bullets to box
            if bullet1_x in range(b_boss_box_1_pos[0], (b_boss_box_1_pos[0] + 100)) and bullet1_y in range((b_boss_box_1_pos[1]), (b_boss_box_1_pos[1] + 100), 1): 
                bullet1_fly = False
                Bullet1_x = -100
                bullet1_y = -100
            if bullet2_x in range(b_boss_box_1_pos[0], (b_boss_box_1_pos[0] + 100))and bullet2_y in range((b_boss_box_1_pos[1]), (b_boss_box_1_pos[1] + 100), 1): 
                bullet2_fly = False
                Bullet2_x = -100
                bullet2_y = -100
            if bullet3_x in range(b_boss_box_1_pos[0], (b_boss_box_1_pos[0] + 100))and bullet3_y in range((b_boss_box_1_pos[1]), (b_boss_box_1_pos[1] + 100), 1): 
                bullet3_fly = False
                Bullet3_x = -100
                bullet3_y = -100
            if bullet4_x in range(b_boss_box_1_pos[0], (b_boss_box_1_pos[0] + 100))and bullet4_y in range((b_boss_box_1_pos[1]), (b_boss_box_1_pos[1] + 100), 1): 
                bullet4_fly = False
                Bullet4_x = -100
                bullet4_y = -100
            if bullet5_x in range(b_boss_box_1_pos[0], (b_boss_box_1_pos[0] + 100))and bullet5_y in range((b_boss_box_1_pos[1]), (b_boss_box_1_pos[1] + 100), 1): 
                bullet5_fly = False
                Bullet5_x = -100
                bullet5_y = -100
            if bullet6_x in range(b_boss_box_1_pos[0], (b_boss_box_1_pos[0] + 100))and bullet6_y in range((b_boss_box_1_pos[1]), (b_boss_box_1_pos[1] + 100), 1): 
                bullet6_fly = False
                Bullet6_x = -100
                bullet6_y = -100
            if bullet7_x in range(b_boss_box_1_pos[0], (b_boss_box_1_pos[0] + 100))and bullet7_y in range((b_boss_box_1_pos[1]), (b_boss_box_1_pos[1] + 100), 1): 
                bullet7_fly = False
                Bullet7_x = -100
                bullet7_y = -100
            if bullet8_x in range(b_boss_box_1_pos[0], (b_boss_box_1_pos[0] + 100))and bullet8_y in range((b_boss_box_1_pos[1]), (b_boss_box_1_pos[1] + 100), 1): 
                bullet8_fly = False
                Bullet8_x = -100
                bullet8_y = -100
            if bullet9_x in range(b_boss_box_1_pos[0], (b_boss_box_1_pos[0] + 100))and bullet9_y in range((b_boss_box_1_pos[1]), (b_boss_box_1_pos[1] + 100), 1): 
                bullet9_fly = False
                Bullet9_x = -100
                bullet9_y = -100
            if bullet10_x in range(b_boss_box_1_pos[0], (b_boss_box_1_pos[0] + 100))and bullet10_y in range((b_boss_box_1_pos[1]), (b_boss_box_1_pos[1] + 100), 1): 
                bullet10_fly = False
                Bullet10_x = -100
                bullet10_y = -100 
                
            if bullet1_x in range(b_boss_box_2_pos[0], (b_boss_box_2_pos[0] + 100)) and bullet1_y in range((b_boss_box_2_pos[1]), (b_boss_box_2_pos[1] + 100), 1): 
                bullet1_fly = False
                Bullet1_x = -100
                bullet1_y = -100
            if bullet2_x in range(b_boss_box_2_pos[0], (b_boss_box_2_pos[0] + 100))and bullet2_y in range((b_boss_box_2_pos[1]), (b_boss_box_2_pos[1] + 100), 1): 
                bullet2_fly = False
                Bullet2_x = -100
                bullet2_y = -100
            if bullet3_x in range(b_boss_box_2_pos[0], (b_boss_box_2_pos[0] + 100))and bullet3_y in range((b_boss_box_2_pos[1]), (b_boss_box_2_pos[1] + 100), 1): 
                bullet3_fly = False
                Bullet3_x = -100
                bullet3_y = -100
            if bullet4_x in range(b_boss_box_2_pos[0], (b_boss_box_2_pos[0] + 100))and bullet4_y in range((b_boss_box_2_pos[1]), (b_boss_box_2_pos[1] + 100), 1): 
                bullet4_fly = False
                Bullet4_x = -100
                bullet4_y = -100
            if bullet5_x in range(b_boss_box_2_pos[0], (b_boss_box_2_pos[0] + 100))and bullet5_y in range((b_boss_box_2_pos[1]), (b_boss_box_2_pos[1] + 100), 1): 
                bullet5_fly = False
                Bullet5_x = -100
                bullet5_y = -100
            if bullet6_x in range(b_boss_box_2_pos[0], (b_boss_box_2_pos[0] + 100))and bullet6_y in range((b_boss_box_2_pos[1]), (b_boss_box_2_pos[1] + 100), 1): 
                bullet6_fly = False
                Bullet6_x = -100
                bullet6_y = -100
            if bullet7_x in range(b_boss_box_2_pos[0], (b_boss_box_2_pos[0] + 100))and bullet7_y in range((b_boss_box_2_pos[1]), (b_boss_box_2_pos[1] + 100), 1): 
                bullet7_fly = False
                Bullet7_x = -100
                bullet7_y = -100
            if bullet8_x in range(b_boss_box_2_pos[0], (b_boss_box_2_pos[0] + 100))and bullet8_y in range((b_boss_box_2_pos[1]), (b_boss_box_2_pos[1] + 100), 1): 
                bullet8_fly = False
                Bullet8_x = -100
                bullet8_y = -100
            if bullet9_x in range(b_boss_box_2_pos[0], (b_boss_box_2_pos[0] + 100))and bullet9_y in range((b_boss_box_2_pos[1]), (b_boss_box_2_pos[1] + 100), 1): 
                bullet9_fly = False
                Bullet9_x = -100
                bullet9_y = -100
            if bullet10_x in range(b_boss_box_2_pos[0], (b_boss_box_2_pos[0] + 100))and bullet10_y in range((b_boss_box_2_pos[1]), (b_boss_box_2_pos[1] + 100), 1): 
                bullet10_fly = False
                Bullet10_x = -100
                bullet10_y = -100 
                
                
            if bullet1_x in range(b_boss_box_1_1_pos[0], (b_boss_box_1_1_pos[0] + 100)) and bullet1_y in range((b_boss_box_1_1_pos[1]), (b_boss_box_1_1_pos[1] + 100), 1): 
                bullet1_fly = False
                Bullet1_x = -100
                bullet1_y = -100
            if bullet2_x in range(b_boss_box_1_1_pos[0], (b_boss_box_1_1_pos[0] + 100))and bullet2_y in range((b_boss_box_1_1_pos[1]), (b_boss_box_1_1_pos[1] + 100), 1): 
                bullet2_fly = False
                Bullet2_x = -100
                bullet2_y = -100
            if bullet3_x in range(b_boss_box_1_1_pos[0], (b_boss_box_1_1_pos[0] + 100))and bullet3_y in range((b_boss_box_1_1_pos[1]), (b_boss_box_1_1_pos[1] + 100), 1): 
                bullet3_fly = False
                Bullet3_x = -100
                bullet3_y = -100
            if bullet4_x in range(b_boss_box_1_1_pos[0], (b_boss_box_1_1_pos[0] + 100))and bullet4_y in range((b_boss_box_1_1_pos[1]), (b_boss_box_1_1_pos[1] + 100), 1): 
                bullet4_fly = False
                Bullet4_x = -100
                bullet4_y = -100
            if bullet5_x in range(b_boss_box_1_1_pos[0], (b_boss_box_1_1_pos[0] + 100))and bullet5_y in range((b_boss_box_1_1_pos[1]), (b_boss_box_1_1_pos[1] + 100), 1): 
                bullet5_fly = False
                Bullet5_x = -100
                bullet5_y = -100
            if bullet6_x in range(b_boss_box_1_1_pos[0], (b_boss_box_1_1_pos[0] + 100))and bullet6_y in range((b_boss_box_1_1_pos[1]), (b_boss_box_1_1_pos[1] + 100), 1): 
                bullet6_fly = False
                Bullet6_x = -100
                bullet6_y = -100
            if bullet7_x in range(b_boss_box_1_1_pos[0], (b_boss_box_1_1_pos[0] + 100))and bullet7_y in range((b_boss_box_1_1_pos[1]), (b_boss_box_1_1_pos[1] + 100), 1): 
                bullet7_fly = False
                Bullet7_x = -100
                bullet7_y = -100
            if bullet8_x in range(b_boss_box_1_1_pos[0], (b_boss_box_1_1_pos[0] + 100))and bullet8_y in range((b_boss_box_1_1_pos[1]), (b_boss_box_1_1_pos[1] + 100), 1): 
                bullet8_fly = False
                Bullet8_x = -100
                bullet8_y = -100
            if bullet9_x in range(b_boss_box_1_1_pos[0], (b_boss_box_1_1_pos[0] + 100))and bullet9_y in range((b_boss_box_1_1_pos[1]), (b_boss_box_1_1_pos[1] + 100), 1): 
                bullet9_fly = False
                Bullet9_x = -100
                bullet9_y = -100
            if bullet10_x in range(b_boss_box_1_1_pos[0], (b_boss_box_1_1_pos[0] + 100))and bullet10_y in range((b_boss_box_1_1_pos[1]), (b_boss_box_1_1_pos[1] + 100), 1): 
                bullet10_fly = False
                Bullet10_x = -100
                bullet10_y = -100 
                
            if bullet1_x in range(b_boss_box_2_1_pos[0], (b_boss_box_2_1_pos[0] + 100)) and bullet1_y in range((b_boss_box_2_1_pos[1]), (b_boss_box_2_1_pos[1] + 100), 1): 
                bullet1_fly = False
                Bullet1_x = -100
                bullet1_y = -100
            if bullet2_x in range(b_boss_box_2_1_pos[0], (b_boss_box_2_1_pos[0] + 100))and bullet2_y in range((b_boss_box_2_1_pos[1]), (b_boss_box_2_1_pos[1] + 100), 1): 
                bullet2_fly = False
                Bullet2_x = -100
                bullet2_y = -100
            if bullet3_x in range(b_boss_box_2_1_pos[0], (b_boss_box_2_1_pos[0] + 100))and bullet3_y in range((b_boss_box_2_1_pos[1]), (b_boss_box_2_1_pos[1] + 100), 1): 
                bullet3_fly = False
                Bullet3_x = -100
                bullet3_y = -100
            if bullet4_x in range(b_boss_box_2_1_pos[0], (b_boss_box_2_1_pos[0] + 100))and bullet4_y in range((b_boss_box_2_1_pos[1]), (b_boss_box_2_1_pos[1] + 100), 1): 
                bullet4_fly = False
                Bullet4_x = -100
                bullet4_y = -100
            if bullet5_x in range(b_boss_box_2_1_pos[0], (b_boss_box_2_1_pos[0] + 100))and bullet5_y in range((b_boss_box_2_1_pos[1]), (b_boss_box_2_1_pos[1] + 100), 1): 
                bullet5_fly = False
                Bullet5_x = -100
                bullet5_y = -100
            if bullet6_x in range(b_boss_box_2_1_pos[0], (b_boss_box_2_1_pos[0] + 100))and bullet6_y in range((b_boss_box_2_1_pos[1]), (b_boss_box_2_1_pos[1] + 100), 1): 
                bullet6_fly = False
                Bullet6_x = -100
                bullet6_y = -100
            if bullet7_x in range(b_boss_box_2_1_pos[0], (b_boss_box_2_1_pos[0] + 100))and bullet7_y in range((b_boss_box_2_1_pos[1]), (b_boss_box_2_1_pos[1] + 100), 1): 
                bullet7_fly = False
                Bullet7_x = -100
                bullet7_y = -100
            if bullet8_x in range(b_boss_box_2_1_pos[0], (b_boss_box_2_1_pos[0] + 100))and bullet8_y in range((b_boss_box_2_1_pos[1]), (b_boss_box_2_1_pos[1] + 100), 1): 
                bullet8_fly = False
                Bullet8_x = -100
                bullet8_y = -100
            if bullet9_x in range(b_boss_box_2_1_pos[0], (b_boss_box_2_1_pos[0] + 100))and bullet9_y in range((b_boss_box_2_1_pos[1]), (b_boss_box_2_1_pos[1] + 100), 1): 
                bullet9_fly = False
                Bullet9_x = -100
                bullet9_y = -100
            if bullet10_x in range(b_boss_box_2_1_pos[0], (b_boss_box_2_1_pos[0] + 100))and bullet10_y in range((b_boss_box_2_1_pos[1]), (b_boss_box_2_1_pos[1] + 100), 1): 
                bullet10_fly = False
                Bullet10_x = -100
                bullet10_y = -100 
                
        
        # bullet to beam
            if bullet1_x in range(b_boss_beam_1_pos[0], (b_boss_beam_1_pos[0] + 100)) and bullet1_y in range((b_boss_beam_1_pos[1]), (b_boss_beam_1_pos[1] + 1080), 1): 
                bullet1_fly = False
                Bullet1_x = -100
                bullet1_y = -100
            if bullet2_x in range(b_boss_beam_1_pos[0], (b_boss_beam_1_pos[0] + 100))and bullet2_y in range((b_boss_beam_1_pos[1]), (b_boss_beam_1_pos[1] + 1080), 1): 
                bullet2_fly = False
                Bullet2_x = -100
                bullet2_y = -100
            if bullet3_x in range(b_boss_beam_1_pos[0], (b_boss_beam_1_pos[0] + 100))and bullet3_y in range((b_boss_beam_1_pos[1]), (b_boss_beam_1_pos[1] + 1080), 1): 
                bullet3_fly = False
                Bullet3_x = -100
                bullet3_y = -100
            if bullet4_x in range(b_boss_beam_1_pos[0], (b_boss_beam_1_pos[0] + 100))and bullet4_y in range((b_boss_beam_1_pos[1]), (b_boss_beam_1_pos[1] + 1080), 1): 
                bullet4_fly = False
                Bullet4_x = -100
                bullet4_y = -100
            if bullet5_x in range(b_boss_beam_1_pos[0], (b_boss_beam_1_pos[0] + 100))and bullet5_y in range((b_boss_beam_1_pos[1]), (b_boss_beam_1_pos[1] + 1080), 1): 
                bullet5_fly = False
                Bullet5_x = -100
                bullet5_y = -100
            if bullet6_x in range(b_boss_beam_1_pos[0], (b_boss_beam_1_pos[0] + 100))and bullet6_y in range((b_boss_beam_1_pos[1]), (b_boss_beam_1_pos[1] + 1080), 1): 
                bullet6_fly = False
                Bullet6_x = -100
                bullet6_y = -100
            if bullet7_x in range(b_boss_beam_1_pos[0], (b_boss_beam_1_pos[0] + 100))and bullet7_y in range((b_boss_beam_1_pos[1]), (b_boss_beam_1_pos[1] + 1080), 1): 
                bullet7_fly = False
                Bullet7_x = -100
                bullet7_y = -100
            if bullet8_x in range(b_boss_beam_1_pos[0], (b_boss_beam_1_pos[0] + 100))and bullet8_y in range((b_boss_beam_1_pos[1]), (b_boss_beam_1_pos[1] + 1080), 1): 
                bullet8_fly = False
                Bullet8_x = -100
                bullet8_y = -100
            if bullet9_x in range(b_boss_beam_1_pos[0], (b_boss_beam_1_pos[0] + 100))and bullet9_y in range((b_boss_beam_1_pos[1]), (b_boss_beam_1_pos[1] + 1080), 1): 
                bullet9_fly = False
                Bullet9_x = -100
                bullet9_y = -100
            if bullet10_x in range(b_boss_beam_1_pos[0], (b_boss_beam_1_pos[0] + 100))and bullet10_y in range((b_boss_beam_1_pos[1]), (b_boss_beam_1_pos[1] + 1080), 1): 
                bullet10_fly = False
                Bullet10_x = -100
                bullet10_y = -100 
                
            if bullet1_x in range(b_boss_beam_2_pos[0], (b_boss_beam_2_pos[0] + 100)) and bullet1_y in range((b_boss_beam_2_pos[1]), (b_boss_beam_2_pos[1] + 1080), 1): 
                bullet1_fly = False
                Bullet1_x = -100
                bullet1_y = -100
            if bullet2_x in range(b_boss_beam_2_pos[0], (b_boss_beam_2_pos[0] + 100))and bullet2_y in range((b_boss_beam_2_pos[1]), (b_boss_beam_2_pos[1] + 1080), 1): 
                bullet2_fly = False
                Bullet2_x = -100
                bullet2_y = -100
            if bullet3_x in range(b_boss_beam_2_pos[0], (b_boss_beam_2_pos[0] + 100))and bullet3_y in range((b_boss_beam_2_pos[1]), (b_boss_beam_2_pos[1] + 1080), 1): 
                bullet3_fly = False
                Bullet3_x = -100
                bullet3_y = -100
            if bullet4_x in range(b_boss_beam_2_pos[0], (b_boss_beam_2_pos[0] + 100))and bullet4_y in range((b_boss_beam_2_pos[1]), (b_boss_beam_2_pos[1] + 1080), 1): 
                bullet4_fly = False
                Bullet4_x = -100
                bullet4_y = -100
            if bullet5_x in range(b_boss_beam_2_pos[0], (b_boss_beam_2_pos[0] + 100))and bullet5_y in range((b_boss_beam_2_pos[1]), (b_boss_beam_2_pos[1] + 1080), 1): 
                bullet5_fly = False
                Bullet5_x = -100
                bullet5_y = -100
            if bullet6_x in range(b_boss_beam_2_pos[0], (b_boss_beam_2_pos[0] + 100))and bullet6_y in range((b_boss_beam_2_pos[1]), (b_boss_beam_2_pos[1] + 1080), 1): 
                bullet6_fly = False
                Bullet6_x = -100
                bullet6_y = -100
            if bullet7_x in range(b_boss_beam_2_pos[0], (b_boss_beam_2_pos[0] + 100))and bullet7_y in range((b_boss_beam_2_pos[1]), (b_boss_beam_2_pos[1] + 1080), 1): 
                bullet7_fly = False
                Bullet7_x = -100
                bullet7_y = -100
            if bullet8_x in range(b_boss_beam_2_pos[0], (b_boss_beam_2_pos[0] + 100))and bullet8_y in range((b_boss_beam_2_pos[1]), (b_boss_beam_2_pos[1] + 1080), 1): 
                bullet8_fly = False
                Bullet8_x = -100
                bullet8_y = -100
            if bullet9_x in range(b_boss_beam_2_pos[0], (b_boss_beam_2_pos[0] + 100))and bullet9_y in range((b_boss_beam_2_pos[1]), (b_boss_beam_2_pos[1] + 1080), 1): 
                bullet9_fly = False
                Bullet9_x = -100
                bullet9_y = -100
            if bullet10_x in range(b_boss_beam_2_pos[0], (b_boss_beam_2_pos[0] + 100))and bullet10_y in range((b_boss_beam_2_pos[1]), (b_boss_beam_2_pos[1] + 1080), 1): 
                bullet10_fly = False
                Bullet10_x = -100
                bullet10_y = -100 
                
    
    
  
        # Phase 1 cubes
        if rd_cubes == True and menu == False:
            cube1_y += round(bg_sp * (cube1_y_rd/10))
            cube2_y += round(bg_sp * (cube2_y_rd/10))
            cube3_y += round(bg_sp * (cube3_y_rd/10))
            cube4_y += round(bg_sp * (cube4_y_rd/10))
            
            cube5_y += round(bg_sp * (cube5_y_rd/10))
            cube6_y += round(bg_sp * (cube6_y_rd/10))
            cube7_y += round(bg_sp * (cube7_y_rd/10))
            cube8_y += round(bg_sp * (cube8_y_rd/10))
            
            cube9_y += round(bg_sp * (cube9_y_rd/10))
            cube10_y += round(bg_sp * (cube10_y_rd/10))
            cube11_y += round(bg_sp * (cube11_y_rd/10))
            cube12_y += round(bg_sp * (cube12_y_rd/10))
            
            cube13_y += round(bg_sp * (cube13_y_rd/10))
            cube14_y += round(bg_sp * (cube14_y_rd/10))
            cube15_y += round(bg_sp * (cube15_y_rd/10))
            cube16_y += round(bg_sp * (cube16_y_rd/10))
            
            cube17_y += round(bg_sp * (cube17_y_rd/10))
            cube18_y += round(bg_sp * (cube18_y_rd/10))
            cube19_y += round(bg_sp * (cube19_y_rd/10))
            cube20_y += round(bg_sp * (cube20_y_rd/10))
            
            if (cube1_y >= 1000 or cube1_hp <= 0) and (cube_rs == True):
                cube1_hp = cube_hp1
                cube1_y_rd = random.randrange(3, 7, (1))
                cube1_x = random.randrange(0, 1400, (cube_size))    
                cube1_y = random.randrange(-2000, -50, (cube_size))
            if (cube2_y >= 1000 or cube2_hp <= 0) and (cube_rs == True):
                cube2_hp = cube_hp1
                cube2_y_rd = random.randrange(3, 7, (1))
                cube2_x = random.randrange(0, 1400, (cube_size))      
                cube2_y = random.randrange(-2000, -50, (cube_size))
            if (cube3_y >= 1000 or cube3_hp <= 0) and (cube_rs == True):
                cube3_hp = cube_hp1
                cube3_y_rd = random.randrange(3, 7, (1))
                cube3_x = random.randrange(0, 1400, (cube_size))       
                cube3_y = random.randrange(-2000, -50, (cube_size))
            if (cube4_y >= 1000 or cube4_hp <= 0) and (cube_rs == True):
                cube4_hp = cube_hp1
                cube4_y_rd = random.randrange(3, 7, (1))
                cube4_x = random.randrange(0, 1400, (cube_size))      
                cube4_y = random.randrange(-2000, -50, (cube_size))
                
            if (cube5_y >= 1000 or cube5_hp <= 0) and (cube_rs == True):
                cube5_hp = cube_hp2
                cube5_y_rd = random.randrange(3, 7, (1))
                cube5_x = random.randrange(0, 1400, (cube_size))    
                cube5_y = random.randrange(-2000, -50, (cube_size))
            if (cube6_y >= 1000 or cube6_hp <= 0) and (cube_rs == True):
                cube6_hp = cube_hp2
                cube6_y_rd = random.randrange(3, 7, (1))
                cube6_x = random.randrange(0, 1400, (cube_size))      
                cube6_y = random.randrange(-2000, -50, (cube_size))
            if (cube7_y >= 1000 or cube7_hp <= 0) and (cube_rs == True):
                cube7_hp = cube_hp2
                cube7_y_rd = random.randrange(3, 7, (1))
                cube7_x = random.randrange(0, 1400, (cube_size))       
                cube7_y = random.randrange(-2000, -50, (cube_size))
            if (cube8_y >= 1000 or cube8_hp <= 0) and (cube_rs == True):
                cube8_hp = cube_hp2
                cube8_y_rd = random.randrange(3, 7, (1))
                cube8_x = random.randrange(0, 1400, (cube_size))      
                cube8_y = random.randrange(-2000, -50, (cube_size))
                
            if (cube9_y >= 1000 or cube9_hp <= 0) and (cube_rs == True):
                cube9_hp = cube_hp3
                cube9_y_rd = random.randrange(3, 7, (1))
                cube9_x = random.randrange(0, 1400, (cube_size))    
                cube9_y = random.randrange(-2000, -50, (cube_size))
            if (cube10_y >= 1000 or cube10_hp <= 0) and (cube_rs == True):
                cube10_hp = cube_hp3
                cube10_y_rd = random.randrange(3, 7, (1))
                cube10_x = random.randrange(0, 1400, (cube_size))      
                cube10_y = random.randrange(-2000, -50, (cube_size))
            if (cube11_y >= 1000 or cube11_hp <= 0) and (cube_rs == True):
                cube11_hp = cube_hp3
                cube11_y_rd = random.randrange(3, 7, (1))
                cube11_x = random.randrange(0, 1400, (cube_size))       
                cube11_y = random.randrange(-2000, -50, (cube_size))
            if (cube12_y >= 1000 or cube12_hp <= 0) and (cube_rs == True):
                cube12_hp = cube_hp3
                cube12_y_rd = random.randrange(3, 7, (1))
                cube12_x = random.randrange(0, 1400, (cube_size))      
                cube12_y = random.randrange(-2000, -50, (cube_size))
                
            if (cube13_y >= 1000 or cube13_hp <= 0) and (cube_rs == True):
                cube13_hp = cube_hp4
                cube13_y_rd = random.randrange(3, 7, (1))
                cube13_x = random.randrange(0, 1400, (cube_size))    
                cube13_y = random.randrange(-2000, -50, (cube_size))
            if (cube14_y >= 1000 or cube14_hp <= 0) and (cube_rs == True):
                cube14_hp = cube_hp4
                cube14_y_rd = random.randrange(3, 7, (1))
                cube14_x = random.randrange(0, 1400, (cube_size))      
                cube14_y = random.randrange(-2000, -50, (cube_size))
            if (cube15_y >= 1000 or cube15_hp <= 0) and (cube_rs == True):
                cube15_hp = cube_hp4
                cube15_y_rd = random.randrange(3, 7, (1))
                cube15_x = random.randrange(0, 1400, (cube_size))       
                cube15_y = random.randrange(-2000, -50, (cube_size))
            if (cube16_y >= 1000 or cube16_hp <= 0) and (cube_rs == True):
                cube16_hp = cube_hp4
                cube16_y_rd = random.randrange(3, 7, (1))
                cube16_x = random.randrange(0, 1400, (cube_size))      
                cube16_y = random.randrange(-2000, -50, (cube_size))
                
            if (cube17_y >= 1000 or cube17_hp <= 0) and (cube_rs == True):
                cube17_hp = cube_hp5
                cube17_y_rd = random.randrange(3, 7, (1))
                cube17_x = random.randrange(0, 1400, (cube_size))    
                cube17_y = random.randrange(-2000, -50, (cube_size))
            if (cube18_y >= 1000 or cube18_hp <= 0) and (cube_rs == True):
                cube18_hp = cube_hp5
                cube18_y_rd = random.randrange(3, 7, (1))
                cube18_x = random.randrange(0, 1400, (cube_size))      
                cube18_y = random.randrange(-2000, -50, (cube_size))
            if (cube19_y >= 1000 or cube19_hp <= 0) and (cube_rs == True):
                cube19_hp = cube_hp5
                cube19_y_rd = random.randrange(3, 7, (1))
                cube19_x = random.randrange(0, 1400, (cube_size))       
                cube19_y = random.randrange(-2000, -50, (cube_size))
            if (cube20_y >= 1000 or cube20_hp <= 0) and (cube_rs == True):
                cube20_hp = cube_hp5
                cube20_y_rd = random.randrange(3, 7, (1))
                cube20_x = random.randrange(0, 1400, (cube_size))      
                cube20_y = random.randrange(-2000, -50, (cube_size))
    
  
        # Phase 2 walls
        if rd_walls2 == True and menu == False:
            
            if time_rd_walls2 < 2 and menu == False and b_boss == False:
                time_rd_walls2 += 1
            if time_rd_walls2 == 1 and menu == False and b_boss == False:
                wall4_x = -150
                wall4_y = random.randrange(0, 900, (150))
                    
                wall5_x = -790
                wall5_y = random.randrange(0, 900, (150))
                    
                wall6_x = -1430
                wall6_y = random.randrange(0, 900, (150))
            
            
            # wall move right
            if menu == False and hp > 0:
                wall4_x += bg_sp
                wall5_x += bg_sp
                wall6_x += bg_sp
                
            if (wall4_x >= 1920) and (wall_rs == True):
                wall4_x = -150
                wall4_y = random.randrange(0, 900, (150))

            if (wall5_x >= 1920) and (wall_rs == True):
                wall5_x = -150
                wall5_y = random.randrange(0, 900, (150))
                if wall4_x == -200:
                    wall5_x = -790

            if (wall6_x >= 1920) and (wall_rs == True):
                wall6_x = -150
                wall6_y = random.randrange(0, 900, (150))
                if wall4_x == -200:
                    wall6_x = -1430
                

            
            # bullet to walls
            if bullet1_x in range(wall4_x, (wall4_x + 150)) and bullet1_y in range(wall4_y, (wall4_y + 200), 1): 
                bullet1_fly = False
                Bullet1_x = -100
                bullet1_y = -100
            if bullet2_x in range(wall4_x, (wall4_x + 150)) and bullet2_y in range(wall4_y, (wall4_y + 200), 1): 
                bullet2_fly = False
                Bullet2_x = -100
                bullet2_y = -100
            if bullet3_x in range(wall4_x, (wall4_x + 150)) and bullet3_y in range(wall4_y, (wall4_y + 200), 1): 
                bullet3_fly = False
                Bullet3_x = -100
                bullet3_y = -100
            if bullet4_x in range(wall4_x, (wall4_x + 150)) and bullet4_y in range(wall4_y, (wall4_y + 200), 1): 
                bullet4_fly = False
                Bullet4_x = -100
                bullet4_y = -100
            if bullet5_x in range(wall4_x, (wall4_x + 150)) and bullet5_y in range(wall4_y, (wall4_y + 200), 1): 
                bullet5_fly = False
                Bullet5_x = -100
                bullet5_y = -100
            if bullet6_x in range(wall4_x, (wall4_x + 150)) and bullet6_y in range(wall4_y, (wall4_y + 200), 1): 
                bullet6_fly = False
                Bullet6_x = -100
                bullet6_y = -100
            if bullet7_x in range(wall4_x, (wall4_x + 150)) and bullet7_y in range(wall4_y, (wall4_y + 200), 1): 
                bullet7_fly = False
                Bullet7_x = -100
                bullet7_y = -100
            if bullet8_x in range(wall4_x, (wall4_x + 150)) and bullet8_y in range(wall4_y, (wall4_y + 200), 1): 
                bullet8_fly = False
                Bullet8_x = -100
                bullet8_y = -100
            if bullet9_x in range(wall4_x, (wall4_x + 150)) and bullet9_y in range(wall4_y, (wall4_y + 200), 1): 
                bullet9_fly = False
                Bullet9_x = -100
                bullet9_y = -100
            if bullet10_x in range(wall4_x, (wall4_x + 150)) and bullet10_y in range(wall4_y, (wall4_y + 200), 1): 
                bullet10_fly = False
                Bullet10_x = -100
                bullet10_y = -100
             
            if bullet1_x in range(wall5_x, (wall5_x + 150)) and bullet1_y in range(wall5_y, (wall5_y + 200), 1): 
                bullet1_fly = False
                Bullet1_x = -100
                bullet1_y = -100
            if bullet2_x in range(wall5_x, (wall5_x + 150)) and bullet2_y in range(wall5_y, (wall5_y + 200), 1): 
                bullet2_fly = False
                Bullet2_x = -100
                bullet2_y = -100
            if bullet3_x in range(wall5_x, (wall5_x + 150)) and bullet3_y in range(wall5_y, (wall5_y + 200), 1): 
                bullet3_fly = False
                Bullet3_x = -100
                bullet3_y = -100
            if bullet4_x in range(wall5_x, (wall5_x + 150)) and bullet4_y in range(wall5_y, (wall5_y + 200), 1): 
                bullet4_fly = False
                Bullet4_x = -100
                bullet4_y = -100
            if bullet5_x in range(wall5_x, (wall5_x + 150)) and bullet5_y in range(wall5_y, (wall5_y + 200), 1): 
                bullet5_fly = False
                Bullet5_x = -100
                bullet5_y = -100
            if bullet6_x in range(wall5_x, (wall5_x + 150)) and bullet6_y in range(wall5_y, (wall5_y + 200), 1): 
                bullet6_fly = False
                Bullet6_x = -100
                bullet6_y = -100
            if bullet7_x in range(wall5_x, (wall5_x + 150)) and bullet7_y in range(wall5_y, (wall5_y + 200), 1): 
                bullet7_fly = False
                Bullet7_x = -100
                bullet7_y = -100
            if bullet8_x in range(wall5_x, (wall5_x + 150)) and bullet8_y in range(wall5_y, (wall5_y + 200), 1): 
                bullet8_fly = False
                Bullet8_x = -100
                bullet8_y = -100
            if bullet9_x in range(wall5_x, (wall5_x + 150)) and bullet9_y in range(wall5_y, (wall5_y + 200), 1): 
                bullet9_fly = False
                Bullet9_x = -100
                bullet9_y = -100
            if bullet10_x in range(wall5_x, (wall5_x + 150)) and bullet10_y in range(wall5_y, (wall5_y + 200), 1): 
                bullet10_fly = False
                Bullet10_x = -100
                bullet10_y = -100
                
            if bullet1_x in range(wall6_x, (wall6_x + 150)) and bullet1_y in range(wall6_y, (wall6_y + 200), 1): 
                bullet1_fly = False
                Bullet1_x = -100
                bullet1_y = -100
            if bullet2_x in range(wall6_x, (wall6_x + 150)) and bullet2_y in range(wall6_y, (wall6_y + 200), 1): 
                bullet2_fly = False
                Bullet2_x = -100
                bullet2_y = -100
            if bullet3_x in range(wall6_x, (wall6_x + 150)) and bullet3_y in range(wall6_y, (wall6_y + 200), 1): 
                bullet3_fly = False
                Bullet3_x = -100
                bullet3_y = -100
            if bullet4_x in range(wall6_x, (wall6_x + 150)) and bullet4_y in range(wall6_y, (wall6_y + 200), 1): 
                bullet4_fly = False
                Bullet4_x = -100
                bullet4_y = -100
            if bullet5_x in range(wall6_x, (wall6_x + 150)) and bullet5_y in range(wall6_y, (wall6_y + 200), 1): 
                bullet5_fly = False
                Bullet5_x = -100
                bullet5_y = -100
            if bullet6_x in range(wall6_x, (wall6_x + 150)) and bullet6_y in range(wall6_y, (wall6_y + 200), 1): 
                bullet6_fly = False
                Bullet6_x = -100
                bullet6_y = -100
            if bullet7_x in range(wall6_x, (wall6_x + 150)) and bullet7_y in range(wall6_y, (wall6_y + 200), 1): 
                bullet7_fly = False
                Bullet7_x = -100
                bullet7_y = -100
            if bullet8_x in range(wall6_x, (wall6_x + 150)) and bullet8_y in range(wall6_y, (wall6_y + 200), 1): 
                bullet8_fly = False
                Bullet8_x = -100
                bullet8_y = -100
            if bullet9_x in range(wall6_x, (wall6_x + 150)) and bullet9_y in range(wall6_y, (wall6_y + 200), 1): 
                bullet9_fly = False
                Bullet9_x = -100
                bullet9_y = -100
            if bullet10_x in range(wall6_x, (wall6_x + 150)) and bullet10_y in range(wall6_y, (wall6_y + 200), 1): 
                bullet10_fly = False
                Bullet10_x = -100
                bullet10_y = -100
             
            
            # wall x to player
            if hitbox_player[1] in range(wall4_y - pl_height, (wall4_y + 200), 1) and (hitbox_player[0]) in range(wall4_x + 70, (wall4_x + 100)):
                pl_x += bg_sp
                sp_x = 0
            if hitbox_player[1] in range(wall5_y - pl_height, (wall5_y + 200), 1) and (hitbox_player[0]) in range(wall5_x + 70, (wall5_x + 100)):
                pl_x += bg_sp
                sp_x = 0
            if hitbox_player[1] in range(wall6_y - pl_height, (wall6_y + 200), 1) and (hitbox_player[0]) in range(wall6_x + 70, (wall6_x + 100)):
                pl_x += bg_sp
                sp_x = 0
                
            # resets wall x if not in wall
            if (not (hitbox_player[1] in range(wall4_y - pl_height, (wall4_y + 200), 1) and (hitbox_player[0]) in range(wall4_x + 70, (wall4_x + 100))) 
                and not (hitbox_player[1] in range(wall5_y - pl_height, (wall5_y + 200), 1) and (hitbox_player[0]) in range(wall5_x + 70, (wall5_x + 100)))
                and not (hitbox_player[1] in range(wall6_y - pl_height, (wall6_y + 200), 1) and (hitbox_player[0]) in range(wall6_x + 70, (wall6_x + 100)))
                ):
                sp_x = sp_x_save
                
                
                
            # wall to player y up
            if (hitbox_player[0]) in range(wall4_x - pl_height -50, (wall4_x + 150)) and hitbox_player[1] in range(wall4_y + 150, (wall4_y + 200), 1):
                sp_y_up = 0
            if (hitbox_player[0]) in range(wall5_x - pl_height -50, (wall5_x + 150)) and hitbox_player[1] in range(wall5_y + 150, (wall5_y + 200), 1):
                sp_y_up = 0
            if (hitbox_player[0]) in range(wall6_x - pl_height -50, (wall6_x + 150)) and hitbox_player[1] in range(wall6_y + 150, (wall6_y + 200), 1):
                sp_y_up = 0
                
            
            # # resets wall y up if not in wall
            if (not ((hitbox_player[0]) in range(wall4_x - pl_length, (wall4_x + 150)) and hitbox_player[1] in range(wall4_y + 150, (wall4_y + 200), 1))
                and not ((hitbox_player[0]) in range(wall5_x - pl_length, (wall5_x + 150)) and hitbox_player[1] in range(wall5_y + 150, (wall5_y + 200), 1))
                and not ((hitbox_player[0]) in range(wall6_x - pl_length, (wall6_x + 150)) and hitbox_player[1] in range(wall6_y + 150, (wall6_y + 200), 1))
                ):
                sp_y_up = sp_y_up_save
                
                
            # wall to player down
            if (hitbox_player[0]) in range(wall4_x - pl_height -50, (wall4_x + 150)) and hitbox_player[1] in range(wall4_y - pl_height, (wall4_y - pl_height + 50), 1):
                sp_y_down = 0
            if (hitbox_player[0]) in range(wall5_x - pl_height -50, (wall5_x + 150)) and hitbox_player[1] in range(wall5_y - pl_height, (wall5_y - pl_height + 50), 1):
                sp_y_down = 0
            if (hitbox_player[0]) in range(wall6_x - pl_height -50, (wall6_x + 150)) and hitbox_player[1] in range(wall6_y - pl_height, (wall6_y - pl_height + 50), 1):
                sp_y_down = 0
                
            
            # # resets wall y down if not in wall
            if (not ((hitbox_player[0]) in range(wall4_x - pl_length, (wall4_x + 150)) and hitbox_player[1] in range(wall4_y - pl_height, (wall4_y - pl_height + 50), 1))
                and not ((hitbox_player[0]) in range(wall5_x - pl_length, (wall5_x + 150)) and hitbox_player[1] in range(wall5_y - pl_height, (wall5_y - pl_height + 50), 1))
                and not ((hitbox_player[0]) in range(wall6_x - pl_length, (wall6_x + 150)) and hitbox_player[1] in range(wall6_y - pl_height, (wall6_y - pl_height + 50), 1))
                ):
                sp_y_down = sp_y_down_save                
                


        
        # bboss dmg to player
        if menu == False:
            if hitbox_player[0] + pl_length in range(b_boss_pos[0], (b_boss_pos[0] + 450)) and ((hitbox_player[1] in range((b_boss_pos[1]), (b_boss_pos[1] + 450), 1) or hitbox_player[1] + pl_height in range((b_boss_pos[1]), (b_boss_pos[1] + 450)))): # player get hit
                hp = 0
        
        
        # bboss get dmg
        if bullet1_x in range(b_boss_pos[0], (b_boss_pos[0] + 450)) and bullet1_y in range((b_boss_pos[1]), (b_boss_pos[1] + 450), 1): 
            bullet1_fly = False
            Bullet1_x = -100
            bullet1_y = -100
            b_boss_hp -= 1
        if bullet2_x in range(b_boss_pos[0], (b_boss_pos[0] + 450))and bullet2_y in range((b_boss_pos[1]), (b_boss_pos[1] + 450), 1): 
            bullet2_fly = False
            Bullet2_x = -100
            bullet2_y = -100
            b_boss_hp -= 1
        if bullet3_x in range(b_boss_pos[0], (b_boss_pos[0] + 450))and bullet3_y in range((b_boss_pos[1]), (b_boss_pos[1] + 450), 1): 
            bullet3_fly = False
            Bullet3_x = -100
            bullet3_y = -100
            b_boss_hp -= 1
        if bullet4_x in range(b_boss_pos[0], (b_boss_pos[0] + 450))and bullet4_y in range((b_boss_pos[1]), (b_boss_pos[1] + 450), 1): 
            bullet4_fly = False
            Bullet4_x = -100
            bullet4_y = -100
            b_boss_hp -= 1
        if bullet5_x in range(b_boss_pos[0], (b_boss_pos[0] + 450))and bullet5_y in range((b_boss_pos[1]), (b_boss_pos[1] + 450), 1): 
            bullet5_fly = False
            Bullet5_x = -100
            bullet5_y = -100
            b_boss_hp -= 1
        if bullet6_x in range(b_boss_pos[0], (b_boss_pos[0] + 450))and bullet6_y in range((b_boss_pos[1]), (b_boss_pos[1] + 450), 1): 
            bullet6_fly = False
            Bullet6_x = -100
            bullet6_y = -100
            b_boss_hp -= 2
        if bullet7_x in range(b_boss_pos[0], (b_boss_pos[0] + 450))and bullet7_y in range((b_boss_pos[1]), (b_boss_pos[1] + 450), 1): 
            bullet7_fly = False
            Bullet7_x = -100
            bullet7_y = -100
            b_boss_hp -= 1
        if bullet8_x in range(b_boss_pos[0], (b_boss_pos[0] + 450))and bullet8_y in range((b_boss_pos[1]), (b_boss_pos[1] + 450), 1): 
            bullet8_fly = False
            Bullet8_x = -100
            bullet8_y = -100
            b_boss_hp -= 1
        if bullet9_x in range(b_boss_pos[0], (b_boss_pos[0] + 450))and bullet9_y in range((b_boss_pos[1]), (b_boss_pos[1] + 450), 1): 
            bullet9_fly = False
            Bullet9_x = -100
            bullet9_y = -100
            b_boss_hp -= 1
        if bullet10_x in range(b_boss_pos[0], (b_boss_pos[0] + 450))and bullet10_y in range((b_boss_pos[1]), (b_boss_pos[1] + 450), 1): 
            bullet10_fly = False
            Bullet10_x = -100
            bullet10_y = -100 
            b_boss_hp -= 1
            

    ##################################
    #         Ordering Rounds        #
    ##################################
    if Round == 1:
        rd_cubes = True
        cube_rs = True
        b_boss_x = 2000
        b_boss_y = 300
        if menu == False:
            time_round += 1
            pygame.mouse.set_cursor(pygame.SYSTEM_CURSOR_ARROW)
        b_boss_finished = False
        rd_walls2 = False
        bullets = True
        time_rd_walls = 0
        time_rd_walls2 = 0
        if time_round > time_round_max:
            cube_rs = False
        if ((cube1_x < -cube_size)
            and (cube2_x < -cube_size)
            and (cube3_x < -cube_size)
            and (cube4_x < -cube_size)
            and (cube5_x < -cube_size)
            and (cube6_x < -cube_size)
            and (cube7_x < -cube_size)
            and (cube8_x < -cube_size)
            and (cube9_x < -cube_size)
            and (cube10_x < -cube_size)
            and (cube11_x < -cube_size)
            and (cube12_x < -cube_size)
            and (cube13_x < -cube_size)
            and (cube14_x < -cube_size)
            and (cube15_x < -cube_size)
            and (cube16_x < -cube_size)
            and (cube17_x < -cube_size)
            and (cube18_x < -cube_size)
            and (cube19_x < -cube_size)
            and (cube20_x < -cube_size)
            and (time_round > 100)
            ):
            rd_cubes = False
            time_round = 0
            Round = 2
            
            
    elif Round == 2:
        rd_walls = True
        wall_rs = True
        rd_walls2 = False
        time_rd_cubes = 0
        time_rd_walls2 = 0
        b_boss_x = 2000
        b_boss_y = 300
        if menu == False:
            time_round += 1
            pygame.mouse.set_cursor(pygame.SYSTEM_CURSOR_ARROW)
        b_boss_finished = False
        bullets = True
        if time_round > time_round_max:
            wall_rs = False
            s_boss1_x = 2000
            s_boss1_y = 0

            s_boss2_x = 2000
            s_boss2_y = 282

            s_boss3_x = 2000
            s_boss3_y = 562

            s_boss4_x = 2000
            s_boss4_y = 846

            s_boss1_1_x = -180
            s_boss2_1_x = -180
            s_boss3_1_x = -180
            s_boss4_1_x = -180

            s_boss1_beam_pos = 0, - 1000
            s_boss2_beam_pos = 0, - 1000
            s_boss3_beam_pos = 0, - 1000
            s_boss4_beam_pos = 0, - 1000

            time_beam = 0
            time_beam_outro = False
            s_boss_end = False
            
        if ((wall1_x < -wall_width)
              and (wall2_x < -wall_width)
              and (wall3_x < -wall_width)
              and (time_round > 100)
              ):
            rd_walls = False
            time_round = 0
            Round = 3
            
    
    elif Round == 3:
        s_boss = True
        bullets = True
        rd_walls2 = False
        time_rd_cubes = 0
        time_rd_walls = 0
        time_rd_walls2 = 0 
        b_boss_x = 2000
        b_boss_y = 300
        if menu == False:
            time_round += 1
            pygame.mouse.set_cursor(pygame.SYSTEM_CURSOR_ARROW)
        if s_boss_end == True:
            time_round = 0
            s_boss_end = False
            time_beam_outro = False
            s_boss = False
            Round = 4            


    elif Round == 4:
        rd_cubes = True
        rd_cubes_hard = True
        cube_rs = True
        rd_walls2 = False
        time_rd_walls = 0
        time_rd_walls2 = 0
        b_boss_x = 2000
        b_boss_y = 300
        if menu == False:
            time_round += 1
            pygame.mouse.set_cursor(pygame.SYSTEM_CURSOR_ARROW)
        b_boss_finished = False
        bullets = True
        if time_round > time_round_max:
            cube_rs = False
        if ((cube1_x < -cube_size)
            and (cube2_x < -cube_size)
            and (cube3_x < -cube_size)
            and (cube4_x < -cube_size)
            and (cube5_x < -cube_size)
            and (cube6_x < -cube_size)
            and (cube7_x < -cube_size)
            and (cube8_x < -cube_size)
            and (cube9_x < -cube_size)
            and (cube10_x < -cube_size)
            and (cube11_x < -cube_size)
            and (cube12_x < -cube_size)
            and (cube13_x < -cube_size)
            and (cube14_x < -cube_size)
            and (cube15_x < -cube_size)
            and (cube16_x < -cube_size)
            and (cube17_x < -cube_size)
            and (cube18_x < -cube_size)
            and (cube19_x < -cube_size)
            and (cube20_x < -cube_size)
            and (time_round > 100)
            ):
            rd_cubes = False
            time_round = 0
            rd_cubes_hard = False
            Round = 5    
            
            
    elif Round == 5:
        rd_walls = True
        rd_walls_hard = True
        wall_rs = True
        rd_walls2 = False
        time_round += 1
        b_boss_finished = False
        bullets = True
        time_rd_cubes = 0
        time_rd_walls2 = 0
        b_boss_x = 2000
        b_boss_y = 300
        if menu == False:
            pygame.mouse.set_cursor(pygame.SYSTEM_CURSOR_ARROW)
        if time_round > time_round_max:
            wall_rs = False
        if ((wall1_x < -wall_width)
              and (wall2_x < -wall_width)
              and (wall3_x < -wall_width)
              and (time_round > 100)
              ):
            rd_walls = False
            rd_walls_hard = False
            time_round = 0
            Round = 6
            # phase 3 
            wall4_x = -150
            wall4_y = random.randrange(0, 900, (150))
                                
            wall5_x = -790
            wall5_y = random.randrange(0, 900, (150))
                                
            wall6_x = -1430
            wall6_y = random.randrange(0, 900, (150))

            phase3 = False
            b_boss_hp = 390

            b_boss_box_1_x = 500
            b_boss_box_1_y = -100

            b_boss_box_2_x = 1000
            b_boss_box_2_y = -100

            b_boss_box_1_1_y = 950
            b_boss_box_2_1_y = 950

            b_boss_beam_1_pos = -1000, -2000
            b_boss_beam_2_pos = -1000, -2000

            time_box_b_boss = 0
            time_box_outro_b_boss = False
            b_boss_end = False

            b_boss_box_1_x_rand = random.randrange(0, 650, (5))
            b_boss_box_2_x_rand = random.randrange(650, 1300, (5))
            

    elif Round == 6:
        b_boss = True
        bullets = True
        time_rd_cubes = 0
        time_rd_walls = 0
        if menu == False:
            pygame.mouse.set_cursor(pygame.SYSTEM_CURSOR_ARROW)
        if b_boss_finished == True:
            time_round = 0
            b_boss = False
            bg_sp += bg_sp_multi
            Round = 1

                                          
    ##################################
    #             Player             #
    ##################################    
    player = screen.blit(ship, (pl_x - 10, pl_y -35))
    

    ##################################
    #         Player get dmg         #
    ################################## 
    if pl_get_dmg == True:
        invulnerable = True
        if invulnerable_time in range(1, 5, 1) or invulnerable_time in range(10, 15, 1) or invulnerable_time in range(20, 25, 1) or invulnerable_time in range(30, 35, 1) and invulnerable_time in range(40, 45, 1):
            screen.blit(ship_DMG, (pl_x - 10, pl_y -35))
        if invulnerable_time == 1:
            hp -= 1
            pygame.mixer.Sound.play(pl_get_dmg_sound)
        if invulnerable == True and invulnerable_time < 45:
            invulnerable_time += 1
        else:
            invulnerable_time = 0
            invulnerable = False
            pl_get_dmg = False
    
    
    ##################################
    #            Bullets             #
    ################################## 
    if bullets == True:
        if pressed[pygame.K_SPACE] and shooting == False and menu == False:
            pygame.mixer.Sound.play(laser)
            if bullet1_fly == False:
                bullet1_x = pl_x + 115
                bullet1_y = pl_y + 13
                bullet1_fly = True
                shooting = True
            elif bullet2_fly == False:
                bullet2_x = pl_x + 115
                bullet2_y = pl_y + 13
                bullet2_fly = True
                shooting = True
            elif bullet3_fly == False:
                bullet3_x = pl_x + 115
                bullet3_y = pl_y + 13
                bullet3_fly = True
                shooting = True
            elif bullet4_fly == False:
                bullet4_x = pl_x + 115
                bullet4_y = pl_y + 13
                bullet4_fly = True
                shooting = True
            elif bullet5_fly == False:
                bullet5_x = pl_x + 115
                bullet5_y = pl_y + 13
                bullet5_fly = True
                shooting = True
            elif bullet6_fly == False:
                bullet6_x = pl_x + 115
                bullet6_y = pl_y + 13
                bullet6_fly = True
                shooting = True
            elif bullet7_fly == False:
                bullet7_x = pl_x + 115
                bullet7_y = pl_y + 13
                bullet7_fly = True
                shooting = True
            elif bullet8_fly == False:
                bullet8_x = pl_x + 115
                bullet8_y = pl_y + 13
                bullet8_fly = True
                shooting = True
            elif bullet9_fly == False:
                bullet9_x = pl_x + 115
                bullet9_y = pl_y + 13
                bullet9_fly = True
                shooting = True
                    
        if bullet1_fly == True:
            pygame.draw.rect(screen, (BULLET_COLOR), ((bullet1_x, bullet1_y), (bullet_len, 4)))
            if menu == False:
                bullet1_x += bullet_sp
            if bullet1_x > 1930:
                bullet1_fly = False
                Bullet1_x = -100
        if bullet2_fly == True:
            pygame.draw.rect(screen, (BULLET_COLOR), ((bullet2_x, bullet2_y), (bullet_len, 4)))
            if menu == False:
                bullet2_x += bullet_sp
            if bullet2_x > 1930:
                bullet2_fly = False
                Bullet2_x = -100
        if bullet3_fly == True:
            pygame.draw.rect(screen, (BULLET_COLOR), ((bullet3_x, bullet3_y), (bullet_len, 4)))
            if menu == False:
                bullet3_x += bullet_sp
            if bullet3_x > 1930:
                bullet3_fly = False
                Bullet3_x = -100
        if bullet4_fly == True:
            pygame.draw.rect(screen, (BULLET_COLOR), ((bullet4_x, bullet4_y), (bullet_len, 4)))
            if menu == False:
                bullet4_x += bullet_sp
            if bullet4_x > 1930:
                bullet4_fly = False
                Bullet4_x = -100
        if bullet5_fly == True:
            pygame.draw.rect(screen, (BULLET_COLOR), ((bullet5_x, bullet5_y), (bullet_len, 4)))
            if menu == False:
                bullet5_x += bullet_sp
            if bullet5_x > 1930:
                bullet5_fly = False
                Bullet5_x = -100
        if bullet6_fly == True:
            pygame.draw.rect(screen, (BULLET_COLOR), ((bullet6_x, bullet6_y), (bullet_len, 4)))
            if menu == False:
                bullet6_x += bullet_sp
            if bullet6_x > 1930:
                bullet6_fly = False
                Bullet6_x = -100
        if bullet7_fly == True:
            pygame.draw.rect(screen, (BULLET_COLOR), ((bullet7_x, bullet7_y), (bullet_len, 4)))
            if menu == False:
                bullet7_x += bullet_sp
            if bullet7_x > 1930:
                bullet7_fly = False
                Bullet7_x = -100
        if bullet8_fly == True:
            pygame.draw.rect(screen, (BULLET_COLOR), ((bullet8_x, bullet8_y), (bullet_len, 4)))
            if menu == False:
                bullet8_x += bullet_sp
            if bullet8_x > 1930:
                bullet8_fly = False
                Bullet8_x = -100
        if bullet9_fly == True:
            pygame.draw.rect(screen, (BULLET_COLOR), ((bullet9_x, bullet9_y), (bullet_len, 4)))
            if menu == False:
                bullet9_x += bullet_sp
            if bullet9_x > 1930:
                bullet9_fly = False
                Bullet9_x = -100
        if bullet10_fly == True:
            pygame.draw.rect(screen, (BULLET_COLOR), ((bullet10_x, bullet10_y), (bullet_len, 4)))
            if menu == False:
                bullet10_x += bullet_sp
            if bullet10_x > 1930:
                bullet10_fly = False
                Bullet10_x = -100

    ##################################
    #           Game menu           #
    ################################## 
    if menu == True:
        sp_x = 0
        sp_y_up = 0
        sp_y_down = 0
        pygame.draw.rect(screen, (BLUE), ((500, 50), (920, 850))) # Background
        
        pygame.draw.rect(screen, (WHITE), ((500, 50), (920, 5)))   # Border top
        pygame.draw.rect(screen, (WHITE), ((500, 50), (5, 850)))    # Border left
        pygame.draw.rect(screen, (WHITE), ((500, 900), (925, 5)))    # Border bottom
        pygame.draw.rect(screen, (WHITE), ((1420, 50), (5, 850)))   # Border right
        
        
        # title
        pygame.draw.rect(screen, (CYAN), ((505, 55), (915, 95)))   # title color
        pygame.draw.rect(screen, (WHITE), ((500, 150), (920, 5)))   # Border title
        
        txt_gamename = font_progress.render('SPACE FORCE', False, (WHITE))
        screen.blit(txt_gamename, ( 675 , 66))
        
        # Highscore
        pygame.draw.rect(screen, (LIGHT_YELLOW), ((550, 200), (820, 450)))   # title color       
        pygame.draw.rect(screen, (D_GRAY3), ((550, 200), (820, 50)))   # title color    


        if hs_1 == True:
            pygame.draw.rect(screen, (GREEN), ((555,250), (810,75)))

        if hs_2 == True:
            pygame.draw.rect(screen, (GREEN), ((555,325), (810,85)))
            
        if hs_3 == True:
            pygame.draw.rect(screen, (GREEN), ((555,410), (810,85)))
            
        if hs_4 == True:
            pygame.draw.rect(screen, (GREEN), ((555,490), (810,85)))            
        
        if hs_5 == True:
            pygame.draw.rect(screen, (GREEN), ((555,575), (810,75)))  
        
        pygame.draw.rect(screen, (WHITE), ((550, 250), (820, 5)))   # Border highscore top
        pygame.draw.rect(screen, (GRAY), ((550, 323), (820, 5)))   # Border highscore 1
        pygame.draw.rect(screen, (GRAY), ((550, 406), (820, 5)))   # Border highscore 2
        pygame.draw.rect(screen, (GRAY), ((550, 489), (820, 5)))   # Border highscore 3        
        pygame.draw.rect(screen, (GRAY), ((550, 572), (820, 5)))   # Border highscore 3        
                
        pygame.draw.rect(screen, (WHITE), ((550, 200), (820, 5)))   # Border top
        pygame.draw.rect(screen, (WHITE), ((550, 200), (5, 450)))   # Border left
        pygame.draw.rect(screen, (WHITE), ((1365, 200), (5, 450)))   # Border right
        pygame.draw.rect(screen, (WHITE), ((550, 650), (820, 5)))   # Border bottom

        txt_hs = font_score.render('HIGHSCORE', False, (WHITE))
        screen.blit(txt_hs, (598 , 210))
        
        txt_1 = font_gamename.render('1.', False, (D_GRAY3))
        screen.blit(txt_1, (610 , 265))
        txt_hs_ = font_gamename.render('--', False, (D_GRAY2))
        screen.blit(txt_hs_, (680 , 265))# divider before date
        
        txt_2 = font_gamename.render('2.', False, (D_GRAY3))
        screen.blit(txt_2, (600 , 345))
        screen.blit(txt_hs_, (680 , 345))# divider before date

        txt_3 = font_gamename.render('3.', False, (D_GRAY3))
        screen.blit(txt_3, (600 , 428))
        screen.blit(txt_hs_, (680 , 428))# divider before date
    
        txt_4 = font_gamename.render('4.', False, (D_GRAY3))
        screen.blit(txt_4, (600 , 510))
        screen.blit(txt_hs_, (680 , 510))# divider before date
            
        txt_5 = font_gamename.render('5.', False, (D_GRAY3))
        screen.blit(txt_5, (600 , 590))
        screen.blit(txt_hs_, (680 , 590))  # divider before date
    
        screen.blit(txt_hs_, (1070 , 265))  # divider before score
        screen.blit(txt_hs_, (1070 , 345))   # divider before score     
        screen.blit(txt_hs_, (1070 , 428))   # divider before score
        screen.blit(txt_hs_, (1070 , 510))  # divider before score
        screen.blit(txt_hs_, (1070 , 590))  # divider before score
        
        
        # highscore score
        txt_hs_s_1 = font_gamename.render(str(hs_s_1), False, (D_GRAY3))
        screen.blit(txt_hs_s_1, (1160 , 265))

        txt_hs_s_2 = font_gamename.render(str(hs_s_2), False, (D_GRAY3))
        screen.blit(txt_hs_s_2, (1160 , 345))
        
        txt_hs_s_3 = font_gamename.render(str(hs_s_3), False, (D_GRAY3))
        screen.blit(txt_hs_s_3, (1160 , 428))

        txt_hs_s_4 = font_gamename.render(str(hs_s_4), False, (D_GRAY3))
        screen.blit(txt_hs_s_4, (1160 , 510))
          
        txt_hs_s_5 = font_gamename.render(str(hs_s_5), False, (D_GRAY3))
        screen.blit(txt_hs_s_5, (1160 , 590))
        
        # highscore name
        txt_hs_n_1 = font_gamename.render(str(hs_n_1), False, (D_GRAY3))
        txt_hs_n_1_len = txt_hs_n_1.get_width()
        screen.blit(txt_hs_n_1, ((893 - (txt_hs_n_1_len/2)) , 265))

        txt_hs_n_2 = font_gamename.render(str(hs_n_2), False, (D_GRAY3))
        txt_hs_n_2_len = txt_hs_n_2.get_width()
        screen.blit(txt_hs_n_2, ((893 - (txt_hs_n_2_len/2)) , 345))
        
        txt_hs_n_3 = font_gamename.render(str(hs_n_3), False, (D_GRAY3))
        txt_hs_n_3_len = txt_hs_n_3.get_width()
        screen.blit(txt_hs_n_3, ((893 - (txt_hs_n_3_len/2)), 428))

        txt_hs_n_4 = font_gamename.render(str(hs_n_4), False, (D_GRAY3))
        txt_hs_n_4_len = txt_hs_n_4.get_width()
        screen.blit(txt_hs_n_4, ((893 - (txt_hs_n_4_len/2)), 510))
          
        txt_hs_n_5 = font_gamename.render(str(hs_n_5), False, (D_GRAY3))
        txt_hs_n_5_len = txt_hs_n_5.get_width()
        screen.blit(txt_hs_n_5, ((893 - (txt_hs_n_5_len/2)), 590))
        
        
        # button new game
        button_settings = pygame.draw.rect(screen, (BUTTON3), ((1332, 70), (60, 60)))
        if settings_ == True or death == True:
            button_settings = -1000, -1000

        if settings_ == False or death == True:
            time_button2 += 1
            mute_music = -1000,-1000
            v1_music = -1000,-1000
            v2_music = -1000,-1000
            v3_music = -1000,-1000
            v4_music = -1000,-1000
            mute_effect = -1000,-1000
            v1_effect = -1000,-1000
            v2_effect = -1000,-1000
            v3_effect = -1000,-1000
            v4_effect = -1000,-1000
            
        if time_button2 > 10: 
            if (pos[0] in range (button_settings[0], button_settings[0] + 60) and pos[1] in range(button_settings[1], button_settings[1] + 60)):
                pygame.draw.rect(screen, (BUTTON4), ((1332, 70), (60, 60)))
                if event.type == pygame.MOUSEBUTTONUP:
                    settings_ = True
                    time_button2 = 0
                    time_button = 0
                    pygame.event.post(pygame.event.Event(pygame.K_l))

        
        pygame.draw.rect(screen, (WHITE), ((1332, 70), (60, 5)))
        pygame.draw.rect(screen, (WHITE), ((1332, 70), (5, 60)))
        pygame.draw.rect(screen, (WHITE), ((1332, 125), (60, 5)))
        pygame.draw.rect(screen, (WHITE), ((1392, 70), (5, 60)))
        screen.blit(settings, (1344, 80))
        
        
        button_newgame = pygame.draw.rect(screen, (BUTTON), ((620, 720), (300, 70)))
        button_resume = -1000,-1000
        button_back = -1000, -1000
        button_death =  -1000, -1000
        button_ok = -1000,-1000
        if settings_ == True:
            button_newgame = -1000, -1000
            button_back = pygame.draw.rect(screen, (D_GRAY4), ((1332, 70), (60, 60)))
        
        if death == True:
            button_newgame = -1000, -1000
            button_death = pygame.draw.rect(screen, (BUTTON), ((620, 790), (680, 70)))
        
        if (hs_1 or hs_2 or hs_3 or hs_4 or hs_5) == True and death == True and player_name_len > 40:
            button_ok = pygame.draw.rect(screen, (BUTTON), ((1313, 795), (55, 55)))

        if (hs_1 or hs_2 or hs_3 or hs_4 or hs_5) == True:
            button_death = (-1000, -1000)
        
        
        pygame.draw.rect(screen, (D_GRAY2), ((1000, 720), (300, 70)))
        txt_resume = font_score.render('Resume', False, (D_GRAY))
        if Round > 0:
            sp_bg = 0
            button_resume = pygame.draw.rect(screen, (BUTTON), ((1000, 720), (300, 70)))
            txt_resume = font_score.render('Resume', False, (WHITE))

        if settings_ == True or death == True:
            button_resume = -1000, -1000
            
        if pos[0] in range (button_newgame[0], button_newgame[0] + 300) and pos[1] in range(button_newgame[1], button_newgame[1] + 70):
            pygame.draw.rect(screen, (BUTTON2), ((620, 720), (300, 70)))
            if event.type == pygame.MOUSEBUTTONUP:
                Round = 1
                score = 0
                bg_sp = 11
                sp_bg = 10
                time_round = 0
                menu = False
                pl_x = 145          # starting x position of the player
                pl_y = 500          # starting y position of the player
                resume = False
                time_hp = 0
                death = False
                time_rd_cubes = 0
                time_rd_walls = 0
                time_rd_walls2 = 0
                
                hs_1 = False
                hs_2 = False
                hs_3 = False
                hs_4 = False
                hs_5 = False
                
                time_button = 0
                time_button2 = 0
                
                sp_x = sp_x_save
                sp_y_up = sp_y_up_save
                sp_y_down = sp_y_down_save
                bg_sp = 11
                
                rd_cubes = False
                rd_cubes_hard = False
                rd_walls = False
                rd_walls_hard = False
                s_boss = False
                b_boss = False
                
                hp = 3
                
                # bullets
                bullet1_fly = False
                Bullet1_x = -100
                bullet2_fly = False
                Bullet2_x = -100
                bullet3_fly = False
                Bullet3_x = -100
                bullet4_fly = False
                Bullet4_x = -100
                bullet5_fly = False
                Bullet5_x = -100
                bullet6_fly = False
                Bullet6_x = -100
                bullet7_fly = False
                Bullet7_x = -100
                bullet8_fly = False
                Bullet8_x = -100
                bullet9_fly = False
                Bullet9_x = -100
                bullet10_fly = False
                Bullet10_x = -100
                
                # phase 3 bboss
                
                wall4_x = -150
                wall4_y = random.randrange(0, 900, (150))
                                    
                wall5_x = -790
                wall5_y = random.randrange(0, 900, (150))
                                    
                wall6_x = -1430
                wall6_y = random.randrange(0, 900, (150))

                phase3 = False
                
                b_boss_hp = 390

                b_boss_box_1_x = 500
                b_boss_box_1_y = -100

                b_boss_box_2_x = 1000
                b_boss_box_2_y = -100

                b_boss_box_1_1_y = 950
                b_boss_box_2_1_y = 950

                b_boss_beam_1_pos = -1000, -2000
                b_boss_beam_2_pos = -1000, -2000

                time_box_b_boss = 0
                time_box_outro_b_boss = False
                b_boss_end = False

                b_boss_box_1_x_rand = random.randrange(0, 650, (5))
                b_boss_box_2_x_rand = random.randrange(650, 1300, (5))
                
                # walls
                wall1_x = 1920
                wall1_y = random.randrange(-1010, -250, (150))
                wall2_x = 2560
                wall2_y = random.randrange(-1010, -250, (150))
                wall3_x = 3200
                wall3_y = random.randrange(-1010, -250, (150))
                door2_str = 1
                
                # walls hard
                wall1_y_move_up = 0
                wall2_y_move_up = 0
                wall3_y_move_up = 0
                wall1_y_move_down = 0
                wall2_y_move_down = 0
                wall3_y_move_down = 0
                time_wall = 0
                wall_rs = True

                # bboss
                b_boss_finished = False
                b_boss_hp = 390
                
                # rd_cubes_hard
                cube1_y_move = 0
                cube2_y_move = 0
                cube3_y_move = 0
                cube4_y_move = 0

                cube5_y_move = 0
                cube6_y_move = 0
                cube7_y_move = 0
                cube8_y_move = 0

                cube9_y_move = 0
                cube10_y_move = 0
                cube11_y_move = 0
                cube12_y_move = 0

                cube13_y_move = 0
                cube14_y_move = 0
                cube15_y_move = 0
                cube16_y_move = 0

                cube17_y_move = 0
                cube18_y_move = 0
                cube19_y_move = 0
                cube20_y_move = 0

                time_cube = 0
                cube_rs = True
                
                # cubes
                cube_size =  50
                cube_hp1 = 1
                cube_hp2 = 2
                cube_hp3 = 3
                cube_hp4 = 4
                cube_hp5 = 5

                cube1_hp, cube2_hp, cube3_hp, cube4_hp = cube_hp1, cube_hp1, cube_hp1, cube_hp1
                cube5_hp, cube6_hp, cube7_hp, cube8_hp = cube_hp2, cube_hp2, cube_hp2, cube_hp2
                cube9_hp, cube10_hp, cube11_hp, cube12_hp = cube_hp3, cube_hp3, cube_hp3, cube_hp3
                cube13_hp, cube14_hp, cube15_hp, cube16_hp = cube_hp4, cube_hp4, cube_hp4, cube_hp4
                cube17_hp, cube18_hp, cube19_hp, cube20_hp = cube_hp5, cube_hp5, cube_hp5, cube_hp5

                cube1_x = random.randrange(1920, 3840, (cube_size))    
                cube1_y = random.randrange(0, 945, (cube_size))
                cube2_x = random.randrange(1920, 3840, (cube_size))    
                cube2_y = random.randrange(0, 945, (cube_size))
                cube3_x = random.randrange(1920, 3840, (cube_size))    
                cube3_y = random.randrange(0, 945, (cube_size))
                cube4_x = random.randrange(1920, 3840, (cube_size))    
                cube4_y = random.randrange(0, 945, (cube_size))


                cube5_x = random.randrange(1920, 3840, (cube_size))    
                cube5_y = random.randrange(0, 945, (cube_size))
                cube6_x = random.randrange(1920, 3840, (cube_size))    
                cube6_y = random.randrange(0, 945, (cube_size))
                cube7_x = random.randrange(1920, 3840, (cube_size))    
                cube7_y = random.randrange(0, 945, (cube_size))
                cube8_x = random.randrange(1920, 3840, (cube_size))    
                cube8_y = random.randrange(0, 945, (cube_size))

                cube9_x = random.randrange(1920, 3840, (cube_size))    
                cube9_y = random.randrange(0, 945, (cube_size))
                cube10_x = random.randrange(1920, 3840, (cube_size))    
                cube10_y = random.randrange(0, 945, (cube_size))
                cube11_x = random.randrange(1920, 3840, (cube_size))    
                cube11_y = random.randrange(0, 945, (cube_size))
                cube12_x = random.randrange(1920, 3840, (cube_size))    
                cube12_y = random.randrange(0, 945, (cube_size))

                cube13_x = random.randrange(1920, 3840, (cube_size))    
                cube13_y = random.randrange(0, 945, (cube_size))
                cube14_x = random.randrange(1920, 3840, (cube_size))    
                cube14_y = random.randrange(0, 945, (cube_size))
                cube15_x = random.randrange(1920, 3840, (cube_size))    
                cube15_y = random.randrange(0, 945, (cube_size))
                cube16_x = random.randrange(1920, 3840, (cube_size))    
                cube16_y = random.randrange(0, 945, (cube_size))

                cube17_x = random.randrange(1920, 3840, (cube_size))    
                cube17_y = random.randrange(0, 945, (cube_size))
                cube18_x = random.randrange(1920, 3840, (cube_size))    
                cube18_y = random.randrange(0, 945, (cube_size))
                cube19_x = random.randrange(1920, 3840, (cube_size))    
                cube19_y = random.randrange(0, 945, (cube_size))
                cube20_x = random.randrange(1920, 3840, (cube_size))    
                cube20_y = random.randrange(0, 945, (cube_size))

                s_boss1_x = 2000
                s_boss1_y = 0

                s_boss2_x = 2000
                s_boss2_y = 282

                s_boss3_x = 2000
                s_boss3_y = 563

                s_boss4_x = 2000
                s_boss4_y = 845

                s_boss1_1_x = -180
                s_boss2_1_x = -180
                s_boss3_1_x = -180
                s_boss4_1_x = -180

                s_boss1_beam_pos = 0, - 1000
                s_boss2_beam_pos = 0, - 1000
                s_boss3_beam_pos = 0, - 1000
                s_boss4_beam_pos = 0, - 1000

                s_boss1_y_rand = random.randrange(0, 90, (2))
                s_boss2_y_rand = random.randrange(190, 372, (2))
                s_boss3_y_rand = random.randrange(472, 654, (2))
                s_boss4_y_rand = random.randrange(754, 846, (2))

                time_beam = 0
                time_beam_outro = False
                s_boss_end = False

                
        if Round > 0:        
            if pos[0] in range (button_resume[0], button_resume[0] + 300) and pos[1] in range(button_resume[1], button_resume[1] + 70):
                pygame.draw.rect(screen, (BUTTON2), ((1000, 720), (300, 70)))
                if event.type == pygame.MOUSEBUTTONUP:
                    menu = False
                    bg_sp = 11
                    sp_bg = 10
                    sp_x = sp_x_save
                    sp_y_up = sp_y_up_save
                    sp_y_down = sp_y_down_save
            
            
        if ((pos[0] in range (button_newgame[0], button_newgame[0] + 300) and pos[1] in range(button_newgame[1], button_newgame[1] + 70))
            or (pos[0] in range (button_resume[0], button_resume[0] + 300) and pos[1] in range(button_resume[1], button_resume[1] + 70))
            or (pos[0] in range (button_settings[0], button_settings[0] + 60) and pos[1] in range(button_settings[1], button_settings[1] + 60))
            or (pos[0] in range (button_back[0], button_back[0] + 60) and pos[1] in range(button_back[1], button_back[1] + 60))
            or (pos[0] in range (mute_music[0], mute_music[0] + 50) and pos[1] in range(mute_music[1], mute_music[1] + 50))
            or (pos[0] in range (v1_music[0], v1_music[0] + 50) and pos[1] in range(v1_music[1], v1_music[1] + 50))
            or (pos[0] in range (v2_music[0], v2_music[0] + 50) and pos[1] in range(v2_music[1], v2_music[1] + 50))
            or (pos[0] in range (v3_music[0], v3_music[0] + 50) and pos[1] in range(v3_music[1], v3_music[1] + 50))
            or (pos[0] in range (v4_music[0], v4_music[0] + 50) and pos[1] in range(v4_music[1], v4_music[1] + 50))
            or (pos[0] in range (mute_effect[0], mute_effect[0] + 50) and pos[1] in range(mute_effect[1], mute_effect[1] + 50))
            or (pos[0] in range (v1_effect[0], v1_effect[0] + 50) and pos[1] in range(v1_effect[1], v1_effect[1] + 50))
            or (pos[0] in range (v2_effect[0], v2_effect[0] + 50) and pos[1] in range(v2_effect[1], v2_effect[1] + 50))
            or (pos[0] in range (v3_effect[0], v3_effect[0] + 50) and pos[1] in range(v3_effect[1], v3_effect[1] + 50))
            or (pos[0] in range (v4_effect[0], v4_effect[0] + 50) and pos[1] in range(v4_effect[1], v4_effect[1] + 50))
            or (pos[0] in range (button_death[0], button_death[0] + 680) and pos[1] in range(button_death[1], button_death[1] + 70))
            or (pos[0] in range (button_ok[0], button_ok[0] + 55) and pos[1] in range(button_ok[1], button_ok[1] + 55))
            ):      
            pygame.mouse.set_cursor(pygame.SYSTEM_CURSOR_HAND)
        else:
            pygame.mouse.set_cursor(pygame.SYSTEM_CURSOR_ARROW)

            
        # Boders buttons
        pygame.draw.rect(screen, (WHITE), ((620, 720), (300, 5)))     # button new game top  
        pygame.draw.rect(screen, (WHITE), ((620, 720), (5, 70)))       # button new game left
        pygame.draw.rect(screen, (WHITE), ((620, 790), (300, 5)))       # button new game bottom
        pygame.draw.rect(screen, (WHITE), ((920, 720), (5, 75)))       # button new game right
        
        pygame.draw.rect(screen, (WHITE), ((1000, 720), (300, 5)))     # button resume top  
        pygame.draw.rect(screen, (WHITE), ((1000, 720), (5, 70)))       # button resume left
        pygame.draw.rect(screen, (WHITE), ((1000, 790), (300, 5)))       # button resume bottom
        pygame.draw.rect(screen, (WHITE), ((1300, 720), (5, 75)))       # button resume right
        
        # buttons text
        txt_newgame = font_score.render('NEW GAME', False, (WHITE))
        screen.blit(txt_newgame, (660, 740))
        
        screen.blit(txt_resume, (1065, 740))
        
        
        if settings_ == True:
            pygame.draw.rect(screen, (BLUE), ((500, 50), (920, 850))) # Background
            
            
            pygame.draw.rect(screen, (WHITE), ((500, 50), (920, 5)))   # Border top
            pygame.draw.rect(screen, (WHITE), ((500, 50), (5, 850)))    # Border left
            pygame.draw.rect(screen, (WHITE), ((500, 900), (925, 5)))    # Border bottom
            pygame.draw.rect(screen, (WHITE), ((1420, 50), (5, 850)))   # Border right
            
            
            # title
            pygame.draw.rect(screen, (CYAN), ((505, 55), (915, 95)))   # title color
            pygame.draw.rect(screen, (WHITE), ((500, 150), (920, 5)))   # Border title
            
            txt_settings = font_progress.render('SETTINGS', False, (WHITE))
            screen.blit(txt_settings, (770 , 66))
            
            # back button
            pygame.draw.rect(screen, (BUTTON3), ((1332, 70), (60, 60)))
            
            if time_button > 10:
                if (pos[0] in range (button_back[0], button_back[0] + 60) and pos[1] in range(button_back[1], button_back[1] + 60)):
                    pygame.draw.rect(screen, (BUTTON4), ((1332, 70), (60, 60)))
                    if event.type == pygame.MOUSEBUTTONUP:
                        settings_ = False
                        pygame.event.post(pygame.event.Event(pygame.K_l))

            
            pygame.draw.line(screen, (BLACK), (1345, 80), (1383, 120) ,7)
            pygame.draw.line(screen, (BLACK), (1345, 120), (1383, 80) ,7)
            
            pygame.draw.rect(screen, (WHITE), ((1332, 70), (60, 5)))
            pygame.draw.rect(screen, (WHITE), ((1332, 70), (5, 60)))
            pygame.draw.rect(screen, (WHITE), ((1332, 125), (60, 5)))
            pygame.draw.rect(screen, (WHITE), ((1392, 70), (5, 60)))   
            
            time_button += 1
            
            
            pygame.draw.rect(screen, (COLOR_KEYS_BG), ((550, 200), (820, 390)))   # title color       
            pygame.draw.rect(screen, (COLOR_KEYS_TITLE), ((550, 200), (820, 50)))   # title color    
            
            pygame.draw.rect(screen, (WHITE), ((550, 250), (820, 5)))   # Border highscore top
     
                    
            pygame.draw.rect(screen, (WHITE), ((550, 200), (820, 5)))   # Border top
            pygame.draw.rect(screen, (WHITE), ((550, 200), (5, 390)))   # Border left
            pygame.draw.rect(screen, (WHITE), ((1365, 200), (5, 390)))   # Border right
            pygame.draw.rect(screen, (WHITE), ((550, 590), (820, 5)))   # Border bottom
            
            # keybinds
            txt_keys = font_score.render('KEYBINDS', False, (WHITE))
            screen.blit(txt_keys, (598 , 210))
            
            
            txt_key_esc = font_score.render('Pause:', False, (COLOR_KEYS))
            screen.blit(txt_key_esc, (600 , 280))
            txt_key_esc2 = font_score.render('ESC', False, (COLOR_KEYS))
            screen.blit(txt_key_esc2, (900 , 280))

            txt_key_up = font_score.render('UP:', False, (COLOR_KEYS))
            screen.blit(txt_key_up, (600 , 345))
            txt_key_up2 = font_score.render('W', False, (COLOR_KEYS))
            screen.blit(txt_key_up2, (900 , 345))  
            
            txt_key_down = font_score.render('DOWN:', False, (COLOR_KEYS))
            screen.blit(txt_key_down, (600 , 385))
            txt_key_down2 = font_score.render('S', False, (COLOR_KEYS))
            screen.blit(txt_key_down2, (900 , 385))

            txt_key_fw = font_score.render('FORWARD:', False, (COLOR_KEYS))
            screen.blit(txt_key_fw, (600 , 425))
            txt_key_fw2 = font_score.render('D', False, (COLOR_KEYS))
            screen.blit(txt_key_fw2, (900 , 425))
            
            txt_key_bw = font_score.render('BACKWARD:', False, (COLOR_KEYS))
            screen.blit(txt_key_bw, (600 , 465))
            txt_key_bw2 = font_score.render('A', False, (COLOR_KEYS))
            screen.blit(txt_key_bw2, (900 , 465))
            
            txt_key_sp = font_score.render('FIRE:', False, (COLOR_KEYS))
            screen.blit(txt_key_sp, (600 , 530))
            txt_key_sp2 = font_score.render('SPACE', False, (COLOR_KEYS))
            screen.blit(txt_key_sp2, (900 , 530))
            
            # music volume          
            
            pygame.draw.rect(screen, (COLOR_KEYS_BG), ((550, 660), (820, 70)))
            pygame.draw.rect(screen, (WHITE), ((550, 660), (5, 70)))
            pygame.draw.rect(screen, (WHITE), ((550, 660), (820, 5)))
            pygame.draw.rect(screen, (WHITE), ((550, 730), (820, 5)))
            pygame.draw.rect(screen, (WHITE), ((1370, 660), (5, 75)))
            
            txt_music = font_score.render('Music Volume:', False, (COLOR_KEYS))
            screen.blit(txt_music, (580, 680))
            
            pygame.draw.rect(screen, (MUSIC_BUTTONS), ((975, 672), (50, 50))) # mute button
            if music_set == 0:
                pygame.draw.rect(screen, (MUSIC_BUTTONS_ACTIVE), ((975, 672), (50, 50)))
            if (pos[0] in range (mute_music[0], mute_music[0] + 50) and pos[1] in range(mute_music[1], mute_music[1] + 50)):
                pygame.draw.rect(screen, (MUSIC_BUTTONS_HOVER), ((975, 672), (50, 50)))
                if event.type == pygame.MOUSEBUTTONUP:
                    music_set = 0
                    

            mute_music = screen.blit(mute,(988, 679))
            pygame.draw.rect(screen, (WHITE), ((975, 672), (5, 50)))
            pygame.draw.rect(screen, (WHITE), ((975, 672), (50, 5)))
            pygame.draw.rect(screen, (WHITE), ((1025, 672), (5, 50)))
            pygame.draw.rect(screen, (WHITE), ((975, 717), (50, 5)))
            
            pygame.draw.rect(screen, (MUSIC_BUTTONS), ((1065, 672), (50, 50))) # music volume 1
            if music_set == 1:
                pygame.draw.rect(screen, (MUSIC_BUTTONS_ACTIVE), ((1065, 672), (50, 50)))
            if (pos[0] in range (v1_music[0], v1_music[0] + 50) and pos[1] in range(v1_music[1], v1_music[1] + 50)):
                pygame.draw.rect(screen, (MUSIC_BUTTONS_HOVER), ((1065, 672), (50, 50)))
                if event.type == pygame.MOUSEBUTTONUP:
                    music_set = 1

            v1_music = screen.blit(volume1,(1070, 679))
            pygame.draw.rect(screen, (WHITE), ((1065, 672), (5, 50)))
            pygame.draw.rect(screen, (WHITE), ((1065, 672), (50, 5)))
            pygame.draw.rect(screen, (WHITE), ((1115, 672), (5, 50)))
            pygame.draw.rect(screen, (WHITE), ((1065, 717), (50, 5)))
            
            pygame.draw.rect(screen, (MUSIC_BUTTONS), ((1135, 672), (50, 50))) # music volume 2
            if music_set == 2:
                pygame.draw.rect(screen, (MUSIC_BUTTONS_ACTIVE), ((1135, 672), (50, 50)))
            if (pos[0] in range (v2_music[0], v2_music[0] + 50) and pos[1] in range(v2_music[1], v2_music[1] + 50)):
                pygame.draw.rect(screen, (MUSIC_BUTTONS_HOVER), ((1135, 672), (50, 50)))
                if event.type == pygame.MOUSEBUTTONUP:
                    music_set = 2

            v2_music = screen.blit(volume2,(1147, 679))
            pygame.draw.rect(screen, (WHITE), ((1135, 672), (5, 50)))
            pygame.draw.rect(screen, (WHITE), ((1135, 672), (50, 5)))
            pygame.draw.rect(screen, (WHITE), ((1185, 672), (5, 50)))
            pygame.draw.rect(screen, (WHITE), ((1135, 717), (50, 5)))
            
            pygame.draw.rect(screen, (MUSIC_BUTTONS), ((1205, 672), (50, 50))) # music volume 3
            if music_set == 3:
                pygame.draw.rect(screen, (MUSIC_BUTTONS_ACTIVE), ((1205, 672), (50, 50)))
            if (pos[0] in range (v3_music[0], v3_music[0] + 50) and pos[1] in range(v3_music[1], v3_music[1] + 50)):
                pygame.draw.rect(screen, (MUSIC_BUTTONS_HOVER), ((1205, 672), (50, 50)))
                if event.type == pygame.MOUSEBUTTONUP:
                    music_set = 3

            v3_music = screen.blit(volume3,(1217, 679))
            pygame.draw.rect(screen, (WHITE), ((1205, 672), (5, 50)))
            pygame.draw.rect(screen, (WHITE), ((1205, 672), (50, 5)))
            pygame.draw.rect(screen, (WHITE), ((1255, 672), (5, 50)))
            pygame.draw.rect(screen, (WHITE), ((1205, 717), (50, 5)))
            
            pygame.draw.rect(screen, (MUSIC_BUTTONS), ((1275, 672), (50, 50))) # music volume 4
            if music_set == 4:
                pygame.draw.rect(screen, (MUSIC_BUTTONS_ACTIVE), ((1275, 672), (50, 50)))
            if (pos[0] in range (v4_music[0], v4_music[0] + 50) and pos[1] in range(v4_music[1], v4_music[1] + 50)):
                pygame.draw.rect(screen, (MUSIC_BUTTONS_HOVER), ((1275, 672), (50, 50)))
                if event.type == pygame.MOUSEBUTTONUP:
                    music_set = 4

            v4_music = screen.blit(volume4,(1284, 679))
            pygame.draw.rect(screen, (WHITE), ((1275, 672), (5, 50)))
            pygame.draw.rect(screen, (WHITE), ((1275, 672), (50, 5)))
            pygame.draw.rect(screen, (WHITE), ((1325, 672), (5, 50)))
            pygame.draw.rect(screen, (WHITE), ((1275, 717), (50, 5)))
            
            
            # effect volume
            
            pygame.draw.rect(screen, (COLOR_KEYS_BG), ((550, 770), (820, 70)))
            pygame.draw.rect(screen, (WHITE), ((550, 770), (5, 70)))
            pygame.draw.rect(screen, (WHITE), ((550, 770), (820, 5)))
            pygame.draw.rect(screen, (WHITE), ((550, 840), (820, 5)))
            pygame.draw.rect(screen, (WHITE), ((1370, 770), (5, 75)))            
            
            txt_effect = font_score.render('Effect Volume:', False, (COLOR_KEYS))
            screen.blit(txt_effect, (580, 790))
                    
            pygame.draw.rect(screen, (MUSIC_BUTTONS), ((975, 782), (50, 50))) # mute button
            if effect_set == 0:
                pygame.draw.rect(screen, (MUSIC_BUTTONS_ACTIVE), ((975, 782), (50, 50)))
            if (pos[0] in range (mute_effect[0], mute_effect[0] + 50) and pos[1] in range(mute_effect[1], mute_effect[1] + 50)):
                pygame.draw.rect(screen, (MUSIC_BUTTONS_HOVER), ((975, 782), (50, 50)))
                if event.type == pygame.MOUSEBUTTONUP:
                    effect_set = 0

            mute_effect = screen.blit(mute,(988, 789))
            pygame.draw.rect(screen, (WHITE), ((975, 782), (5, 50)))
            pygame.draw.rect(screen, (WHITE), ((975, 782), (50, 5)))
            pygame.draw.rect(screen, (WHITE), ((1025, 782), (5, 50)))
            pygame.draw.rect(screen, (WHITE), ((975, 827), (50, 5)))
            
            pygame.draw.rect(screen, (MUSIC_BUTTONS), ((1065, 782), (50, 50))) # effect volume 1
            if effect_set == 1:
                pygame.draw.rect(screen, (MUSIC_BUTTONS_ACTIVE), ((1065, 782), (50, 50)))
            if (pos[0] in range (v1_effect[0], v1_effect[0] + 50) and pos[1] in range(v1_effect[1], v1_effect[1] + 50)):
                pygame.draw.rect(screen, (MUSIC_BUTTONS_HOVER), ((1065, 782), (50, 50)))
                if event.type == pygame.MOUSEBUTTONUP:
                    effect_set = 1
                    pygame.mixer.Sound.play(laser)
                    pygame.event.post(pygame.event.Event(pygame.K_l))
                    
            v1_effect = screen.blit(volume1,(1070, 789))
            pygame.draw.rect(screen, (WHITE), ((1065, 782), (5, 50)))
            pygame.draw.rect(screen, (WHITE), ((1065, 782), (50, 5)))
            pygame.draw.rect(screen, (WHITE), ((1115, 782), (5, 50)))
            pygame.draw.rect(screen, (WHITE), ((1065, 827), (50, 5)))
            
            pygame.draw.rect(screen, (MUSIC_BUTTONS), ((1135, 782), (50, 50))) # effect volume 2
            if effect_set == 2:
                pygame.draw.rect(screen, (MUSIC_BUTTONS_ACTIVE), ((1135, 782), (50, 50)))
            if (pos[0] in range (v2_effect[0], v2_effect[0] + 50) and pos[1] in range(v2_effect[1], v2_effect[1] + 50)):
                pygame.draw.rect(screen, (MUSIC_BUTTONS_HOVER), ((1135, 782), (50, 50)))
                if event.type == pygame.MOUSEBUTTONUP:
                    effect_set = 2
                    pygame.mixer.Sound.play(laser)
                    pygame.event.post(pygame.event.Event(pygame.K_l))
                    
            v2_effect = screen.blit(volume2,(1147, 789))
            pygame.draw.rect(screen, (WHITE), ((1135, 782), (5, 50)))
            pygame.draw.rect(screen, (WHITE), ((1135, 782), (50, 5)))
            pygame.draw.rect(screen, (WHITE), ((1185, 782), (5, 50)))
            pygame.draw.rect(screen, (WHITE), ((1135, 827), (50, 5)))
            
            pygame.draw.rect(screen, (MUSIC_BUTTONS), ((1205, 782), (50, 50))) # effect volume 3
            if effect_set == 3:
                pygame.draw.rect(screen, (MUSIC_BUTTONS_ACTIVE), ((1205, 782), (50, 50))) 
            if (pos[0] in range (v3_effect[0], v3_effect[0] + 50) and pos[1] in range(v3_effect[1], v3_effect[1] + 50)):
                pygame.draw.rect(screen, (MUSIC_BUTTONS_HOVER), ((1205, 782), (50, 50))) 
                if event.type == pygame.MOUSEBUTTONUP:
                    effect_set = 3
                    pygame.mixer.Sound.play(laser)
                    pygame.event.post(pygame.event.Event(pygame.K_l))

            v3_effect = screen.blit(volume3,(1217, 789))
            pygame.draw.rect(screen, (WHITE), ((1205, 782), (5, 50)))
            pygame.draw.rect(screen, (WHITE), ((1205, 782), (50, 5)))
            pygame.draw.rect(screen, (WHITE), ((1255, 782), (5, 50)))
            pygame.draw.rect(screen, (WHITE), ((1205, 827), (50, 5)))
            
            pygame.draw.rect(screen, (MUSIC_BUTTONS), ((1275, 782), (50, 50))) # effect volume 4
            if effect_set == 4:
                pygame.draw.rect(screen, (MUSIC_BUTTONS_ACTIVE), ((1275, 782), (50, 50)))
            if (pos[0] in range (v4_effect[0], v4_effect[0] + 50) and pos[1] in range(v4_effect[1], v4_effect[1] + 50)):
                pygame.draw.rect(screen, (MUSIC_BUTTONS_HOVER), ((1275, 782), (50, 50)))
                if event.type == pygame.MOUSEBUTTONUP:
                    effect_set = 4
                    pygame.mixer.Sound.play(laser)
                    pygame.event.post(pygame.event.Event(pygame.K_l))

            v4_effect = screen.blit(volume4,(1284, 789))
            pygame.draw.rect(screen, (WHITE), ((1275, 782), (5, 50)))
            pygame.draw.rect(screen, (WHITE), ((1275, 782), (50, 5)))
            pygame.draw.rect(screen, (WHITE), ((1325, 782), (5, 50)))
            pygame.draw.rect(screen, (WHITE), ((1275, 827), (50, 5)))
            
        # death screen   
        if death == True:
            pygame.draw.rect(screen, (BLUE), ((500, 50), (920, 850))) # Background

            pygame.draw.rect(screen, (WHITE), ((500, 50), (920, 5)))   # Border top
            pygame.draw.rect(screen, (WHITE), ((500, 50), (5, 850)))    # Border left
            pygame.draw.rect(screen, (WHITE), ((500, 900), (925, 5)))    # Border bottom
            pygame.draw.rect(screen, (WHITE), ((1420, 50), (5, 850)))   # Border right
                
                
            # title
            pygame.draw.rect(screen, (CYAN), ((505, 55), (915, 95)))   # title color
            pygame.draw.rect(screen, (WHITE), ((500, 150), (920, 5)))   # Border title
                
            txt_gamename = font_progress.render('SPACE FORCE', False, (WHITE))
            screen.blit(txt_gamename, ( 675 , 66))
                      

            button_death = pygame.draw.rect(screen, (BUTTON), ((620, 790), (680, 70)))
            if (hs_1 or hs_2 or hs_3 or hs_4 or hs_5) == True:
                button_death = (-1000, -1000)
            if (pos[0] in range (button_death[0], button_death[0] + 620) and pos[1] in range(button_death[1], button_death[1] + 70)):
                pygame.draw.rect(screen, (BUTTON2), ((620, 790), (680, 70)))
                if event.type == pygame.MOUSEBUTTONUP:
                    hp = 3
                    death = False
            
            txt_death_btn = font_score.render('BACK TO MAIN MENU', False, (WHITE))
            screen.blit(txt_death_btn, (755, 810))
            
            pygame.draw.rect(screen, (WHITE), ((620, 790), (680, 5)))
            pygame.draw.rect(screen, (WHITE), ((620, 790), (5, 70)))
            pygame.draw.rect(screen, (WHITE), ((1300, 790), (5, 75)))
            pygame.draw.rect(screen, (WHITE), ((620, 860), (680, 5)))
            
            screen.blit(death_bg, (540, 190))
            pygame.draw.rect(screen, (WHITE), ((540, 190), (840, 5))) 
            pygame.draw.rect(screen, (WHITE), ((540, 190), (5, 540))) 
            pygame.draw.rect(screen, (WHITE), ((540, 730), (845, 5))) 
            pygame.draw.rect(screen, (WHITE), ((1380, 190), (5, 540))) 
            
            pygame.draw.rect(screen, (CYAN), ((735, 350), (450, 200))) 
            pygame.draw.rect(screen, (WHITE), ((735, 350), (450, 5))) 
            pygame.draw.rect(screen, (WHITE), ((735, 350), (5, 200))) 
            pygame.draw.rect(screen, (WHITE), ((1185, 350), (5, 200)))
            pygame.draw.rect(screen, (WHITE), ((735, 550), (455, 5)))
            
            txt_death_score1 = font_score.render('You Scored', False, (WHITE))
            screen.blit(txt_death_score1, (831, 375))
            
            txt_score2 = font_gamename.render(str(score), False, (SCORE_CLR))
            txt_score2_width = txt_score2.get_width()
            screen.blit(txt_score2, (((size_x - txt_score2_width)/2) , 433))
            
            txt_death_score2 = font_score.render('POINTS', False, (WHITE))
            screen.blit(txt_death_score2, (890, 500)) 

            
            txt_death = font_score.render('YOUR SPACECRAFT GOT DESTROYED!', False, (LIGHT_YELLOW))
            screen.blit(txt_death, (590, 235))
            
            txt_death_ = font_score.render('BETTER LUCK NEXT TIME', False, (LIGHT_YELLOW))
            screen.blit(txt_death_, (708, 660))
            
            
            # if highscore
            if (hs_1 or hs_2 or hs_3 or hs_4 or hs_5) == True:
                pygame.draw.rect(screen, (BLUE), ((600, 760), (730, 140)))
                screen.blit(hs_bg, (540, 190))
                pygame.draw.rect(screen, (WHITE), ((540, 190), (840, 5))) 
                pygame.draw.rect(screen, (WHITE), ((540, 190), (5, 540))) 
                pygame.draw.rect(screen, (WHITE), ((540, 730), (845, 5))) 
                pygame.draw.rect(screen, (WHITE), ((1380, 190), (5, 540))) 
                
                txt_hs1 = font_score.render('CONGRATULATION YOU HAVE REACHED', False, (LIGHT_YELLOW))
                screen.blit(txt_hs1, (575, 235))
                txt_hs2 = font_score.render('THE TOP 5 HIGHSCORE!', False, (LIGHT_YELLOW))
                screen.blit(txt_hs2, (735, 290))
                
                pygame.draw.rect(screen, (CYAN), ((735, 380), (450, 200))) 
                pygame.draw.rect(screen, (WHITE), ((735, 380), (450, 5))) 
                pygame.draw.rect(screen, (WHITE), ((735, 380), (5, 200))) 
                pygame.draw.rect(screen, (WHITE), ((1185, 380), (5, 200)))
                pygame.draw.rect(screen, (WHITE), ((735, 580), (455, 5)))
                
                txt_death_score1 = font_score.render('You Scored', False, (WHITE))
                screen.blit(txt_death_score1, (831, 405))
                
                txt_score2 = font_gamename.render(str(score), False, (SCORE_CLR))
                txt_score2_width = txt_score2.get_width()
                screen.blit(txt_score2, (((size_x - txt_score2_width)/2) , 463))
                
                txt_death_score2 = font_score.render('POINTS', False, (WHITE))
                screen.blit(txt_death_score2, (890, 530)) 
                
                
                txt_hs3 = font_score.render('YOU PLACED', False, (LIGHT_YELLOW))
                screen.blit(txt_hs3, (780, 660))
                
                if hs_1 == True:
                    txt_hs4 = font_score.render('# 1ST', False, (SCORE_CLR))
                elif hs_2 == True:
                    txt_hs4 = font_score.render('# 2ND', False, (SCORE_CLR))
                elif hs_3 == True:
                    txt_hs4 = font_score.render('# 3RD', False, (SCORE_CLR))
                elif hs_4 == True:
                    txt_hs4 = font_score.render('# 4TH', False, (SCORE_CLR))
                elif hs_5 == True:
                    txt_hs4 = font_score.render('# 5TH', False, (SCORE_CLR))
                screen.blit(txt_hs4, (1050, 660))
                
                # pls enter name
                pygame.draw.rect(screen, (D_GRAY3), ((540, 780), (840, 80)))
                
                pygame.draw.rect(screen, (WHITE), ((540, 780), (840, 5)))
                pygame.draw.rect(screen, (WHITE), ((540, 780), (5, 80)))
                pygame.draw.rect(screen, (WHITE), ((540, 860), (840, 5)))
                pygame.draw.rect(screen, (WHITE), ((1380, 780), (5, 85)))  

                txt_name = font_score.render('ENTER USERNAME:', False, (WHITE))
                screen.blit(txt_name, (570, 805))
                
                pygame.draw.rect(screen, (GRAY), ((975, 795), (320, 55)))
                pygame.draw.rect(screen, (WHITE), ((975, 795), (5, 55)))
                pygame.draw.rect(screen, (WHITE), ((975, 795), (320, 5)))
                pygame.draw.rect(screen, (WHITE), ((1290, 795), (5, 55)))
                pygame.draw.rect(screen, (WHITE), ((975, 845), (320, 5)))
                
                txt_name2 = font_score.render(str(player_name), False, (WHITE))
                screen.blit(txt_name2, (995, 805))
            
                player_name_len = txt_name2.get_width()    
                if event.type == pygame.KEYUP:
                    next_key = True
                    next_key_back = 0
                    pygame.event.post(pygame.event.Event(pygame.KEYDOWN))
                    
                

                if player_name_len < 220:
                    if pressed[pygame.K_q] and next_key == True:
                        player_name = player_name + 'q'
                        next_key = False
                    elif pressed[pygame.K_w] and next_key == True:
                        player_name = player_name + 'w'
                        next_key = False
                    elif pressed[pygame.K_e] and next_key == True:
                        player_name = player_name + 'e'
                        next_key = False
                    elif pressed[pygame.K_r] and next_key == True:
                        player_name = player_name + 'r'
                        next_key = False
                    elif pressed[pygame.K_t] and next_key == True:
                        player_name = player_name + 't'
                        next_key = False
                    elif pressed[pygame.K_z] and next_key == True:
                        player_name = player_name + 'z'
                        next_key = False
                    elif pressed[pygame.K_u] and next_key == True:
                        player_name = player_name + 'u'
                        next_key = False
                    elif pressed[pygame.K_i] and next_key == True:
                        player_name = player_name + 'i'
                        next_key = False
                    elif pressed[pygame.K_o] and next_key == True:
                        player_name = player_name + 'o'
                        next_key = False
                    elif pressed[pygame.K_p] and next_key == True:
                        player_name = player_name + 'p'
                        next_key = False
                    elif pressed[pygame.K_a] and next_key == True:
                        player_name = player_name + 'a'
                        next_key = False
                    elif pressed[pygame.K_s] and next_key == True:
                        player_name = player_name + 's'
                        next_key = False
                    elif pressed[pygame.K_d] and next_key == True:
                        player_name = player_name + 'd'
                        next_key = False
                    elif pressed[pygame.K_f] and next_key == True:
                        player_name = player_name + 'f'
                        next_key = False
                    elif pressed[pygame.K_g] and next_key == True:
                        player_name = player_name + 'g'
                        next_key = False
                    elif pressed[pygame.K_h] and next_key == True:
                        player_name = player_name + 'h'
                        next_key = False
                    elif pressed[pygame.K_j] and next_key == True:
                        player_name = player_name + 'j'
                        next_key = False
                    elif pressed[pygame.K_k] and next_key == True:
                        player_name = player_name + 'k'
                        next_key = False
                    elif pressed[pygame.K_l] and next_key == True:
                        player_name = player_name + 'l'
                        next_key = False
                    elif pressed[pygame.K_y] and next_key == True:
                        player_name = player_name + 'y'
                        next_key = False
                    elif pressed[pygame.K_x] and next_key == True:
                        player_name = player_name + 'x'
                        next_key = False
                    elif pressed[pygame.K_c] and next_key == True:
                        player_name = player_name + 'c'
                        next_key = False
                    elif pressed[pygame.K_v] and next_key == True:
                        player_name = player_name + 'v'
                        next_key = False
                    elif pressed[pygame.K_b] and next_key == True:
                        player_name = player_name + 'b'
                        next_key = False
                    elif pressed[pygame.K_n] and next_key == True:
                        player_name = player_name + 'n'
                        next_key = False
                    elif pressed[pygame.K_m] and next_key == True:
                        player_name = player_name + 'm'
                        next_key = False
                    elif pressed[pygame.K_1] and next_key == True:
                        player_name = player_name + '1'
                        next_key = False
                    elif pressed[pygame.K_2] and next_key == True:
                        player_name = player_name + '2'
                        next_key = False
                    elif pressed[pygame.K_3] and next_key == True:
                        player_name = player_name + '3'
                        next_key = False
                    elif pressed[pygame.K_4] and next_key == True:
                        player_name = player_name + '4'
                        next_key = False
                    elif pressed[pygame.K_5] and next_key == True:
                        player_name = player_name + '5'
                        next_key = False
                    elif pressed[pygame.K_6] and next_key == True:
                        player_name = player_name + '6'
                        next_key = False
                    elif pressed[pygame.K_7] and next_key == True:
                        player_name = player_name + '7'
                        next_key = False
                    elif pressed[pygame.K_8] and next_key == True:
                        player_name = player_name + '8'
                        next_key = False
                    elif pressed[pygame.K_9] and next_key == True:
                        player_name = player_name + '9'
                        next_key = False
                    elif pressed[pygame.K_0] and next_key == True:
                        player_name = player_name + '0'
                        next_key = False
                
                if pressed[pygame.K_BACKSPACE]:
                    next_key_back += 1
                
                if pressed[pygame.K_BACKSPACE] and (next_key == True or next_key_back > 10):
                    player_name = player_name[:-1]
                    next_key = False
                    
                
                pygame.draw.rect(screen, (D_GRAY), ((1313, 795), (55, 55)))
                if player_name_len > 40:    
                    button_ok = pygame.draw.rect(screen, (LIGHT_YELLOW), ((1313, 795), (55, 55)))
                    if pressed[pygame.K_RETURN]:
                        death = False
                        hp = 3
                        if hs_1 == True:
                            hs_n_1 = player_name
                        elif hs_2 == True:
                            hs_n_2 = player_name
                        elif hs_3 == True:
                            hs_n_3 = player_name
                        elif hs_4 == True:
                            hs_n_4 = player_name
                        elif hs_5 == True:
                            hs_n_5 = player_name
                    if (pos[0] in range (button_ok[0], button_ok[0] + 55) and pos[1] in range(button_ok[1], button_ok[1] + 55)):
                        pygame.draw.rect(screen, (LIGHT_YELLOW2), ((1313, 795), (55, 55)))
                        if event.type == pygame.MOUSEBUTTONUP:
                            death = False
                            hp = 3
                            if hs_1 == True:
                                hs_n_1 = player_name
                            elif hs_2 == True:
                                hs_n_2 = player_name
                            elif hs_3 == True:
                                hs_n_3 = player_name
                            elif hs_4 == True:
                                hs_n_4 = player_name
                            elif hs_5 == True:
                                hs_n_5 = player_name
                                
                txt_name3 = font_score.render('|', False, (WHITE))
                time_name += 1
                if time_name < 15:
                    screen.blit(txt_name3, (997 + player_name_len, 803))
                elif time_name > 30:
                    time_name = 0
                            
                screen.blit(img_check, (1318, 800))
                if player_name_len > 40:  
                    screen.blit(img_check1, (1318, 800))
                pygame.draw.rect(screen, (WHITE), ((1313, 795), (55, 5)))
                pygame.draw.rect(screen, (WHITE), ((1313, 795), (5, 55)))
                pygame.draw.rect(screen, (WHITE), ((1363, 795), (5, 55)))
                pygame.draw.rect(screen, (WHITE), ((1313, 845), (55, 5)))


    ##################################
    #       Header Background        #
    ################################## 
    
    # new
    pygame.draw.rect(screen, (BLUE), ((0, 950), (1920, 200)))
    pygame.draw.rect(screen, (CYAN), ((580, 950), (755, 200)))
        
    pygame.draw.rect(screen, (BLACK), ((0, 945), (size_x, 5))) # border Bottom
    pygame.draw.rect(screen, (BLACK), ((0, 1075), (size_x, 5))) # border top
    pygame.draw.rect(screen, (BLACK), ((0, 945), (5, 135)))    # border left
    pygame.draw.rect(screen, (BLACK), (((size_x - 5), 945), (5, 135)))    # border right
    pygame.draw.rect(screen, (BLACK), ((580, 945), (5, 135)))    # border middle left
    pygame.draw.rect(screen, (BLACK), ((1335, 945), (5, 135))) # border middle right
    
    
    ##################################
    #             Score              #
    ################################## 
    txt_score = font_score.render('SCORE:  ' + str(score), False, (SCORE_CLR))
    txt_score_width = txt_score.get_width()
    screen.blit(txt_score, (((size_x - txt_score_width)/2) , 960))

    if not Round == 0 and menu == False and not Round == 6:
        score = score + 2       # sets score every 1/30 of a second
        
        if (cube1_hp == 0
            or cube2_hp == 0
            or cube3_hp == 0
            or cube4_hp == 0):
            score += sc_cubes1
                    
        if (cube5_hp == 0
            or cube6_hp == 0
            or cube7_hp == 0
            or cube8_hp == 0):
            score += sc_cubes2
        
        if (cube9_hp == 0
            or cube10_hp == 0
            or cube11_hp == 0
            or cube12_hp == 0):
            score += sc_cubes3
        
        if (cube13_hp == 0
            or cube14_hp == 0
            or cube15_hp == 0
            or cube16_hp == 0):
            score += sc_cubes4
            
        if (cube17_hp == 0
            or cube18_hp == 0
            or cube19_hp == 0
            or cube20_hp == 0):
            score += sc_cubes5
            
        if door2_hp == 0 and sc_door2_reset == False:
            sc_door2_reset = True
            if door2_str == 1:
                score += sc_cubes1
            elif door2_str == 2:
                score += sc_cubes2
            
    
    
    ##################################
    #               HP               #
    ##################################  
    pygame.draw.rect(screen, (GRAY), ((675, 1010), (570, 55)))
    pygame.draw.rect(screen, (D_GRAY), ((680, 1015), (560, 45)))
    if hp == 3:
        pygame.draw.rect(screen, (GREEN), ((680, 1015), (560, 45)))
    elif hp == 2:
        pygame.draw.rect(screen, (GREEN), ((680, 1015), (373, 45)))
    elif hp == 1:
        pygame.draw.rect(screen, (GREEN), ((680, 1015), (187, 45)))
        
    pygame.draw.rect(screen,(GRAY), ((867, 1010), (5, 55)))    
    pygame.draw.rect(screen,(GRAY), ((1053, 1010), (5, 55)))
    
    txt_hp = font_score.render('HP', False, (WHITE))
    screen.blit(txt_hp, (939 , 1019))
    
    if  (pl_x < 0 or pl_x > 1935 - pl_length) and menu == False:
        hp = 0
    
    if hp <= 0:
        time_hp += 1
        Round = 0
        sp_x = 0
        sp_y_down = 0
        sp_y_up = 0
        if time_hp > 30:
            menu = True
            sp_bg = 0
            esc_lock = False
            death = True
            if not (pl_x in range(400, 1420) and pl_y in range(0,1080)):
                screen.blit(explosion3, (pl_x, pl_y-40))
        elif time_hp > 25:
            screen.blit(explosion3, (pl_x, pl_y-40))
        elif time_hp > 20:
            screen.blit(explosion2, (pl_x, pl_y-40))  
        elif time_hp > 15:
            screen.blit(explosion1, (pl_x, pl_y-40))
        elif time_hp > 10:
            screen.blit(explosion3, (pl_x, pl_y-40))
        elif time_hp > 5:
            screen.blit(explosion2, (pl_x, pl_y-40))
        elif time_hp > 1:
            screen.blit(explosion1, (pl_x, pl_y-40))
            esc_lock = True
            pygame.mixer.Sound.play(explosion_sound)
            bullets = False
        elif time_hp == 1:
            if score > hs_s_1:
                
                hs_s_5 = hs_s_4
                hs_s_4 = hs_s_3
                hs_s_3 = hs_s_2
                hs_s_2 = hs_s_1
                hs_s_1 = score
                
                hs_n_5 = hs_n_4
                hs_n_4 = hs_n_3
                hs_n_3 = hs_n_2
                hs_n_2 = hs_n_1
                
                hs_1 = True
            elif score > hs_s_2:
                
                hs_s_5 = hs_s_4
                hs_s_4 = hs_s_3
                hs_s_3 = hs_s_2
                hs_s_2 = score
               
                hs_n_5 = hs_n_4
                hs_n_4 = hs_n_3
                hs_n_3 = hs_n_2
                
                hs_2 = True
            elif score > hs_s_3:
                
                hs_s_5 = hs_s_4
                hs_s_4 = hs_s_3
                hs_s_3 = score
            
                hs_n_5 = hs_n_4
                hs_n_4 = hs_n_3
                
                hs_3 = True
            elif score > hs_s_4:
                
                hs_s_5 = hs_s_4
                hs_s_4 = score
                
                hs_n_5 = hs_n_4
                
                hs_4 = True
            elif score > hs_s_5:
                hs_s_5 = score
                hs_5 = True
            
    ##################################
    #              Speed             #
    ##################################    
    
    pygame.draw.rect(screen, (GRAY), ((65, 985), (450, 80)))
    pygame.draw.rect(screen, (D_GRAY), ((70, 990), (440, 70)))
    
    pygame.draw.rect(screen, (D_GRAY3), ((127, 990), (5, 70)))
    pygame.draw.rect(screen, (D_GRAY3), ((207, 990), (5, 70)))
    pygame.draw.rect(screen, (D_GRAY3), ((287, 990), (5, 70)))
    pygame.draw.rect(screen, (D_GRAY3), ((367, 990), (5, 70)))
    pygame.draw.rect(screen, (D_GRAY3), ((447, 990), (5, 70)))
    
    pygame.draw.rect(screen, (D_GRAY2), ((127-40, 990), (5, 70)))
    pygame.draw.rect(screen, (D_GRAY2), ((127+40, 990), (5, 70)))
    pygame.draw.rect(screen, (D_GRAY2), ((207+40, 990), (5, 70)))
    pygame.draw.rect(screen, (D_GRAY2), ((287+40, 990), (5, 70)))
    pygame.draw.rect(screen, (D_GRAY2), ((367+40, 990), (5, 70)))
    pygame.draw.rect(screen, (D_GRAY2), ((447+40, 990), (5, 70)))
    
    txt_20 = font_score.render('20', False, (RED))
    screen.blit(txt_20, ((105) , 1000))
    
    txt_40 = font_score.render('40', False, (RED))
    screen.blit(txt_40, ((185) , 1000))
    
    txt_60 = font_score.render('60', False, (RED))
    screen.blit(txt_60, ((265) , 1000))
    
    txt_80 = font_score.render('80', False, (RED))
    screen.blit(txt_80, ((345) , 1000))
    
    txt_100 = font_score.render('100', False, (RED))
    screen.blit(txt_100, ((425) , 1000))
    
    txt_mph = font_tacho.render('Projectile speed in mph', False, (WHITE))
    screen.blit(txt_mph, ((155) , 1027-70))
    
    pygame.draw.rect(screen, (LIGHT_YELLOW), (((bg_sp*20.5-19), 990), (5, 70)))
    
    
    ##################################
    #            Progress            #
    ##################################    
    
    pygame.draw.rect(screen, (GRAY), ((1405, 985), (450, 80)))
    pygame.draw.rect(screen, (D_GRAY), ((1410, 990), (440, 70)))

    if Round == 1:
        pygame.draw.rect(screen,(LIGHT_YELLOW), (((1410), 990), ((time_round/100*5), 70)))
    if Round == 2:
        pygame.draw.rect(screen,(LIGHT_YELLOW), (((1410), 990), ((73), 70)))
        pygame.draw.rect(screen,(LIGHT_YELLOW), (((1483), 990), ((time_round/100*5.3), 70)))
    if Round == 3:
        pygame.draw.rect(screen,(LIGHT_YELLOW), (((1410), 990), ((73), 70)))
        pygame.draw.rect(screen,(LIGHT_YELLOW), (((1483), 990), ((75), 70)))
        pygame.draw.rect(screen,(LIGHT_YELLOW), (((1560), 990), ((time_round/100*5.3), 70)))
    if Round == 4:
        pygame.draw.rect(screen,(LIGHT_YELLOW), (((1410), 990), ((73), 70)))
        pygame.draw.rect(screen,(LIGHT_YELLOW), (((1483), 990), ((75), 70)))
        pygame.draw.rect(screen,(LIGHT_YELLOW), (((1560), 990), ((75), 70)))
        pygame.draw.rect(screen,(LIGHT_YELLOW), (((1630), 990), ((time_round/100*5), 70)))
    if Round == 5:
        pygame.draw.rect(screen,(LIGHT_YELLOW), (((1410), 990), ((73), 70)))
        pygame.draw.rect(screen,(LIGHT_YELLOW), (((1483), 990), ((75), 70)))
        pygame.draw.rect(screen,(LIGHT_YELLOW), (((1560), 990), ((75), 70)))
        pygame.draw.rect(screen,(LIGHT_YELLOW), (((1630), 990), ((75), 70)))
        pygame.draw.rect(screen,(LIGHT_YELLOW), (((1703), 990), ((time_round/100*5.3), 70)))
    if Round == 6:
        pygame.draw.rect(screen,(LIGHT_YELLOW), (((1410), 990), ((73), 70)))
        pygame.draw.rect(screen,(LIGHT_YELLOW), (((1483), 990), ((75), 70)))
        pygame.draw.rect(screen,(LIGHT_YELLOW), (((1560), 990), ((75), 70)))
        pygame.draw.rect(screen,(LIGHT_YELLOW), (((1630), 990), ((75), 70)))
        pygame.draw.rect(screen,(LIGHT_YELLOW), (((1703), 990), ((75), 70)))
        pygame.draw.rect(screen,(LIGHT_YELLOW), (((1777), 990), (((390 - b_boss_hp)/390*70), 70)))
        
    
    pygame.draw.rect(screen,(GRAY), ((1483, 985), (5, 80)))    # border 1 
    pygame.draw.rect(screen,(GRAY), ((1557, 985), (5, 80)))    # border 2 
    pygame.draw.rect(screen,(GRAY), ((1630, 985), (5, 80)))    # border 3
    pygame.draw.rect(screen,(GRAY), ((1703, 985), (5, 80)))    # border 4
    pygame.draw.rect(screen,(GRAY), ((1777, 985), (5, 80)))    # border 5

    txt_pg1 = font_progress.render('1', False, (D_GRAY2))
    screen.blit(txt_pg1, ((1438) , 988))
    txt_pg2 = font_progress.render('2', False, (D_GRAY2))
    screen.blit(txt_pg2, ((1500) , 988))
    txt_pg3 = font_progress.render('3', False, (D_GRAY3))
    screen.blit(txt_pg3, ((1574) , 988))
    txt_pg4 = font_progress.render('4', False, (D_GRAY2))
    screen.blit(txt_pg4, ((1646) , 988))
    txt_pg5 = font_progress.render('5', False, (D_GRAY2))
    screen.blit(txt_pg5, ((1720) , 988))
    txt_pg6 = font_progress.render('6', False, (D_GRAY4))
    screen.blit(txt_pg6, ((1793) , 988))
    
    txt_pg = font_tacho.render('Spacecraft Position', False, (WHITE))
    screen.blit(txt_pg, ((1518) , 1027-70))

    ##################################
    #               ETC              #
    ##################################   
    
    # Counter
    if shooting == True:    # shooting counter
        time += 1
        if time > 10:
            time = 0
            shooting = False
              
    fpsClock.tick(FPS)      # sets the refreshrate
    pygame.display.flip()   # refeshes the screen
    
pygame.quit()



#################
#    TODOlist   #
# bboss death and outro
# score needs a fix (cubes when killed)
# bboss rewards ( hp and score and speed)