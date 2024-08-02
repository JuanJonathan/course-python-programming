
class Cat:
    '''
    ini adalah class untuk membuat objek kucing
    melalui kelas ini kita bisa mendefinisikan nama dan juga tipe dari kucing yang dibuat
    '''

    spesies = "kucing"

    def __init__(self, nama, tipe):
        self.nama = nama
        self.tipe = tipe
        
    def run(self, speed):
        print(f"kucing {self.nama} berlari dengan {speed}...")

    def play(self):
        print(f"kucing {self.nama} bermain dengan kucing lainnya...")

    def eat(self):
        pass

# Membuat objek
kinako = Cat(nama="kinako", tipe="anggora")
minto = Cat(nama="minto", tipe="persia")

print(f"kinako adalah seekor {kinako.__class__.spesies}")
print(f"{kinako.nama} merupakan kucing jenis {kinako.tipe}")


print(kinako)
print(minto)

kinako.run('cepat')
kinako.play()

print(kinako.__doc__)




class Employee():
    '''
    ini adalah class untuk memanipulasi data employee
    melalui kelas ini kita bisa memanipulasi data yang ada seperti baca, hapus dan tambah
    '''

    def __init__(self, lokasi_file):
        self.data_employee = open(f'{lokasi_file}', mode='r', encoding='utf-8')
        self.data_per_sesi = 10

    def baca_data(self):
        
        self.data_employee = self.data_employee[:self.data_per_sesi]
        return self.data_employee

    def hapus_data(self, baris, kolom):
        
        del self.data_employee[baris][kolom]

    def tambah_data(self, data_baru):
        nama, gaji, posisi, jabatan, domisili = data_baru
        self.data_employee.append([nama, gaji, posisi, jabatan, domisili])


# Membuat objek
it = Employee(lokasi_file='./karyawan_IT.xls')
marketing = Employee(lokasi_file='./karyawan_marketing.xls')
product = Employee(lokasi_file='./karyawan_product.xls')


# Abstract object
class RamdomForest():
    pass



