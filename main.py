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
    square_selected = () # Keep track of the last click from the user 
    player_clicks = [] # Keeps track of player clicks (2 Tupels)

    while running: 
        for event in py.event.get():
            if event.type == py.QUIT:
                running = False
            elif event.type == py.MOUSEBUTTONDOWN:  #If click something this condition will be activated 
                location = py.mouse.get_pos() #(x, y) Location of the mouse 
                col = location[0] // SQUARE_SIZE
                row = location[1] // SQUARE_SIZE
                if square_selected == (row, col):
                    square_selected = ()
                    player_clicks = []
                else:
                    square_selected = (row, col)
                    player_clicks.append(square_selected)
                if len(player_clicks) == 2:
                    row_move1 = list(player_clicks[0])[0]
                    col_move1 = list(player_clicks[0])[1]
                    row_move2 = list(player_clicks[1])[0]
                    col_move2 = list(player_clicks[1])[1]
                    gs.making_a_move(row_move1, col_move1, row_move2, col_move2)
                    player_clicks = []
                    square_selected = ()

                    
        draw_game_state(screen, gs) 
        clock.tick(FPS)       
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

    