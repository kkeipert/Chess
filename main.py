from asyncio import constants
import pygame as py
from constants import DIMENSION, SQUARE_SIZE, WIDTH, HEIGHT, load_images, IMAGES
import chessEngine

FPS = 30 

py.init()
py.display.set_caption("Chess")

# Runs the actual game 
def main():

    screen = py.display.set_mode((WIDTH, HEIGHT))
    
    clock = py.time.Clock()
    gs = chessEngine.GameState()
    load_images()
    running = True 

    while running: 
        for event in py.event.get():
            if event.type == py.QUIT:
                running = False
        draw_game_state(screen, gs)        
        py.display.flip()      
        

def draw_game_state(screen, gs):
    draw_squares_board(screen)

    draw_pieces(screen, gs.board) #Draw piece on Top of those squares 


def draw_squares_board(screen):
    colors = [py.Color("white"), py.Color("light grey")]
    for row in range(DIMENSION):
        for column in range(DIMENSION):
            color = colors[(row+column) % 2]
            py.draw.rect(screen, color, py.Rect(column*SQUARE_SIZE, row*SQUARE_SIZE, SQUARE_SIZE, SQUARE_SIZE))

def draw_pieces(screen, board):
    for row in range(DIMENSION):
        for column in range(DIMENSION):
            piece = board[row][column]
            if piece != "--":
                screen.blit(IMAGES[piece], py.Rect(column*SQUARE_SIZE, row*SQUARE_SIZE, SQUARE_SIZE, SQUARE_SIZE))

if __name__ == "__main__":
    main()

    