import random

computer_zahl = random.randint(1, 100)
eingabe = -1
versuche = 0
while computer_zahl != eingabe:
    # input erwartet eine Eingabe auf der Tastatur
    print("Eingabe:",  flush=True)
    eingabe = input()
    # hier wird die Tastatureingabe der variable input zugewiesen
    print("Eingabe:" , eingabe)

    # Spiel : Computer soll eine Zahl erfinden , die wir erraten müssen
    # Programm soll ausgeben wenn wir falsch oder richtig liegen

    eingabe = int(eingabe)

    # Vergleich auf Gleichheit immer mit ==
    #print(type(computer_zahl))
    #print(type(eingabe))
    if computer_zahl == eingabe:
        print("Richtig erraten")
    else:
        print("falsche Eingabe")
        if computer_zahl < eingabe:
            print("Eingabe ist zu gross")
        else:
            print("Eingabe ist zu klein")

    versuche = versuche + 1
print("Fertig mit ", versuche, " Versuchen")