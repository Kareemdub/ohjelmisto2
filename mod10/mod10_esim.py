

class Koira:
    def __init__(self, nimi, syntymävuosi, haukahdus="vuhvuh"):
        self.nimi = nimi
        self.syntymävuosi = syntymävuosi
        self.haukahdus = haukahdus

    def hauku(self, kerrat):
        for i in range(kerrat):
            print(self.nimi + " haukkuu: " + self.haukahdus)
        return

class Hoitola:
    def __init__(self, nimi):
        self.nimi = nimi
        self.koirat =[]
    def lisaa_koira(self, koira):
        self.koirat.append(koira)
        print(f"{koira.nimi} on lisätty {self.nimi} hoitolaan.")
    def poista_koira(self, koira):
        self.koirat.remove(koira)
        print(f"{koira.nimi} on poistettu {self.nimi} hoitolasta. heihei!")
    def printtaa_koirat(self):
        for koira in self.koirat:
            print(f"hoitolassa {self.nimi} on {koira.nimi}")
    def tervehdi_koiria(self, kerrat):
        for koira in self.koirat:
            print(f"tervehditään {koira.nimi} ja koira haukahtaa {kerrat} kertaa!")
            koira.hauku(kerrat)

class Yritys:
    def __init__(self, nimi):
        self.nimi = nimi
        self.hoitolat = []
    def lisaa_hoitola(self, hoitola):
        self.hoitolat.append(hoitola)
        print(f"Musti ja mirri omistaa hoitolan {hoitola.nimi}")
    def anna_joululahja(self):
        for hoitola in self.hoitolat:
            for koira in hoitola.koirat:
                print(f"{koira.nimi} saa joululahjaksi luun!")
                koira.hauku(1)

    def tulosta_hoitolat(self):
        for Hoitola in self.hoitolat:
            print(f"Mustilla ja mirrillä on hoitola {Hoitola.nimi}")


yritys1 = Yritys("Musti ja mirri")
hoitola1 = Hoitola("Onnentassu")
hoitola2 = Hoitola("Pikkukoirat")

yritys1.lisaa_hoitola(hoitola1)
yritys1.lisaa_hoitola(hoitola2)


koira1 = Koira("Miau", 1998, "miau")
koira2 = Koira("Hauva", 2004, "hauhau")
koira3 = Koira("Vuffe", 2020, "räyh")
koira4 = Koira("Räkky", 2016, "haukku")
koira3.hauku(3)

hoitola1.lisaa_koira(koira1)
hoitola1.lisaa_koira(koira2)
hoitola2.lisaa_koira(koira3)
hoitola2.lisaa_koira(koira4)


hoitola1.poista_koira(koira1)

hoitola1.tervehdi_koiria(2)
hoitola2.tervehdi_koiria(3)
yritys1.anna_joululahja()

yritys1.tulosta_hoitolat()
