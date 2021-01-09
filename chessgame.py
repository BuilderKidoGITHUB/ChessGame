import pygame
import os
from pygame.locals import *
pygame.init()
pygame.font.init()
width = 800
height = 800
col = width // 8
row = height // 8
screen = pygame.display.set_mode(size = (width,height))
screen.fill(pygame.Color(255,255,255))
class Grid:
    row = 8
    column = 8
    white_dir = -1
    black_dir = 1
    black_king = pygame.image.load(os.path.join('chess', 'chess_piece_2_black_king.png'))
    black_bishop = pygame.image.load(os.path.join('chess', 'chess_piece_2_black_bishop.png'))
    black_knight = pygame.image.load(os.path.join('chess', 'chess_piece_2_black_knight.png'))
    black_pawn = pygame.image.load(os.path.join('chess', 'chess_piece_2_black_pawn.png'))
    black_queen = pygame.image.load(os.path.join('chess', 'chess_piece_2_black_queen.png'))
    black_rook = pygame.image.load(os.path.join('chess', 'chess_piece_2_black_rook.png'))
    white_king = pygame.image.load(os.path.join('chess', 'chess_piece_2_white_king.png'))
    white_bishop = pygame.image.load(os.path.join('chess', 'chess_piece_2_white_bishop.png'))
    white_knight = pygame.image.load(os.path.join('chess', 'chess_piece_2_white_knight.png'))
    white_pawn = pygame.image.load(os.path.join('chess', 'chess_piece_2_white_pawn.png'))
    white_queen = pygame.image.load(os.path.join('chess', 'chess_piece_2_white_queen.png'))
    white_rook = pygame.image.load(os.path.join('chess', 'chess_piece_2_white_rook.png'))
    def __init__(self):
        self.grid = [
        [self.black_rook, self.black_knight, self.black_bishop, self.black_king,self.black_queen , self.black_bishop, self.black_knight, self.black_rook],
        [self.black_pawn, self.black_pawn, self.black_pawn, self.black_pawn, self.black_pawn, self.black_pawn, self.black_pawn, self.black_pawn],
        ["" for n in range(8)],
        ["" for n in range(8)],
        ["" for n in range(8)],
        ["" for n in range(8)],
        [self.white_pawn, self.white_pawn, self.white_pawn, self.white_pawn, self.white_pawn, self.white_pawn, self.white_pawn, self.white_pawn],
        [self.white_rook, self.white_knight, self.white_bishop, self.white_king, self.white_queen, self.white_bishop, self.white_knight, self.white_rook]
        ]

    def valid(self, p, n):

        x, y = p
        new_x, new_y = n
        piece = self.grid[y][x]
        if piece == self.white_pawn:
            step = 1
            if y == 6:
                step = 2
            possible_cords = [(x-1, y-1), (x+1, y-1)]
            for i in range(1, step+1):
                if y - i == new_y and x == new_x:
                    possible_cords.append((new_x, new_y))
            return n in possible_cords and not self.friendly(self.grid[new_y][new_x], piece)
        if piece == self.black_pawn:
            step = 1
            if y == 1:
                step = 2
            possible_cords = [(x+1, y+1), (x-1, y+1)]
            for i in range(1,step+1):
                if y+i == new_y and x == new_x:
                    possible_cords.append((new_x,new_y))
            return n in possible_cords and not self.friendly(self.grid[new_y][new_x], piece)
        if piece == self.black_knight or piece == self.white_knight:
            possible_cords = [(x+1, y+2), (x-1, y+2), (x+1, y-2), (x-1, y-2), (x+2, y+1), (x-2, y+1), (x+2, y-1), (x-2, y-1)]
            return n in possible_cords and not self.friendly(self.grid[new_y][new_x], piece)
        if piece == self.black_rook or piece == self.white_rook or piece == self.black_queen or piece == self.white_queen:
            # Tip for X just replace flip x and i
            possible_cords = []
            for i in list(range(y+1, 8)):
                if not self.friendly(grid.grid[i][x], piece):
                    possible_cords.append((x,i))
                else:
                    break
            for i in list(range(0, y))[::-1]:
                if not self.friendly(grid.grid[i][x], piece):
                    possible_cords.append((x,i))
                else:
                    break
            for i in list(range(0,x))[::-1]:
                if not self.friendly(grid.grid[i][x], piece):
                    possible_cords.append((x,i))
                else:
                    break
            for i in list(range(0,x))[::-1]:
                if not self.friendly(grid.grid[y][i], piece):
                    possible_cords.append((i,y))
                else:
                    break
            for i in list(range(x+1,8)):
                if not self.friendly(grid.grid[y][i], piece):
                    possible_cords.append((i,y))
                else:
                    break
            if(n in possible_cords): return n in possible_cords
        if piece == self.black_bishop or piece == self.white_bishop or piece == self.black_queen or piece == self.white_queen:
            deltay, deltax = ((new_y - y), (new_x - x))
            if deltax == 0:
                return False
            if abs(deltay/deltax) == 1:
                print("slope", deltay/deltax)
                # valid move, check for collision
                for y_relative in range(1, abs(deltax)+1):
                    dir = 1
                    if deltax < 0 and deltay < 0 and (deltay//deltax) == 1:
                        dir = -1

                    if deltay < 0 and deltax > 0 and (deltay//deltax) == -1:
                        dir = -1




                    x_relative = (deltay//deltax)*y_relative
                    if y+y_relative in list(range(0,8)) and x+x_relative in list(range(0,8)):
                        if self.friendly(grid.grid[y+y_relative*dir][x+x_relative*dir], piece):
                            return False
                return True
        return False

    def friendly(self, p, side):
        black_list = [self.black_rook, self.black_knight, self.black_bishop, self.black_king,self.black_queen , self.black_bishop, self.black_knight, self.black_rook,self.black_pawn]

        white_list = [self.white_pawn, self.white_rook, self.white_knight, self.white_bishop, self.white_king, self.white_queen, self.white_bishop, self.white_knight, self.white_rook]
        if p == "":
            return False
        if side in white_list:
            return p in white_list
        if side in black_list:
            return p in black_list



    def move(self, p, n):

        x, y = p
        new_x, new_y = n
        if self.valid(p, n) :
            piece = self.grid[y][x]
            self.grid[new_y][new_x] = piece
            self.grid[y][x] = ""
            return True
    def blit_alpha(self, target, source, location, opacity):
            x = location[0]
            y = location[1]
            temp = pygame.Surface((source.get_width(), source.get_height())).convert()
            temp.blit(target, (-x, -y))
            temp.blit(source, (0, 0))
            temp.set_alpha(opacity)
            target.blit(temp, location)

    def draw(self, surface):
        color_theme = [pygame.Color(139,69,19), pygame.Color(210,105,30)]
        col = width // 8
        row = height // 8
        for x in range(8):
            for y in range(8):
                rect = pygame.Rect((y*row, x*col), (col, row))
                pygame.draw.rect(surface, color_theme[(x + y) % 2], rect)
                if self.grid[x][y] != "":
                    curr_piece = self.grid[x][y]
                    self.blit_alpha(surface, curr_piece, (y*row + row/2 - 45/2, x*col + col/2 - 33/2), 128)




grid = Grid()










running = True
last_clicked = None
while running:
    pygame.display.flip()
    for x in range(8):
        for y in range(8):
            pygame.draw.line(screen, pygame.Color(0,0,0), (0, int(x*col)), (width, int(x*col)))
        pygame.draw.line(screen, pygame.Color(0,0,0), (int(x*col), 0), (int(x*col), height))
    grid.draw(screen)

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        if event.type == pygame.MOUSEBUTTONDOWN:
            if event.button == 1:
                x, y  = event.pos
                x = x // col
                y = y // col
                print(last_clicked == None and grid.grid[y][x] != "")
                print(grid.grid[x][y])
                if last_clicked == None and grid.grid[y][x] != "":
                    last_clicked = (x, y)
                    print(x, y, last_clicked)
                elif last_clicked != None:
                    print(x, y, last_clicked, grid.move(last_clicked, (x,y)))

                    last_clicked = None
                else:
                    last_clicked = None





"""
9/19/2020
HW:
Make all the images transparent
Also learn chess rules

"""

"""
10/3/20
Finish Rook.


"""

"""
10/15/20

Swap the queen and the king sprites

and learn chess

"""
