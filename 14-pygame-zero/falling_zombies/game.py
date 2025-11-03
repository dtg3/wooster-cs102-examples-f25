# Need to have this at the top to use
#  pygame zero
import pgzrun

# This is a standard python module for
#  generating random numbers
import random


# Used for exiting the program
import sys


# This variable is provided by pygame zero
#   and controls changes to the window title
TITLE = 'ZOMBIE DROP'


# These variables are provided by pygame zero
#   and control the window dimensions
WIDTH = 640
HEIGHT = 640


# Create an actor object
#   for our "player" character
explorer = Actor('eidle')
# Change the x and y position of the explorer
#   Actor object
explorer.pos = (100, 500)
explorer.lives = 3
explorer.invincible = False


lives = [Actor('heart', bottomright=(WIDTH-(33*2)-3, HEIGHT-3)),
         Actor('heart', bottomright=(WIDTH-33-3, HEIGHT-3)),
         Actor('heart', bottomright=(WIDTH-3, HEIGHT-3))]

# The zombies variable will reference a list of zombies
#   for now, the list is empty
zombies = []

# Tracking Game State
current_state = 0
STATE = ['title', 'gameplay', 'gameover']

# Speed of the zombies
difficulty = 60


def show_title_screen():
    screen.draw.text("Zombie Drop", (WIDTH // 4, 100), color='black', fontsize=70)
    screen.draw.text("Press Any Key to Start", (WIDTH // 3, HEIGHT - 100), color='black', fontsize=25)


def show_gameover():
    global zombies
    global explorer
    global difficulty
    
    clock.unschedule(spawn_zombie)
    clock.unschedule(increase_challenge)
    screen.draw.text("Game Over", (WIDTH // 4, 100), color='black', fontsize=70)
    screen.draw.text("Press Any Key to Start", (WIDTH // 3, HEIGHT - 100), color='black', fontsize=25)
    zombies.clear()
    explorer.lives = 3
    difficulty = 60
    

# This function is provided by pygame zero
#   and makes the images that make up your game
#   or animation appear on the screen
def draw():
    global zombies
    global current_state
    global explorer
    
    # Draw the picture named bggrass to the screen
    #   starting at 0,0 (top left of the screen)
    screen.blit('bggrass', (0,0))
    
    # Show title screen
    if STATE[current_state] == STATE[0]:
        show_title_screen()
    
    elif STATE[current_state] == STATE[1]:    
        # Get each zombie in our zombies list
        for zombie in zombies:
            # Tell each zombie to draw to the screen
            zombie.draw()
        
        # Tell the explorer to draw to the screen
        explorer.draw()
        
        draw_hearts()
    
    elif STATE[current_state] == STATE[2]:
        show_gameover()    
    

# This function is provided by pygame zero
#  and gets called 60 times each second
#  the dt parameter holds a floating point value of
#  the amount of time that has elapsed since the last
#  call to update
def update(dt):
    global current_state
    global explorer
    global zombies
    
    # Call our check_keys function
    #   to see if any keyboard keys are pressed
    check_keys(dt)
    
    # Call our function to move the zombies
    move_zombie(dt)
    
    check_zombie_collision()
    
    if explorer.lives == 0:
        current_state += 1
    
    # Remove any zombies that are no longer on screen
    zombies = zombie_cleanup()


def check_zombie_collision():
    global zombies
    global explorer
    
    for zombie in zombies:
        if not explorer.invincible and explorer.colliderect(zombie):
            explorer.lives -= 1
            explorer.invincible = True
            clock.schedule_unique(vulnerable, 5)


def vulnerable():
    global explorer
    
    explorer.invincible = False


# Function update the position of the zombies
def move_zombie(dt):
    global zombies
    global difficulty
    
    # Loop over all the zombies in the list
    for zombie in zombies:
        # Add to the y position (zombie
        #   moving down)
        zombie.y += dt * difficulty
        
        # Check if the zombie is off screen
        if zombie.y > HEIGHT + 100:
            # Mark it as safe to cleanup
            zombie.alive = False


def increase_challenge():
    global difficulty
    difficulty += 60


# Function to dynamically create zombies
def spawn_zombie():
    global zombies
    
    # Use random.randint to get a random number
    #   between the first and second arguments
    xpos = random.randint(50, WIDTH-50)
    
    # Create zombie actor
    zombie = Actor('zombie')
    
    # Set the zombie actors position to be off screen
    #   (at the top) and set the x value to be the
    #   randomly generated value
    zombie.pos = (xpos, -50)
    
    # Add a property to set the zombies to start
    #   "alive" so we don't clean it up my accident
    zombie.alive = True
    
    # Append (add) our zombie to the end of the list
    #   of other zombie objects
    zombies.append(zombie)


# Function to delete zombies that are off screen
def zombie_cleanup():
    global zombies
    
    # Create a new empty list
    new_list = []
    
    # Get each zombie from the list of zombies
    for zombie in zombies:
        # Check if the zombie is "alive"
        #   since alive is True or False this
        #   condition is valid
        if zombie.alive:
            new_list.append(zombie)
    
    # Return the new list without the zombies that
    #   are not alive
    return new_list


# Function to check what keys are being pressed
def check_keys(dt):
    global explorer
    
    # Check if the left arrow key is down
    if keyboard.left:
        # Move the explorer to the left
        explorer.x -= dt * 100
    # Check if the right arrow key is down
    if keyboard.right:
        # Move the explorer to the right
        explorer.x += dt * 100


def on_key_down(key):
    global current_state
    
    if key == keys.ESCAPE:
        sys.exit()
    else:
        if key and STATE[current_state] == STATE[0]:
            current_state += 1
            # Schedule a repeating action that calls spawn_zombie every
            #   five seconds. Also start the difficulty increase timer.
            clock.schedule_interval(spawn_zombie, 5)
            clock.schedule_interval(increase_challenge, 30)
        elif key and STATE[current_state] == STATE[2]:
            current_state = 1
            clock.schedule_interval(spawn_zombie, 5)
            clock.schedule_interval(increase_challenge, 30)


def draw_hearts():
    global explorer
    
    for heart in range(explorer.lives):
        lives[heart].draw()


# This needs to be the last line of code
pgzrun.go()
