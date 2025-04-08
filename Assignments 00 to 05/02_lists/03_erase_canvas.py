import streamlit as st
import numpy as np
import pygame

# Initialize pygame
pygame.init()

# Constants
GRID_SIZE = 20
CELL_SIZE = 30
WIDTH, HEIGHT = GRID_SIZE * CELL_SIZE, GRID_SIZE * CELL_SIZE
ERASER_SIZE = 60  # Eraser size

# Create canvas
canvas = np.ones((GRID_SIZE, GRID_SIZE, 3)) * [0, 0, 255]  # Blue canvas

# Set up pygame window
screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Canvas Eraser")

# Run loop
running = True
erasing = False
eraser_x, eraser_y = 0, 0

while running:
    screen.fill((255, 255, 255))  # Clear screen

    # Event handling
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        elif event.type == pygame.MOUSEBUTTONDOWN:
            erasing = True
        elif event.type == pygame.MOUSEBUTTONUP:
            erasing = False
        elif event.type == pygame.MOUSEMOTION:
            eraser_x, eraser_y = event.pos

    # Draw grid
    for row in range(GRID_SIZE):
        for col in range(GRID_SIZE):
            color = canvas[row, col] * 255
            pygame.draw.rect(screen, color, (col * CELL_SIZE, row * CELL_SIZE, CELL_SIZE, CELL_SIZE))

    # Erase cells in contact with the eraser
    if erasing:
        for row in range(GRID_SIZE):
            for col in range(GRID_SIZE):
                cell_x, cell_y = col * CELL_SIZE, row * CELL_SIZE
                if (
                    eraser_x < cell_x + CELL_SIZE
                    and eraser_x + ERASER_SIZE > cell_x
                    and eraser_y < cell_y + CELL_SIZE
                    and eraser_y + ERASER_SIZE > cell_y
                ):
                    canvas[row, col] = [1, 1, 1]  # Set cell to white

    # Draw eraser
    pygame.draw.rect(screen, (255, 255, 255), (eraser_x, eraser_y, ERASER_SIZE, ERASER_SIZE), 0)

    pygame.display.flip()

pygame.quit()