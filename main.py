class Murabbiy:
    def __init__(self, ism, sport):
        self.ism = ism
        self.sport = sport

    def malumot(self):
        return f"{self.ism} - {self.sport}"

class Sportchi:
    def __init__(self, ism, yosh, murabbiy: Murabbiy):
        self.ism = ism
        self.yosh = yosh
        self.murabbiy = murabbiy

    def malumot(self):
        return f"{self.ism} ({self.yosh}) - murabbiy: {self.murabbiy.ism} ({self.murabbiy.sport})"

    def saqlash(self):
        with open("sportchilar.txt", "a") as f:
            f.write(self.malumot())
            print("malumot saqlandi!")

m = Murabbiy("Pep Guardiola", "Futbol")
s = Sportchi("Mbappe", "25 yosh", m)
print(s.malumot())
s.saqlash()