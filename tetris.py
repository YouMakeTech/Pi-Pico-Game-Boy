# tetris.py by Vincent Mistler for YouMakeTech
# Tetris game for the Raspberry Pi Pico Game Boy

from micropython import const
from PicoGameBoy import PicoGameBoy
import time
from random import randint

BLOCK_SIZE = const(12) # Size of a single tetromino block in pixels
GRID_OFFSET = const(2)
GRID_ROWS  = const(20)
GRID_COLS  = const(10)

pgb = PicoGameBoy()

# image definitions 12x12 pixels
tetris_wall=bytearray(b'\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\xf7\x9e\xf7\x9e\xf7\x9emX\x00\x00\x00\x00\xf7\x9e\xf7\x9e\xf7\x9emX\x00\x00\x00\x00\xf7\x9e\xf7\x9e\xf7\x9emX\x00\x00\x00\x00\xf7\x9e\xf7\x9e\xf7\x9emX\x00\x00\x00\x00mXmXmX3\x91\x00\x00\x00\x00mXmXmX3\x91\x00\x00\x00\x00mX3\x913\x913\x91\x00\x00\x00\x00mX3\x913\x913\x91\x00\x00\x00\x00mX3\x913\x913\x91\x00\x00\x00\x00mX3\x913\x913\x91\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00mX\x00\x00\x00\x00\xf7\x9e\xf7\x9e\xf7\x9emX\x00\x00\x00\x00\xf7\x9e\xf7\x9e\xf7\x9emX\x00\x00\x00\x00\xf7\x9e\xf7\x9e\xf7\x9emX\x00\x00\x00\x00\xf7\x9e\xf7\x9e\xf7\x9e3\x91\x00\x00\x00\x00mXmXmX3\x91\x00\x00\x00\x00mXmXmX3\x91\x00\x00\x00\x00mX3\x913\x913\x91\x00\x00\x00\x00mX3\x913\x913\x91\x00\x00\x00\x00mX3\x913\x913\x91\x00\x00\x00\x00mX3\x913\x91')
bottom_border=bytearray(b'\xeeP\xf6\x90\xf6\x90\xf6\x90\xf6\x90\xf6\x90\xf6\x90\xf6\x90\xf6\x90\xf6\x90\xf6\x90\xeeP\xf6p\xfe\xb1\xfe\xb1\xfe\xb1\xfe\xb1\xfe\xb1\xfe\xb1\xfe\xb1\xfe\xb1\xfe\xb1\xfe\xb1\xf6p\xdd\x0f\xe5P\xe5P\xe5P\xe5P\xe5P\xe5P\xe5P\xe5P\xe5P\xe5P\xdd\x0fI\x84I\x84I\x84I\x84I\x84I\x84I\x84I\x84I\x84I\x84I\x84I\x84@\xc3H\xc4H\xc4H\xc4H\xc4H\xc4H\xc4H\xc4H\xc4H\xc4H\xc4@\xc3\xd3\r\xdb.\xdb.\xdb.\xdb.\xdb.\xdb.\xdb.\xdb.\xdb.\xdb.\xd3\r\xe4\xef\xed0\xed0\xed0\xed0\xed0\xed0\xed0\xed0\xed0\xed0\xe4\xef\xe5P\xf5p\xf5p\xf5p\xf5p\xf5p\xf5p\xf5p\xf5p\xf5p\xf5p\xe5P\xf6p\xfe\xb1\xfe\xb1\xfe\xb1\xfe\xb1\xfe\xb1\xfe\xb1\xfe\xb1\xfe\xb1\xfe\xb1\xfe\xb1\xf6p\xe5P\xf5p\xf5p\xf5p\xf5p\xf5p\xf5p\xf5p\xf5p\xf5p\xf5p\xe5P\xdc\xef\xe5\x0f\xe5\x0f\xe5\x0f\xe5\x0f\xe5\x0f\xe5\x0f\xe5\x0f\xe5\x0f\xe5\x0f\xe5\x0f\xdc\xefI\x84I\xa4I\xa4I\xa4I\xa4I\xa4I\xa4I\xa4I\xa4I\xa4I\xa4I\x84')
corner=bytearray(b'\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\x00\x00\x00\x00mX\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\xffmX\x00\x00\x00\x00mXmX\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\xffmXmX\x00\x00\x00\x00mXmXmX\xff\xff\xff\xff\xff\xff\xff\xffmXmXmX\x00\x00\x00\x00mXmXmXmX\xff\xff\xff\xffmXmXmXmX\x00\x00\x00\x00mXmXmXmX3\x913\x91mXmXmXmX\x00\x00\x00\x00mXmXmX3\x913\x913\x913\x91mXmXmX\x00\x00\x00\x00mXmX3\x913\x913\x913\x913\x913\x91mXmX\x00\x00\x00\x00mX3\x913\x913\x913\x913\x913\x913\x913\x91mX\x00\x00\x00\x003\x913\x913\x913\x913\x913\x913\x913\x913\x913\x91\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00')
left_border=bytearray(b'\x00\x00\xe3\x0e\xe3\x0e\xedP\xe3\x0e\xe3\x0e\xe3\x0e\x00\x00\x00\x00\xedP\xedP\xedP\x00\x00\xedP\xedP\xfe\xd1\xedP\xedP\xe3\x0e\x00\x00\x00\x00\xedP\xfe\xd1\xfe\xd1\x00\x00\xedP\xedP\xfe\xd1\xedP\xedP\xe3\x0e\x00\x00\x00\x00\xedP\xfe\xd1\xfe\xd1\x00\x00\xedP\xedP\xfe\xd1\xedP\xedP\xe3\x0e\x00\x00\x00\x00\xedP\xfe\xd1\xfe\xd1\x00\x00\xe3\x0e\xe3\x0e\xedP\xe3\x0e\xe3\x0e\x00\x00\x00\x00\x00\x00\xedP\xfe\xd1\xfe\xd1\x00\x00\xe3\x0e\xe3\x0e\xedP\xe3\x0e\xe3\x0e\x00\x00\x00\x00\x00\x00\xedP\xfe\xd1\xfe\xd1\x00\x00\xfe\xd1\xfe\xd1\xfe\xd1\xfe\xd1\xfe\xd1\xedP\x00\x00\x00\x00\xedP\xfe\xd1\xfe\xd1\x00\x00\xedP\xedP\xfe\xd1\xedP\xedP\xe3\x0e\x00\x00\x00\x00\xedP\xfe\xd1\xfe\xd1\x00\x00\xedP\xedP\xfe\xd1\xedP\xedP\xe3\x0e\x00\x00\x00\x00\xedP\xfe\xd1\xfe\xd1\x00\x00\xe3\x0e\xe3\x0e\xedP\xe3\x0e\xe3\x0e\x00\x00\x00\x00\x00\x00\xedP\xfe\xd1\xfe\xd1\x00\x00\xfe\xd1\xfe\xd1\xfe\xd1\xfe\xd1\xfe\xd1\xedP\x00\x00\x00\x00\xedP\xfe\xd1\xfe\xd1\x00\x00\xfe\xd1\xfe\xd1\xfe\xd1\xfe\xd1\xfe\xd1\xedP\x00\x00\x00\x00\xedP\xfe\xd1\xfe\xd1')
right_border=bytearray(b'\xedP\xedP\xedP\x00\x00\x00\x00\xe3\x0e\xe3\x0e\xe3\x0e\xedP\xe3\x0e\xe3\x0e\x00\x00\xfe\xd1\xfe\xd1\xedP\x00\x00\x00\x00\xe3\x0e\xedP\xedP\xfe\xd1\xedP\xedP\x00\x00\xfe\xd1\xfe\xd1\xedP\x00\x00\x00\x00\xe3\x0e\xedP\xedP\xfe\xd1\xedP\xedP\x00\x00\xfe\xd1\xfe\xd1\xedP\x00\x00\x00\x00\xe3\x0e\xedP\xedP\xfe\xd1\xedP\xedP\x00\x00\xfe\xd1\xfe\xd1\xedP\x00\x00\x00\x00\x00\x00\xe3\x0e\xe3\x0e\xedP\xe3\x0e\xe3\x0e\x00\x00\xfe\xd1\xfe\xd1\xedP\x00\x00\x00\x00\x00\x00\xe3\x0e\xe3\x0e\xedP\xe3\x0e\xe3\x0e\x00\x00\xfe\xd1\xfe\xd1\xedP\x00\x00\x00\x00\xedP\xfe\xd1\xfe\xd1\xfe\xd1\xfe\xd1\xfe\xd1\x00\x00\xfe\xd1\xfe\xd1\xedP\x00\x00\x00\x00\xe3\x0e\xedP\xedP\xfe\xd1\xedP\xedP\x00\x00\xfe\xd1\xfe\xd1\xedP\x00\x00\x00\x00\xe3\x0e\xedP\xedP\xfe\xd1\xedP\xedP\x00\x00\xfe\xd1\xfe\xd1\xedP\x00\x00\x00\x00\x00\x00\xe3\x0e\xe3\x0e\xedP\xe3\x0e\xe3\x0e\x00\x00\xfe\xd1\xfe\xd1\xedP\x00\x00\x00\x00\xedP\xfe\xd1\xfe\xd1\xfe\xd1\xfe\xd1\xfe\xd1\x00\x00\xfe\xd1\xfe\xd1\xedP\x00\x00\x00\x00\xedP\xfe\xd1\xfe\xd1\xfe\xd1\xfe\xd1\xfe\xd1\x00\x00')
top_border=bytearray(b'\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\xedP\xedP\xedP\xedP\xedP\xedP\xedP\xedP\xedP\xedP\xedP\xedP\xedP\xedP\xedP\xedP\xedP\xedP\xedP\xedP\xedP\xedP\xedP\xedP\xfe\xd1\xfe\xd1\xfe\xd1\xfe\xd1\xfe\xd1\xfe\xd1\xfe\xd1\xfe\xd1\xfe\xd1\xfe\xd1\xfe\xd1\xfe\xd1\xedP\xedP\xedP\xedP\xedP\xedP\xedP\xedP\xedP\xedP\xedP\xedP\xedP\xedP\xedP\xedP\xedP\xedP\xedP\xedP\xedP\xedP\xedP\xedP\xe3\x0e\xe3\x0e\xe3\x0e\xe3\x0e\xe3\x0e\xe3\x0e\xe3\x0e\xe3\x0e\xe3\x0e\xe3\x0e\xe3\x0e\xe3\x0e\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\xedP\xedP\xedP\xedP\xedP\xedP\xedP\xedP\xedP\xedP\xedP\xedP\xfe\xd1\xfe\xd1\xfe\xd1\xfe\xd1\xfe\xd1\xfe\xd1\xfe\xd1\xfe\xd1\xfe\xd1\xfe\xd1\xfe\xd1\xfe\xd1\xfe\xd1\xfe\xd1\xfe\xd1\xfe\xd1\xfe\xd1\xfe\xd1\xfe\xd1\xfe\xd1\xfe\xd1\xfe\xd1\xfe\xd1\xfe\xd1')

