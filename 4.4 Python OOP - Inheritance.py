# parent class

class Animal:

    def __init__(self):
        self.tipe = "mamalia"
        self.kecepatan = "lambat"

    def grow(self):
        print("mamalia ini bertumbuh...")


# child class

class Cat(Animal):

    def __init__(self, nama, tipe):

        super().__init__()

        self.nama = nama
        self.tipe = tipe

    def run(self):
        print(f"kucing {self.tipe} ini berlari...")

class Dog(Animal):
    pass

kinako = Cat(nama="kinako", tipe="anggora")
minto = Cat(nama="minto", tipe="persia")

print(kinako.kecepatan)
print(kinako.tipe)


kinako.run()
minto.run()

kinako.grow()
minto.grow()

