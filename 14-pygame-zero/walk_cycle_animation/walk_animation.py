# This code example shows ONE approach to interactive
#	character animation, in this case, walking/running.
#	This is different than using the animate method for
#	Actors in the documentation. That is mostly for
#	positioning or creating an "animated" scene where
#	you need to dictate an end coordinate and want 
#	Pygame zero to handle the rest.
import pgzrun
import sys


# Setup Window Properties
WIDTH = 600
HEIGHT = 200
TITLE = 'Walking Animation Example'


# Global "player" character
explorer = None


def setup_explorer():
    """
    Function called once when the game is run
    to help setup our player character
    """
    global explorer
    
    # Position the character in the middle of the screen at the bottom
    #	we use the positioning relative to the middle bottom of the
    #	explorer image. The "default" image should be the 'idle' image
    explorer = Actor('e_idle', midbottom=(WIDTH // 2, HEIGHT - 1))
    

    # Since pygame zero has limited support for
    #	animation frames we need to do this ourselves
    
    # We will need to change the image frames, so we need to
    #	keep track of all the images needed animated and non-
    #	animated states
    
    # Idle image -> No animation
    explorer.idle = 'e_idle'
    
    # A dictionary that will hold the animation frames
    #	for walking left and right
    explorer.walk = {'left':[], 'right':[]}

    # Add the necessary walking images to the dictionary
    for number in range(1, 8):
        explorer.walk['left'].append(f'e_walkleft{number}')
        explorer.walk['right'].append(f'e_walkright{number}')
    
    # We need to keep track of what animation frame (image) we
    #	need to show...
    explorer.walk_frame = 0
    
    # and what direction we will be walking
    explorer.walk_direction = None


def explorer_walk():
    """
    This function will be set to run at a regular interval to change the image
    of our character to "simulate" a walk/run.
    """
    global explorer
    
    explorer.walk_frame = (explorer.walk_frame + 1) % len(explorer.walk[explorer.walk_direction])
    explorer.image = explorer.walk[explorer.walk_direction][explorer.walk_frame]


def draw():
    """
    This is the draw function supplied by Pygame Zero
    """
    screen.clear()
    explorer.draw()


def update(dt):
    """
    This is the update function supplied by Pygame Zero. This
    will run roughly 60 times a second.
    """
    global explorer
    
    if explorer.walk_direction:
        if explorer.walk_direction == 'right':
            explorer.x += 200 * dt
        elif explorer.walk_direction == 'left':
            explorer.x -= 200 * dt
            

def on_key_down(key):
    """
    This function gets called automatically when a key is pressed, but
    only the first time the key goes down.
    """
    global explorer
    
    # On escape exit the program
    if key == keys.ESCAPE:
        sys.quit()
    
    # if right or left is pressed set the walking direction
    #	and schedule the animation function
    if key == keys.RIGHT:
        if not explorer.walk_direction:
            explorer.walk_direction = 'right'
            clock.schedule_interval(explorer_walk, .09)
    if key == keys.LEFT:
        if not explorer.walk_direction:
            explorer.walk_direction = 'left'
            clock.schedule_interval(explorer_walk, .09)

       
def on_key_up(key):
    """
    This function gets called automatically when a key is released, but
    only the first time the key goes down.
    """
    global explorer

    # When the right or left key is released we need
    #	to restore the actor to an idle state and
    #	change any other related attributes
    if key == keys.RIGHT:
        if explorer.walk_direction:
            clock.unschedule(explorer_walk)
            explorer.image = explorer.idle
            explorer.walk_frame = 0
            explorer.walk_direction = None
    if key == keys.LEFT:
        if explorer.walk_direction:
            clock.unschedule(explorer_walk)
            explorer.image = explorer.idle
            explorer.walk_frame = 0
            explorer.walk_direction = None


def init_game():
    """
    Function that gets called to setup everything before we run our game
    for the first time.
    """
    setup_explorer()


init_game()
pgzrun.go()
