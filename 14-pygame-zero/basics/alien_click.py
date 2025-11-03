# Need to have this at the top to use
#  pygame zero
import pgzrun

# Create an alien Actor object that uses the
#   'alien' picture as it's image. Remember that
#   pygame zero find these assets only if they have
#   ALL lowercase filenames and are in the folders
#   images or sounds.
alien = Actor('alien')

# Set the topright to be an anchor so the image
#   will start just off screen
alien.topright = 0, 10

# Add a property to the alien that holds a score
#   the advantage of this is we do not need to use
#   global to access this variable
alien.score = 0

# WIDTH and HEIGHT is provided by pygame zero
#   and sets the size of the screen
WIDTH = 600

# Note alien has a buit in height property to get the
#   height of the image representing that actor
HEIGHT = alien.height + 40

# The draw function is provided by pygame zero and
#   takes care of drawing things to the screen.
#   We just need to make sure we give it some work to do.
def draw():
    # The screen variable is provided by pygame zero to
    #   give you a way to interact with the game screen.
    # The screen's clear function wipes the screen completely
    #   and defaults it to black.
    screen.clear()
    
    # The alien Actor object has a buit in function to draw
    #   the object's image to the screen
    alien.draw()
    
    # This screen object offers the ability to draw text
    #   (plain or fancy) to the screen. This draws score
    #   near the bottom right of the screen
    screen.draw.text("Score: " + str(alien.score), bottomright=(WIDTH-10, HEIGHT-5))

# This function is provided by pygame zero
#  and gets called 60 times each second
def update():
    # We can update the alien Actor object's
    #   built in x coordinate value
    alien.x += 2
    
    # If the left side of the alien is past the
    #   WIDTH of the screen (the alien is off screen)
    #   we can reset the x value to zero to make it appear
    #   to come out the opposite side of the screen
    if alien.left > WIDTH:
        alien.x = 0

# This function is provided by pygame zero
#  and triggers if a mouse button is pressed.
#  The pos parameter hold the x, y coordinate of
#  the mouse when the button was clicked.
#  NOTE: This will not repeatedly trigger if you
#   hold the button down
def on_mouse_down(pos):
    # The alien can check to see if the pos coordinate
    #   (mouse click location) occurs on the image that
    #   represents the alien
    if alien.collidepoint(pos):
        # Call a custom function to change the alien
        set_alien_hurt()
        # Update the alien score
        alien.score += 1
    else:
        # You missed clicking the alien
        #   score gets decreased
        alien.score -= 1

# Function to update the alien image and
#   play a fun sound
def set_alien_hurt():
    # We can change the image that represents the alien
    #  by setting it's provided image propert to another
    #  image
    alien.image = 'alien_hurt'
    
    # The sounds variable is provided by Pygame and allows
    #  you to play any sound in the sounds folder. Note that
    #  the "eep" part of this line represents the sound file
    #  located in the sounds folder. We can then call play to
    #  hear the sound. WAV files are the best audio choice for
    #  pygame zero. MP3 and OGG files have more limited support.
    sounds.eep.play()
    
    # The clock is provided by pygame zero. This allows you to
    #   schedule (or unschedule) a function so it can be run after
    #   a set amount of time.
    # The example below schedules a single execution of the set_alien_normal
    #  function to run .75 seconds after it was scheduled. If you attempt to
    #  schedule the same function multiple times using schedule_unique it will
    #  first unschedule the call and then schedule a new event.
    clock.schedule_unique(set_alien_normal, 0.75)

# Reset the alien image to the starting image
def set_alien_normal():
    # You can change the image of the actor simply by assigning
    #   a new image to the actor's image property
    alien.image = 'alien'

# This needs to be the last line of code
pgzrun.go()