pgb.add_sprite(tetris_wall,12,12) #0
pgb.add_sprite(bottom_border,12,12) #1
pgb.add_sprite(corner,12,12) #2
pgb.add_sprite(left_border,12,12) #3
pgb.add_sprite(right_border,12,12) #4
pgb.add_sprite(top_border,12,12) #5


field = [[-1 for col in range(GRID_COLS)] for row in range(GRID_ROWS)]

# shape of the 7 tetrominos
# [0][1]
# [2][3]
# [4][5]
# [6][7]
# e.g. [3,4,5,7] is:
#    [ ]
# [ ][ ]
#    [ ]
tetrominos = [[1,3,5,7],
              [2,4,5,7],
              [3,5,4,6],
              [3,5,4,7],
              [2,3,5,7],
              [3,5,7,6],
              [2,3,4,5]]

# Game Boy Color Tetrominos colors
tetrominos_colors =[PicoGameBoy.color(239,146,132),
             PicoGameBoy.color(222,146,239),
             PicoGameBoy.color(239,170,132),
             PicoGameBoy.color(165,211,132),
             PicoGameBoy.color(99,219,222),
             PicoGameBoy.color(231,97,115),
             PicoGameBoy.color(0,0,0)]

# Color scheme
BLACK = PicoGameBoy.color(0,0,0)
WHITE = PicoGameBoy.color(255,255,255)
GRID_BACKGROUND_COLOR = PicoGameBoy.color(255,211,132)
BACKGROUND_COLOR = PicoGameBoy.color(99,154,132)
BACKGROUND_COLOR2 = PicoGameBoy.color(57,89,41)
TEXT_COLOR = BLACK
TEXT_BACKGROUND_COLOR = WHITE

