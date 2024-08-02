count = 0

while (count < 9):
    print("Nilai count:", count)
    count = count + 1

print("selamat tinggal!")

list_angka = [1,2,3,4,5,6,7,8]

for x in list_angka:
    print("instruksi berjalan...")
    print(x)

print(range(10))

print(list(range(10)))

list_range = list(range(1, 2000, 5))
print(list_range)

for x in list(range(1, 11)):
    print(x)


i = 90

while (i < 100):

    j = 2
    print((i/j))
    while(j <= (i/j)):
        print('loop dalam loop!')
        j = j + 1
        i = i + 1
print('selamat tinggal')

# break & continue
for val in "string":

    if val == "i":
        continue

    print(val)

print('loop telah berakhir.')


# Bonus : For Else

daftar_murid = ['angga', 'mardadi', 'rowi']

nama_murid = 'angga'

for nama in daftar_murid:

    if nama == nama_murid:
        print(nama)
        break
else:
    print('nama murid tidak ditemukan') 


# Bonus : Pass

for nama in daftar_murid:
    pass
if daftar_murid == 0:
    pass
else:
    pass
