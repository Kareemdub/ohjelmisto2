
class Koira:
    #konstruktori eli rakentaja
    def __init__(self, name): #
        print(f"uusi koiraolio {name}) luotu")
        self.name = name
    #funktio, mutta luokassa joten metodi eli luokan toiminto
    def hauku(self, toWhom):
        print(f"{self.name} Hauhau {toWhom}")


koira1 = Koira("Räkky")
koira2 = Koira("Täkky")

koira1.hauku("Matille") #matille parametri
koira2.hauku("Pekalle")


#koira1.name = "Räkky"
#koira2.name = "Täkky"
"""
print(koira1) #printtaa koira olion ja muistipaikan
print(koira1.name)
print(koira2.name)
print(koira3.name) #sama kuin koira1
"""

