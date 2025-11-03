# NOTE: You need to install the "pgzero" package in Thonny
#	like we did with Pillow or the pgzrun import will not work

# This import must be the first line of the program
import pgzrun
import sys


# These are special values to set
#   the screen dimensions
WIDTH = 600
HEIGHT = 600


# This is a special function that
#   is called when things need to
#   be drawn to the screen
def draw():
    # Fill sets the screen to a color
    #   default is black. Fill takes one argument
    #   which is a tuple of three values representing
    #   Red, Green, and Blue.
    #   NOTE: A tuple is simply values or variables that
    #   are surrounded by parentheses and separated by commas.
    #   THEY ARE DIFFERENT FROM FUNCTION PARAMETERS OR ARGUMENTS
    #   TO A FUNCTION. Example Tuple:  (10, 20, 30)
    screen.fill( (255,0,0) )


# Pygame Zero provides some "hooks" that allow you to check for
#   certain actions or events. We are doing a simple check here
#   to see if we have pressed the escape key, and then we quit
#   the application.
def on_key_down(key):
    if key == keys.ESCAPE:
        sys.exit()


# This statement must be the last line of the program
pgzrun.go()
