import pygame as py

WIDTH, HEIGHT = 512, 512
DIMENSION = 8
SQUARE_SIZE = WIDTH//DIMENSION

IMAGES = {}

def load_images():
    pieces = ["bR", "bN", "bB", "bQ", "bK", "bP", "wR", "wN", "wB", "wQ", "wK", "wP"]
    
    for pis in pieces:
        IMAGES[pis] = py.transform.scale(py.image.load("images/" + pis + ".png"), (SQUARE_SIZE, SQUARE_SIZE))

load_images()


##!!! Changing !! 