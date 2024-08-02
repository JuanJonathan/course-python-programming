
class Mobil:

    def __init__(self, plat):

        self.__plat = plat
        self.__tipe = "avanza"
        self.__bensin = 40 #liter

    # getter
    def lihatMaksimumBensin(self):
        print(f"Maksimum bensin yaitu: {self.__bensin} liter")

    # setter
    def aturMaksimumBensin(self, bensin):
        self.__bensin = bensin



avanza = Mobil(plat="B 7185 XC")

#print(avanza.plat)

#print(avanza.tipe)

#print(avanza.bensin)

avanza.__bensin = 30

print(avanza.__bensin)


avanza.lihatMaksimumBensin()
avanza.aturMaksimumBensin(100)
avanza.lihatMaksimumBensin()