lines = 0
level = 0
score = 0
last_button="NONE"
has_rotated=False
now = time.ticks_ms()
n = randint(0, 6)
next_n = randint(0, 6)
x=[0,0,0,0]
y=[0,0,0,0]
prev_x=[0,0,0,0]
prev_y=[0,0,0,0]
for i in range(0,4):
    x[i]=(tetrominos[n][i]) % 2;
    y[i]=int(tetrominos[n][i] / 2);
    
    x[i]+=int(GRID_COLS/2)


def collision(x,y):
    for i in range(4):
        # check collision against the border
        if x[i]<0 or x[i]>=GRID_COLS or y[i]>=GRID_ROWS:
            return True
        # check collision against another triomino
        if field[y[i]][x[i]]>=0:
            return True
            
    return False

def title_screen():
    # title screen
    now = time.ticks_ms()
    while pgb.any_button()==False:
        pgb.load_image("tetris_title.bin")
        pgb.show()
        
        if time.ticks_diff(time.ticks_ms(), now) > 200:
            now = time.ticks_ms()
            pgb.center_text("PRESS ANY BUTTON",WHITE)
            pgb.show()
            while time.ticks_diff(time.ticks_ms(), now) < 200:
                time.sleep(0.020)
            now = time.ticks_ms()
            
