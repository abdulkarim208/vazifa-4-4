class Murabbiy:
    def __init__(self, ism, familiya, sport):
        self.ism = ism
        self.familiya = familiya
        self.sport_turi = sport

class Sportchi:
    def __init__(self, ism, familiya, yosh, murabbiy: Murabbiy):
        self.ism = ism
        self.familiya = familiya
        self.yosh = yosh
        self.murabbiy = murabbiy

    def malumot(self):
        return f"{self.ism} {self.familiya}, {self.yosh} yosh, murabbiyi: {self.murabbiy.ism} {self.murabbiy.familiya}"

    def saqlash(self):
        with open("sportchilar2.txt", "a",) as f:
            f.write(self.malumot() + "\n")

m1 = Murabbiy("Ali", "Valiyev", "Futbol")
m2 = Murabbiy("Hasan", "Karimov", "Boks")

s1 = Sportchi("Anvar", "Aliyev", 18, m1)
s2 = Sportchi("Sardor", "Valiyev", 20, m1)
s3 = Sportchi("Jasur", "Karimov", 19, m2)
s4 = Sportchi("Aziz", "Hasanov", 21, m2)

s1.saqlash()
s2.saqlash()
s3.saqlash()
s4.saqlash()
            
print("sportchilar malumoti saqlandi!")