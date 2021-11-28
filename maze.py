import os
import sys
import random
import pygame


# Class for the orange dude
class Player(object):

    def __init__(self):
        self.rect = pygame.Rect(32, 32, 16, 16)

    def move(self, dx, dy):

        # Move each axis separately. Note that this checks for collisions both times.
        if dx != 0:
            self.move_single_axis(dx, 0)
        if dy != 0:
            self.move_single_axis(0, dy)

    def move_single_axis(self, dx, dy):

        # Move the rect
        self.rect.x += dx
        self.rect.y += dy

        # If you collide with a wall, move out based on velocity
        for wall in walls:
            if self.rect.colliderect(wall.rect):
                if dx > 0:  # Moving right; Hit the left side of the wall
                    self.rect.right = wall.rect.left
                if dx < 0:  # Moving left; Hit the right side of the wall
                    self.rect.left = wall.rect.right
                if dy > 0:  # Moving down; Hit the top side of the wall
                    self.rect.bottom = wall.rect.top
                if dy < 0:  # Moving up; Hit the bottom side of the wall
                    self.rect.top = wall.rect.bottom


# Nice class to hold a wall rect
class Wall(object):

    def __init__(self, pos):
        walls.append(self)
        self.rect = pygame.Rect(pos[0], pos[1], 16, 16)


# Initialise pygame
os.environ["SDL_VIDEO_CENTERED"] = "1"
pygame.init()

# Set up the display
pygame.display.set_caption("Get to the red square!")
screen = pygame.display.set_mode((320, 240))

clock = pygame.time.Clock()
walls = []  # List to hold the walls
player = Player()  # Create the player

# Holds the level layout in a list of strings.
level = [
    "WWWWWWWWWWWWWWWWWWWW",
    "WW WW              W",
    "WW WW     WWWWWW   W",
    "WW WWWWW       W   W",
    "WW WW        WWWW  W",
    "WW WW  WWWW        W",
    "WW WW     W W      W",
    "WW WW     W   WWW WW",
    "WW WWWW WWW   W W  W",
    "WW WW W   W   W W  W",
    "WW WW W   WWWWW W  W",
    "WW WW    WW        W",
    "WW WW WWWW   WWW   W",
    "WWEWW W       W    W",
    "WWWWWWWWWWWWWWWWWWWW",
]

# Parse the level string above. W = wall, E = exit
x = y = 0
for row in level:
    for col in row:
        if col == "W":
            Wall((x, y))
        if col == "E":
            end_rect = pygame.Rect(x, y, 16, 16)
        x += 16
    y += 16
    x = 0