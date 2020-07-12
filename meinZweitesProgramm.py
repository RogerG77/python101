a = 2
# print gibt output in console aus
#print("Summe a + a=" , a + a, ";")

a = "2"
#print(a + a + " bla bla")

# Definition einer Funktion
def Multiplikation(a = 0, b = 0):
    return a * b

m = Multiplikation(2, 3)
#print(m)

import random

anfang = 0
ende = 10
for i in range(anfang, ende):
    Zufallszahl = random.randint(1, 100)
    #print(i, "Zufallszahl:", Zufallszahl)

y = 0
while y < 10:
    print(y)
    y = y + 1
