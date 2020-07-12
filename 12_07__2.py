import datetime
#text=" Das ist hier ein text"
# hier öffne ich eine datei und schreibe rein
#datei = open("text1.txt", 'w')
#datei.write(text)
#datei.close()


# ein kleines Programm (virtuelle geldbörse) welches unsere eingaben speichert
# eingabe : Geldanzahl
datum = datetime.datetime.now()

datei = open("geld.txt", 'a+')
eingabe = ""
while eingabe != "ende":
    eingabe = input()
    if eingabe != "ende":
        datei.write(str(datum) + ": " + eingabe + "\n")
datei.close()