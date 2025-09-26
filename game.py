import pygame
import pymunk
import pymunk.pygame_util

# Initialize Pygame and Pymunk
pygame.init()
screen = pygame.display.set_mode((800, 600))
clock = pygame.time.Clock()
space = pymunk.Space()
space.gravity = (0, 900)  # Gravity downward
draw_options = pymunk.pygame_util.DrawOptions(screen)

# Create static ground plane
ground = pymunk.Segment(space.static_body, (0, 500), (800, 500), 5)
ground.friction = 0.5
space.add(ground)

# Create falling squares
def create_square(space, pos):
    body = pymunk.Body()
    body.position = pos
    shape = pymunk.Poly.create_box(body, (30, 30))
    shape.mass = 1
    shape.friction = 0.5
    space.add(body, shape)
    return shape

# Add three squares at different positions
create_square(space, (200, 100))
create_square(space, (300, 150))
create_square(space, (400, 200))

# Main loop
running = True
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    # Step physics simulation
    space.step(1/60)

    # Draw
    screen.fill((255, 255, 255))  # White background
    space.debug_draw(draw_options)
    pygame.display.flip()
    clock.tick(60)

pygame.quit()