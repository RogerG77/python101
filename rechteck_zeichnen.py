HEIGHT =  300
WIDTH = 400
BLACK = (0, 0, 0)
GREEN = (0, 255, 0)
BLUE = (0, 0, 255)

def zeichne_rechteck():
    pos_X = 50
    pox_Y = 100
    breite = 20
    hoehe = 40
    rechteck = Rect((pos_X, pox_Y), (breite, hoehe))
    screen.draw.filled_rect(rechteck, GREEN)
    return

def zeichne_kreis():
    pos_X = 80
    pos_Y = 110
    radius = 10
    screen.draw.filled_circle((pos_X, pos_Y), radius, BLUE)

def draw():
    screen.fill(BLACK)
    zeichne_rechteck()
    zeichne_kreis()