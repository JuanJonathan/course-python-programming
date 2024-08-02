jumlah_penumpang = 3

if jumlah_penumpang > 10:
    print("mobil berjalan...")

if jumlah_penumpang < 10:
    print("mobil menunggu penumpang lain...")

    print("di luar condition")

score = 78

if score > 75:
    print('lulus')
elif score < 10:
    print('tidak lulus')

if score >= 85:
    print('predikat A/memuaskan')
elif score >= 75:
    print('predikat B/bagus')
else:
    print('tidak lulus')


kelas = 3 

if kelas > 1:
    if score >= 85:
        print('predikat A/memuaskan')
    elif score >= 75:
        print('predikat B/bagus')
    else:
        print('tidak lulus')

else:
    if score >= 80:
        print('predikat A/bagus')
    else:
        print('tidak lulus')


num = float(input("masukan angka: "))

if num >= 0:
    if num == 0:
        print("nol")
    else:
        print("angka positif")
        
        