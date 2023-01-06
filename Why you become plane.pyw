import pygame
import sys
import random
import os

pygame.init()

window_size = (900, 700)

screen = pygame.display.set_mode(window_size)

current_time = pygame.time.get_ticks()

subdirectory = "Images"
filename = "explosion.png"
image_path = os.path.join(subdirectory, filename)

# screen_fill = screen.fill((104, 50, 39))
explosion_image = pygame.image.load("images\Bomb.png")

explosion_pos = (50, 100)
explosion_vel = (2.5, 3)

clock = pygame.time.Clock()

GroundHits = 0

# config
position_monitor = False

font = pygame.font.Font(None, 36)

# Set the change back time (in milliseconds)
# change_back_time1 = 2000
change_back_time = 500
change_back_start_time = 0
image_changed = False
# is_plane = False
# is_explode = False

while True:

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()

        elif event.type == pygame.MOUSEBUTTONDOWN:

            mouse_pos = pygame.mouse.get_pos()

            if (explosion_pos[0] < mouse_pos[0] < explosion_pos[0] + explosion_image.get_width()) and (explosion_pos[1] < mouse_pos[1] < explosion_pos[1] + explosion_image.get_height()):

                explosion_vel = (random.randint(-5, 5), random.randint(-5, 5))

    if explosion_pos[0] < 0 or explosion_pos[0] + explosion_image.get_width() > window_size[0]:
        explosion_vel = (-explosion_vel[0], explosion_vel[1])

    if explosion_pos[0] < 0 or explosion_pos[0] + explosion_image.get_width() > window_size[0]:
        explosion_image = pygame.image.load("images\plane.jfif")
        explosion_vel = (explosion_vel[0], explosion_vel[1])
        image_changed = True
        # is_plane = True
        change_back_start_time = current_time

    if explosion_pos[1] + explosion_image.get_height() > window_size[1]:
        explosion_image = pygame.image.load("images\explosion.png")
        explosion_vel = (explosion_vel[0], -explosion_vel[1])
        GroundHits += 1
        # screen_fill = screen.fill ((255, 255, 255))
        image_changed = True
        # is_explode = True
        change_back_start_time = current_time

    elif explosion_pos[1] < 0:
        explosion_vel = (explosion_vel[0], -explosion_vel[1])

    explosion_pos = (explosion_pos[0] + explosion_vel[0],
                     explosion_pos[1] + explosion_vel[1])

    screen.fill((104, 50, 39))

    screen.blit(explosion_image, explosion_pos)

    # Check config to change
    if position_monitor:
        y = 10
        Position_Counter = font.render(
        "Position: (" + str(explosion_pos[0]) + ", " + str(explosion_pos[1]) + ")", True, (250, 250, 255))
        screen.blit(Position_Counter, (10, y))
        y += 30
        Velocity_Counter = font.render(
        "Velocity: (" + str(explosion_vel[0]) + ", " + str(explosion_vel[1]) + ")", True, (250, 250, 255))
        screen.blit(Velocity_Counter, (10, y))
        y += 30
        Hits_Counter = font.render(
        "Ground Hits: " + str(GroundHits), True, (250, 250, 255))
        screen.blit(Hits_Counter, (10, y))

    else:
        y = 10
        Velocity_Counter = font.render(
        "Velocity: (" + str(explosion_vel[0]) + ", " + str(explosion_vel[1]) + ")", True, (250, 250, 255))
        screen.blit(Velocity_Counter, (10, y))
        y += 30
        Hits_Counter = font.render(
        "Ground Hits: " + str(GroundHits), True, (250, 250, 255))
        screen.blit(Hits_Counter, (10, y))

    if image_changed:  # and is_explode:
        if current_time - change_back_start_time >= change_back_time:
            explosion_image = pygame.image.load("images\bomb.png")
            # screen_fill = screen.fill ((104, 50, 39))
            explosion_rect = explosion_image.get_rect()
            # is_explode = False
            image_changed = False

    # if image_changed and is_plane:
       # if current_time - change_back_start_time >= change_back_time:
            # screen_fill = screen.fill ((104, 50, 39))
        #    is_plane = False
        #    image_changed = False

    pygame.display.flip()

    current_time = pygame.time.get_ticks()

    clock.tick(60)