def game_over_screen():
    pgb.fill_rect(60,90,120,60,BLACK)
    pgb.center_text("GAME OVER",WHITE)
    pgb.show()
    while True:
        time.sleep(0.500)


def draw_background():
    pgb.fill(BACKGROUND_COLOR)
    
    for i in range(0,int(240/BLOCK_SIZE),2):
        for j in range(0,int(240/BLOCK_SIZE),2):
            pgb.fill_rect(j*BLOCK_SIZE,i*BLOCK_SIZE,BLOCK_SIZE,BLOCK_SIZE,BACKGROUND_COLOR2)
            pgb.fill_rect((j+1)*BLOCK_SIZE,(i+1)*BLOCK_SIZE,BLOCK_SIZE,BLOCK_SIZE,BACKGROUND_COLOR2)
            
    pgb.fill_rect(GRID_OFFSET*BLOCK_SIZE,0,
                  GRID_COLS*BLOCK_SIZE,GRID_ROWS*BLOCK_SIZE,
                  GRID_BACKGROUND_COLOR)
    
    # add walls
    for i in range(GRID_ROWS):
        pgb.sprite(0,(GRID_OFFSET-1)*BLOCK_SIZE,i*BLOCK_SIZE)
        pgb.sprite(0,(GRID_OFFSET+GRID_COLS)*BLOCK_SIZE,i*BLOCK_SIZE)
    
    # draw text (LINES)
    pgb.fill_rect((GRID_OFFSET+GRID_COLS+1)*BLOCK_SIZE+1,16*BLOCK_SIZE,
                  BLOCK_SIZE*7,BLOCK_SIZE*2,
                  TEXT_BACKGROUND_COLOR)
    pgb.text("LINES",(GRID_OFFSET+GRID_COLS+2)*BLOCK_SIZE+1,16*BLOCK_SIZE+1,TEXT_COLOR)
    pgb.text("%8s" % lines,(GRID_OFFSET+GRID_COLS+2)*BLOCK_SIZE+1,17*BLOCK_SIZE+1,TEXT_COLOR)
    
    # draw text (LEVEL)
    pgb.fill_rect((GRID_OFFSET+GRID_COLS+1)*BLOCK_SIZE+1,13*BLOCK_SIZE,
                  BLOCK_SIZE*7,BLOCK_SIZE*2,
                  TEXT_BACKGROUND_COLOR)
    pgb.text("LEVEL",(GRID_OFFSET+GRID_COLS+2)*BLOCK_SIZE+1,13*BLOCK_SIZE+1,TEXT_COLOR)
    pgb.text("%8s" % level,(GRID_OFFSET+GRID_COLS+2)*BLOCK_SIZE+1,14*BLOCK_SIZE+1,TEXT_COLOR)
    
    # draw text (SCORE)
    pgb.fill_rect((GRID_OFFSET+GRID_COLS+1)*BLOCK_SIZE+1,10*BLOCK_SIZE,
                  BLOCK_SIZE*7,BLOCK_SIZE*2,
                  TEXT_BACKGROUND_COLOR)
    pgb.text("SCORE",(GRID_OFFSET+GRID_COLS+2)*BLOCK_SIZE+1,10*BLOCK_SIZE+1,TEXT_COLOR)
    pgb.text("%8s" % score,(GRID_OFFSET+GRID_COLS+2)*BLOCK_SIZE+1,11*BLOCK_SIZE+1,TEXT_COLOR)
    
    # next tetromino box
    pgb.fill_rect((GRID_OFFSET+GRID_COLS+2)*BLOCK_SIZE,2*BLOCK_SIZE,
                  BLOCK_SIZE*6 ,BLOCK_SIZE*7,TEXT_BACKGROUND_COLOR)
    
    pgb.sprite(2,(GRID_OFFSET+GRID_COLS+2)*BLOCK_SIZE,2*BLOCK_SIZE) #upper left corner
    pgb.sprite(5,(GRID_OFFSET+GRID_COLS+3)*BLOCK_SIZE,2*BLOCK_SIZE) #top border
    pgb.sprite(5,(GRID_OFFSET+GRID_COLS+4)*BLOCK_SIZE,2*BLOCK_SIZE) #
    pgb.sprite(5,(GRID_OFFSET+GRID_COLS+5)*BLOCK_SIZE,2*BLOCK_SIZE) #
    pgb.sprite(5,(GRID_OFFSET+GRID_COLS+6)*BLOCK_SIZE,2*BLOCK_SIZE) #
    pgb.sprite(2,(GRID_OFFSET+GRID_COLS+7)*BLOCK_SIZE,2*BLOCK_SIZE) #upper right corner
    
    pgb.sprite(2,(GRID_OFFSET+GRID_COLS+2)*BLOCK_SIZE,8*BLOCK_SIZE) #lower left corner
    pgb.sprite(1,(GRID_OFFSET+GRID_COLS+3)*BLOCK_SIZE,8*BLOCK_SIZE) #lower border
    pgb.sprite(1,(GRID_OFFSET+GRID_COLS+4)*BLOCK_SIZE,8*BLOCK_SIZE) #
    pgb.sprite(1,(GRID_OFFSET+GRID_COLS+5)*BLOCK_SIZE,8*BLOCK_SIZE) #
    pgb.sprite(1,(GRID_OFFSET+GRID_COLS+6)*BLOCK_SIZE,8*BLOCK_SIZE) #
    pgb.sprite(2,(GRID_OFFSET+GRID_COLS+7)*BLOCK_SIZE,8*BLOCK_SIZE) #lower right corner
    
    for k in range(3,8):
        pgb.sprite(3,(GRID_OFFSET+GRID_COLS+2)*BLOCK_SIZE,k*BLOCK_SIZE) #left border
        pgb.sprite(4,(GRID_OFFSET+GRID_COLS+7)*BLOCK_SIZE,k*BLOCK_SIZE) #right border
    
    for i in range(4):
        draw_block((GRID_OFFSET+GRID_COLS+2)+tetrominos[next_n][i] % 2,
                   3+int(tetrominos[next_n][i] / 2), next_n)

