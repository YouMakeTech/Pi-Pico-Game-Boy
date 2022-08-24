# GameOfLife.py by YouMakeTech
# John Conway's Game of Life for the Raspberry Pi Pico Game Boy

from PicoGameBoy import PicoGameBoy
import random
pgb = PicoGameBoy()

# Predefined colors
BLACK = PicoGameBoy.color(0,0,0)
WHITE = PicoGameBoy.color(255,255,255)
RED = PicoGameBoy.color(255,0,0)
GREEN = PicoGameBoy.color(0,255,0)
BLUE = PicoGameBoy.color(0,0,255)

# Game parameters
WIDTH = pgb.width        # screen width in pixels
HEIGHT = pgb.height      # screen height in pixels
CELL_SIZE = 8            # width and height of cells in pixels
POPULATION_PERCENT = 12  # Initial population size as function of total surface in %
BACKGROUND_COLOR = BLACK
CELL_COLOR = GREEN

# Board initialisation
BOARD_SIZE_X = int(WIDTH/CELL_SIZE)
BOARD_SIZE_Y = int(HEIGHT/CELL_SIZE)
BOARD_SURFACE = BOARD_SIZE_X * BOARD_SIZE_Y

board=[]
for i in range(0,BOARD_SIZE_Y):
    line = []
    for j in range(0,BOARD_SIZE_X):
        line.append(0)
    board.append(line)


# Initial number of cells 
NUMBER_OF_CELLS = int((POPULATION_PERCENT)/100 * BOARD_SURFACE);

# Create the initial population
for i in range(0,NUMBER_OF_CELLS):
    # Randomly place cells on the board
    board[random.randint(0,BOARD_SIZE_Y-1)][random.randint(0,BOARD_SIZE_X-1)] = CELL_COLOR
    
# run the animation
while True:
    # Update the screen
    pgb.fill(BACKGROUND_COLOR)
    for i in range(0,BOARD_SIZE_Y):
        for j in range(0,BOARD_SIZE_X):
            if board[i][j]!=0:
                pgb.fill_rect(j*CELL_SIZE,i*CELL_SIZE,CELL_SIZE,CELL_SIZE,board[i][j])
    pgb.show()
    
    # count number of neighbors for each position
    for i in range(0,BOARD_SIZE_Y):
        for j in range(0,BOARD_SIZE_X):
            number_neighbors = 0
            
            if i>1 and j>1 and board[i-1][j-1]!=0:
                number_neighbors+=1
            if i>1 and board[i-1][j]!=0:
                number_neighbors+=1
            if i>1 and j<BOARD_SIZE_X-1 and board[i-1][j+1]!=0:
                number_neighbors+=1
            if i<BOARD_SIZE_Y-1 and j>1 and board[i+1][j-1]!=0:
                number_neighbors+=1
            if i<BOARD_SIZE_Y-1 and board[i+1][j]!=0:
                number_neighbors+=1
            if i<BOARD_SIZE_Y-1 and j<BOARD_SIZE_Y-1 and board[i+1][j+1]!=0:
                number_neighbors+=1
            if j>1 and board[i][j-1]!=0:
                number_neighbors+=1
            if j<BOARD_SIZE_X-1 and board[i][j+1]!=0:
                number_neighbors+=1
            
            # The game's rules
            if board[i][j]!=BLACK:
                # There is a living cell at row #i col #j
                # It survives only if it surrounded by 2 or 3 neighbors
                if number_neighbors<2 or number_neighbors>3:
                    board[i][j] = 0
            else:
                # row #i col #j is empty
                # Create a new cell at (i,j) if it is surrounded by exactly 3 neighbors
                if number_neighbors==3:
                    board[i][j] = CELL_COLOR
