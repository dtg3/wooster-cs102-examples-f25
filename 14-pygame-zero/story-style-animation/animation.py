# This needs to be the first line to use pygame zero
import pgzrun

# Variable to hold a number that represents the
#   current state of the animation
current_state = 0

# Create an actor object and set the image to be 'idle'
explorer = Actor('idle')
# Provide by the pygame zero Actor to
#  set the position of the actor (x, y)
#  x or y less than zero will head off screen to the left or top
#  x or y greater than WIDTH or HEIGHT will head off screen right or bottom  
explorer.pos = (-50,400)
# Add a property to the actor that is a list of images
#   use for the walking cyle
explorer.images = ['walk037', 'walk038', 'walk039', 'walk040', 'walk041', 'walk042', 'walk043']
# Add a property to the actor to hold on to the idle image
explorer.idle = 'idle'
# This could also be made to be a property of the actor
#   which would avoid the need for global to access it in
#   the functions
walk_frame = 0

# Create an actor object for the emotes and set the
#  image to be the first elipsis dot
emotes = Actor('emote_dots1')
# Add a property to the actor to hold on to the exclamation emote image
emotes.exclaim = 'emote_exclamation'
# Add a property to the actor that is a list of images
#   use for the elipsis thinking animation
emotes.pause = ['emote_dots1', 'emote_dots2', 'emote_dots3']
# This could also be made to be a property of the actor
#   which would avoid the need for global to access it in
#   the functions
emote_frame = 0

# Create an actor object and set the image to be 'zwalk037'
#  since the zombie will be off screen and will never not
#  be moving we can simply set the first frame of animation
#  to be the first part of the walk cycle
zombie = Actor('zwalk037')
# Provide by the pygame zero Actor to
#  set the position of the actor (x, y)
#  x or y less than zero will head off screen to the left or top
#  x or y greater than WIDTH or HEIGHT will head off screen right or bottom 
zombie.pos = (-50,400)
# Add a property to the actor that is a list of images
#   use for the walking cyle
zombie.images = ['zwalk037', 'zwalk038', 'zwalk039', 'zwalk040', 'zwalk041', 'zwalk042', 'zwalk043']
# This could also be made to be a property of the actor
#   which would avoid the need for global to access it in
#   the functions
zwalk_frame = 0

# Variables with special meaning to pygame zero
#  these set the width and height of the game window
WIDTH = 640
HEIGHT = 640

# This function is provided by pygame zero
#   and makes the images that make up your game
#   or animation appear on the screen
def draw():
    # Get the current_state variable
    global current_state
    
    # Draw our forest background to the screen
    #  make sure to draw your backgrounds FIRST
    screen.blit('bgforest_small', (0,0))
    
    # Draw the explorer on top of the background
    explorer.draw()
    
    # Depending on the state of our application
    #   not everything needs to be drawn
    if current_state == 1:
        
        # Draw the emotes only after the are
        #   properly positioned above the head
        #   of the explorer
        if emotes.x == explorer.x:
            emotes.draw()
            
        # Zombie make an appearance    
        zombie.draw()
        
    elif current_state == 2:
        zombie.draw()

# This function is provided by pygame zero
#  and gets called 60 times each second
#  the dt parameter holds a floating point value of
#  the amount of time that has elapsed since the last
#  call to update
def update(dt):
    check_state(dt)

# This function controls the sequence of events in our animation
def check_state(dt):
    # Get the current_state variable to use/edit
    global current_state
    
    # If our animation is in the first state (0)
    if current_state == 0:
        # Check if the explorer has moved to the location
        #   at half the width of the screen
        if explorer.x > WIDTH // 2:
            # Stop the walking animation
            clock.unschedule(explorer_on)
            # Set the explorer's image to be standing still
            explorer.image = explorer.idle
            
            # Schedule two recurring events
            #   1) Show the emotes above the explorer
            #   2) Start animating the zombie to walk
            clock.schedule_interval(emote_time, 0.5)
            clock.schedule_interval(zombie_run, 0.2)
            
            # Change to the next animation state
            current_state += 1
        else:
            # If our explorer hasn't reached the middle of the
            #   screen, move the image further to the right
            explorer.x += 20*dt
    # If our animation has moved to the second state (1)         
    elif current_state == 1:
        # Check if the zombie is less than 150 pixels away
        # from the explorer
        if zombie.x < explorer.x - 150:
            # Move the zombie image to the right
            zombie.x += 20*dt
        else:
            # The zombie is now within 150 pixels of the explorer
            #   Stop the the emote and schedule the explorere to
            #   resume the walking animation
            clock.unschedule(emote_time)
            clock.schedule_interval(explorer_on, 0.2)
            
            # Change to the next animation state
            current_state += 1
    # This is the last phase of the animation
    else:
        # Both the zombie and the explorer
        #   run away of screen.
        # NOTE: This animation does not "end" on it's own
        #   and this state happens indefinitely until the
        #   program is closed.
        explorer.x += 20*dt
        zombie.x += 20*dt

# Enables the walk cycle animation frames for the explorer
def explorer_on():
    # Grab the walk_frame variable define at the top of the code
    global walk_frame
    
    # Accessing the index of explorer.images list
        #   using mod to ensure that the values
        #   are always in the range of 0 - len(explorer.images)
    explorer.image = explorer.images[walk_frame % len(explorer.images)]
    walk_frame += 1

# Enables the walk cycle animation frames for the zombie
#   works exactly the same as the explorer_on function
def zombie_run():
    global zwalk_frame
    zombie.image = zombie.images[zwalk_frame % len(zombie.images)]
    zwalk_frame += 1

# This displays the emote bubble above the explorer
def emote_time():
    # Grab the variable defined at the top of the code so we
    #   can use them
    global emote_frame
    global current_state
    
    # As long as our zombie is less than half the distance
    #   to our explorer..
    if zombie.x < explorer.x // 2:
        # position the emote above the exporer's head
        emotes.pos = (explorer.x, explorer.y - 50)
        
        # Change the image to show the moving elipsis (...)
        #   emote. Done in the same way as explorer_on and
        #   zombie_run
        emotes.image = emotes.pause[emote_frame % len(emotes.pause)]
        emote_frame += 1
    else:
        # Our zombie is now close enough to the explorer
        #  so we switch the emote to be the exclamation point
        emotes.pos = (explorer.x, explorer.y - 50)
        emotes.image = emotes.exclaim
    
# Schedule the explorer_on function to run at the start of the application
#    every .2 seconds
clock.schedule_interval(explorer_on, 0.2)

# This needs to be the last line to use pygame zero
pgzrun.go()
