import pgzrun

WIDTH = 800
HEIGHT = 600

# Create an Actor to drag
alien = Actor('alien', (WIDTH // 2, HEIGHT // 2))

# Variables to track dragging state
alien.dragging = False
alien.offset_x = 0
alien.offset_y = 0

def draw():
    screen.fill((200, 200, 255))
    alien.draw()

def on_mouse_down(pos):
    global alien
    if alien.collidepoint(pos):
        alien.image = 'alien_drag'
        alien.dragging = True
        mouse_x, mouse_y = pos
        # x and y of an Actor (by default) is our top left
        # of the image this is why where the mouse is on
        # the image will always result in a subtraction as
        # the mouse x,y will always be the bigger value.
        alien.offset_x = mouse_x - alien.x
        alien.offset_y = mouse_y - alien.y

def on_mouse_up(pos):
    global alien
    alien.dragging = False
    alien.image = 'alien'

def on_mouse_move(pos):
    global alien
    if alien.dragging:
        mouse_x, mouse_y = pos
        # Reposition the alient with respect to where the
        # mouse has "grabbed" the image.
        alien.x = mouse_x - alien.offset_x
        alien.y = mouse_y - alien.offset_y
    
def on_key_down(key):
    if key == keys.ESCAPE:
        quit()
        
pgzrun.go()