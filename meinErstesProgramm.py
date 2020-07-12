# Das ist hier ein Kommentar
# Kommetare sind sehr nützlich,
# weil man so seine Gedanken beim Programmieren aufschreiben kann

#fdgedrfgd fg dfgprint("Hello World")

# Variable mit Namen Zahl bekommt als Wert 5
zahl = 5

#print(zahl)

# Datentypen
# Zahlen : 6, 1, 1.1,
# Text/String "das ist ein Text"
# Buchstaben/Characters  a b A ä

a = 2
#print(a)

a = "Text"
#print(a)

zahl1 = 293821
zahl2 = 272761

# Operatoren * , + , / , % ,
#print(zahl1 * zahl2)

# Definition einer Funktion
def Multiplikation(zahl1, zahl2):
    print(zahl1 * zahl2)

# So rufe ich die Funktion auf
#
#--_--
#
Multiplikation
'''
Hier andere ART von Kommentaren
die über mehrere Zeilen gehen können
'''
#Multiplikation(12, 4)
#Multiplikation
def BerechneFlaecheQuadrat(Seitenlaenge):
    flaeche = Seitenlaenge * Seitenlaenge
    return flaeche

# Zuweisung einer Variable den Wert einer Funktion


def BerechneFlaecheRechteck(a, b):
    return a * b

z = BerechneFlaecheRechteck(7, 3)
#print("Rechtecksfläche:" , z, "Quadratfläche:", a)




### 2te Stunde

# leere Methode
def leer(t = "b"):
    print(t)

#leer("leere Methode")
#leer()

def FlaecheDreieck(a, h):
    print(1/2 * a * h)

f = BerechneFlaecheQuadrat(2)
#print(f)
#FlaecheDreieck(2, 2)

import math
import random

def FlaecheKreis(r):
    print(math.pi)
    print(math.pi * r * r)




















for variable in range(0, 5):
    zufallszahl = random.randint(1, 6)
    print(variable , " Zufallszahl=", zufallszahl)
    # Bedingung if = wenn ; else = ansonsten
    if zufallszahl > 3:
        print("wir haben gewonnen")
    else:
        print("wir haben verloren")

    # Vergleich auf ist gleich : ==



#FlaecheKreis(random.randint(25, 75))









