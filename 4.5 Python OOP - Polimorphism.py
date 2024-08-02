class Cat:

    def __init__(self):
        self.nama = "meong"
        self.tipe = "anggora"

    def forward(self):
        print("kucing berlari...")

class Bird:
    
    def __init__(self):
        self.nama = "erago"
        self.tipe = "elang"

    def forward(self):
        print("burung terbang...")


def melaju(objek):
    objek.forward()

meong = Cat(); erago = Bird()

melaju(meong)
melaju(erago)

