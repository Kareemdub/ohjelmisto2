class Julkaisu:
    def __init__(self, name):
        self.name = name

        pass

class Kirja(Julkaisu):
    def __init__(self, name, writer, pages):
        super().__init__(name)
        self.writer = writer
        self.pages = pages


    def kirja_tulosta_tiedot(self):
        print(self.name, self.writer, self.pages)

class Lehti(Julkaisu):
    def __init__(self, name, reporter):
        super().__init__(name)
        self.reporter = reporter

    def lehti_tulosta_tiedot(self):
        print(self.name, self.reporter)


Julkaisu1 = Lehti("Aku Ankka", 'Aki Hyyppä')
Julkaisu2 = Kirja("Hytti", 'Rosa Liksom', '200')


Julkaisu1.lehti_tulosta_tiedot()
Julkaisu2.kirja_tulosta_tiedot()