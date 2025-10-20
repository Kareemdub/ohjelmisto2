
class Koira:
    count = 0
    #konstruktori eli rakentaja
    def __init__(self, name, weight): #
        print(f"uusi koiraolio ({name}) luotu")
        self.name = name
        self.weight = weight
        Koira.count = Koira.count + 1
    #funktio, mutta luokassa joten metodi eli luokan toiminto
    def hauku(self, toWhom, times = 1):
        print(f"{self.name} Haukkuu {toWhom}")
        for i in range(times):
            if self.weight < 10:
               print("Wufwuf")
            else:
                print("Hauhau")

koira1 = Koira("Räkky", 2)
koira2 = Koira("Täkky", 22)
koira3 = koira1
koira4 = Koira(input("Anna koiralle nimi:"), 9)

koira1.hauku("Matille", 2) #matille parametri
koira2.hauku("Pekalle")
koira4.hauku("Jarille", 1)

koira1.name = "Wuffe"
koira1.hauku("Matille")
#koira1.name = "Räkky"
#koira2.name = "Täkky"
print(f"Koiraolioita on luotu {Koira.count}")
"""
print(koira1) #printtaa koira olion ja muistipaikan
print(koira1.name)
print(koira2.name)
print(koira3.name) #sama kuin koira1
"""

