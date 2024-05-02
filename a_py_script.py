import pygame as pg

# Initialize Pygame
pg.init()

# Set screen dimensions
SCREEN_WIDTH = 640
SCREEN_HEIGHT = 480
screen = pg.display.set_mode([SCREEN_WIDTH, SCREEN_HEIGHT])

# Main loop: run until window is closed
running = True
while running:
    for event in pg.event.get():
        if event.type == pg.QUIT:
            running = False
        elif event.type == pg.KEYDOWN:
            if event.key == pg.K_q:
                running = False

# Clean up and quit
pg.quit()