def draw_block(j,i,n):
    # draw a tetris block of type n at the ith row and jth column
    # of the grid

    x = (GRID_OFFSET+j)*BLOCK_SIZE
    y = i*BLOCK_SIZE
    
    pgb.fill_rect(x,y,BLOCK_SIZE,BLOCK_SIZE,tetrominos_colors[n]) # main color
    pgb.rect(x,y,BLOCK_SIZE,BLOCK_SIZE,BLACK) # black border
    pgb.line(x+3,y+3,x+5,y+3,WHITE)
    pgb.line(x+3,y+3,x+3,y+5,WHITE)


#####################################################################

# show title screen and wait for a button
title_screen()

# game loop
while True:
    dx=0
    dy=1
    rotate=False
    delay=500

    if pgb.button_A() or pgb.button_B():
        if last_button!="UP":
            rotate=True
        last_button="UP"
    elif pgb.button_left():
            last_button="RIGHT"
            dx=-1
    elif pgb.button_right():
            last_button="RIGHT"
            dx=1
    elif pgb.button_down():
        last_button="DOWN"
        delay=0
    else:
        last_button="NONE"

    # save current position to restore it
    # in case the requested move generates a collision
    for i in range(4):
        prev_x[i] = x[i]
        prev_y[i] = y[i]
    
    # move left & right
    for i in range(4):
        x[i]+=dx
        
    if collision(x, y):
        # collision detected => impossible move
        # => restore previous position
        for i in range(4):
            x[i] = prev_x[i]
            y[i] = prev_y[i]
        
    # rotate
    if rotate:
        # center of rotation
        x0 = x[1]
        y0 = y[1]
        for i in range(4):
            x_=y[i]-y0
            y_=x[i]-x0
            x[i]=x0-x_
            y[i]=y0+y_
        
        if collision(x, y):
            # collision detected => impossible move
            # => restore previous position
            for i in range(4):
                x[i] = prev_x[i]
                y[i] = prev_y[i]
        else:
            has_rotated=True

    # move down
    ticks_ms = time.ticks_ms()
    if time.ticks_diff(ticks_ms, now) > delay:
        print(str(time.ticks_diff(ticks_ms, now)))
        now = ticks_ms
        
        if has_rotated:
            freq=180
        elif delay>0:
            freq=140
        else:
            freq=0
        pgb.sound(freq)
        has_rotated = False
            
        for i in range(4):
            prev_x[i]=x[i]
            prev_y[i]=y[i]
            y[i]+=dy
           
        if collision(x,y):
            # collision detected
            
            # collision at the top of the screen?
            # => game over
            for i in range(4):
                if prev_y[i]<=1:
                    pgb.sound(0)
                    game_over_screen()
            
            # => Store the last good position in the field
            for i in range(4):
                field[prev_y[i]][prev_x[i]]=n
            
            # => choose randomly the next trinomino
            n = next_n
            next_n = randint(0, 6)
            for i in range(4):
                x[i]=(tetrominos[n][i]) % 2;
                y[i]=int(tetrominos[n][i] / 2);
                
                x[i]+=int(GRID_COLS/2)
        
    # check lines
    k=GRID_ROWS-1
    for i in range(GRID_ROWS-1,0,-1):
        count=0
        for j in range(GRID_COLS):
            if field[i][j]>=0:
                count+=1
            field[k][j]=field[i][j]
        if count<GRID_COLS:
            k-=1
        else:
            # ith line complete
            lines+=1
            score+=40
            
            # make the line blink white <-> black
            
            for l in range(3):
                pgb.sound(1100)
                pgb.fill_rect(GRID_OFFSET*BLOCK_SIZE,i*BLOCK_SIZE,
                              GRID_COLS*BLOCK_SIZE,BLOCK_SIZE,WHITE)
                pgb.show()
                time.sleep(0.050)
                pgb.sound(2000)
                pgb.fill_rect(GRID_OFFSET*BLOCK_SIZE,i*BLOCK_SIZE,
                              GRID_COLS*BLOCK_SIZE,BLOCK_SIZE,BLACK)
                pgb.show()
                time.sleep(0.050)
            pgb.sound(0)
            
    
    #####################################################################
    # update screen 
    
    # background
    draw_background()

    # draw all the previous blocks
    for i in range(GRID_ROWS):
        for j in range(GRID_COLS):
            if field[i][j]>=0:
                # non empty
                draw_block(j,i,field[i][j])
    
    # draw the current block
    for i in range(4):
        draw_block(x[i],y[i],n)
    
    # transfer the frame buffer to the actual screen over the SPI bus
    pgb.show()

    pgb.sound(0)
