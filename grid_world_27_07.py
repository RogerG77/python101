import random


ZELL_GROESSE = 10
# Spielfläche = grid
ROWS = 80
COLS = 50

HEIGHT =  (ROWS * ZELL_GROESSE)
WIDTH = (COLS * ZELL_GROESSE)

SCHWARZ = (0, 0, 0)
GREEN = (0, 255, 0)
BLUE = (0, 0, 255)

def baue_grid():
    grid = []
    for column_num in range(0, COLS):
        row = []
        for row_num in range(0, ROWS):
            row.append(row_num)
        grid.append(row)
    return grid

def baue_zufallswelt(welt):
    for row in range(len(welt)):
        for column in range(len(welt[0])):
            zufall = random.randint(0, 10)
            if zufall == 0:
                welt[row][column] = 1
            else:
                welt[row][column] = 0

def zeichne_zelle(row, column):
    x_coord = ZELL_GROESSE * column
    y_coord = ZELL_GROESSE * row
    rechteck = Rect((x_coord, y_coord), (ZELL_GROESSE, ZELL_GROESSE))
    screen.draw.filled_rect(rechteck, GREEN)
    return

def draw():
    screen.fill(SCHWARZ)
    for row in range(ROWS):
        for col in range(COLS):
            if world[col][row] == 1:
                zeichne_zelle(row, col)


world = baue_grid()
baue_zufallswelt(world)
print(world)