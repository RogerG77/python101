#
var = 1
#print("ID:", id(var))
def eineMethode():
    global var
    print("ID in methode:", id(var))
    print("in der Methode:" , var )

#eineMethode()
#print("ausserhalb:" , var)


x = 10
#print(x)
#print(type(x))

x = 1.1
#print(x)
#print(type(x))

x = "bla bla"
#print(x)
#print(type(x))


#liste = [0, 1, 2, 4]
#print("liste: ", liste)
#print(type(liste))
'''
for i in range(0, 10):
    print(i * i)
'''


Liste = [1, 3, 5, 7, 9]
print(Liste)
for Elemente in Liste:
    if type(Elemente) == str:
        print(Elemente, type(Elemente))




Liste = [1, 3, 5, 7, 9]
'''
for Elemente in Liste:
    print(Elemente)
print('\n')
for i in range(0, 4):
    print(Liste[i] + Liste[i+1])
'''
Liste2 = [1, 2, ["erstes", "zweites"], 3]
#print(Liste2[2][1])
innerListe = Liste2[2]
for Element in innerListe:
    print(Element)


Liste3 = ["a", "ac", "ab", "c"]
Liste3 = sorted(Liste3)
print(Liste3)

l2 = Liste.pop()
print(l2)

Liste3.append(10)
print(Liste3)