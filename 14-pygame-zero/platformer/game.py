import pgzrun
import sys

TITLE = 'JUMP PERSON'
WIDTH = 800
HEIGHT = 600

platforms = [Actor('stage/platform', anchor=('center', 'top'), center=(WIDTH//2, HEIGHT//2)),
             Actor('stage/platform', anchor=('center', 'top'), center=(WIDTH//2 + 200, HEIGHT//2 + 50)),
             Actor('stage/platform', anchor=('center', 'top'), center=(WIDTH//2 - 200, HEIGHT//2 + 50))]

player = Actor('player/tile_0000', anchor=('center', 'bottom'))
player.images = ['player/tile_0000', 'player/tile_0001']
player.midbottom = platforms[0].midtop
player.grounded = True
player.impulse = 0


def draw():
    global player
    
    screen.clear()
    
    if player.grounded:
        player.image = player.images[0]
    else:
        player.image = player.images[1]
        
    player.draw()
    draw_platforms()


def update(dt):
    player_movement(dt)
    ground_check()


def draw_platforms():
    global platforms
    for platform in platforms:
        platform.draw()


def ground_check():
    global player
    global platforms
    
    collision = False
    
    for platform in platforms:
        if player.colliderect(platform):
            player.pos = (player.x, platform.y)
            collision = True
            player.impulse = 0
            
    player.grounded = collision


def player_movement(dt):
    global player
    
    if keyboard.LEFT:
        player.x -= dt * 100
    
    if keyboard.RIGHT:
        player.x += dt * 100
    
    if not player.grounded:
        player.impulse -= 10.8
        player.y -= dt * player.impulse
        
    if player.top > HEIGHT:
        player.pos = (player.x, 0)


def on_key_down(key):
    global player
    if key == keys.SPACE and player.grounded:
        player.grounded = False
        player.impulse = 400
    if key == keys.ESCAPE:
        sys.exit()


pgzrun.go()