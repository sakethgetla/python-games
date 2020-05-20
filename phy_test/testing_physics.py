import pymunk               # Import pymunk..
import pygame


#while True:                 # Infinite loop simulation
#    space.step(0.02)        # Step the simulation one step forward
#    space.debug_draw(print_options) # Print the state of the simulation

pygame.init()
gray = (115, 115, 115)
black = (0, 0, 0)
red = (255, 0, 0)
blue = (0, 0, 255)
green = (0, 255, 0)
lightGreen = (155, 255, 0)
yellow = (255, 255, 0)
white = (255, 255, 255)

display_width = 1300
display_height = 900

pointSize = 50

width = 10
height = width

clock = pygame.time.Clock()
gameDisplay = pygame.display.set_mode((display_width, display_height))
FPS = 30

space = pymunk.Space()      # Create a Space which contain the simulation
#space.gravity = 0, 1000     # Set its gravity
#space.gravity = 0, 0     # Set its gravity
space.iterations = 35
space.gravity = (0.0, +900.0)

# create floor
floor_height = 80
body = pymunk.Body(body_type=pymunk.Body.STATIC)
line = [0, display_height - floor_height, display_width, display_height + 50 -  floor_height]
shape = pymunk.Segment(body, [line[0], line[1]], [line[2], line[3]], 0.0)
shape.friction = 0.1
shape.elasticity = 0.7

#space.add(shape)       # Add both body and shape to the simulation
space.add(body, shape)       # Add both body and shape to the simulation

# create box
#size = 32
mass = 11.0
x = 500 
y = 200
boxSize = (50, 50)
moment = pymunk.moment_for_box(mass, boxSize)
#moment = pymunk.moment_for_box(mass, (boxSize[0], boxSize[1]))
body = pymunk.Body(mass, moment)
body.position = pymunk.Vec2d(x, y)
shape = pymunk.Poly.create_box(body, boxSize, boxSize[0]//2)
shape.elasticity = 0.7
shape.friction = 0.1
space.add(body, shape)
print('body.position = ', [(int(a[0]), int(a[1])) for a in shape.get_vertices()])
#space.add(shape)       # Add both body and shape to the simulation


print_options = pymunk.SpaceDebugDrawOptions() # For easy printing

def draw(gameDisplay, color, pos, size):
    #pygame.draw.rect(gameDisplay, color, [pos[0], pos[1], size[0], size[1]] )
    pygame.draw.polygon(gameDisplay, color, [[int(a[0]), int(a[1])] for a in shape.get_vertices()])
    pygame.draw.line(gameDisplay, color, [line[0], line[1]], [line[2], line[3]])

def gameLoop():
    mouse = pygame.mouse.get_pos()
    click = pygame.mouse.get_pressed()
    gameDisplay.fill(gray)
    gameExit = False
    global gravityON
    nodes = []

    while not gameExit:
        space.step(0.02)        # Step the simulation one step forward
        print('body.position = ', [[int(a[0]), int(a[1])] for a in shape.get_vertices()])
        #print('body.position = ', body.get_vertices())
        draw(gameDisplay, red, body.position, boxSize)
        mouse = pygame.mouse.get_pos()
        click = pygame.mouse.get_pressed()
        

        pygame.display.update()
        gameDisplay.fill(gray)
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                gameExit = True

        clock.tick(FPS)
        key = pygame.key.get_pressed()
        if key[pygame.K_q] :
            gameExit = True

    pygame.quit()
    quit()
gameLoop()
