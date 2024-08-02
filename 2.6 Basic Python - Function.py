# funtion non parameter
def halo_dunia():
    var = 'halo python, halo dunia!'
    print(var)

halo_dunia()

# funtion parameter
def selamat_datang(nama):
    var = f'halo {nama}, welcome!'
    print(var)

selamat_datang('nurul')

def selamat_datang(nama, asal):
    var = f'halo {nama} dari {asal}, welcome!'
    print(var)

selamat_datang('nurul', 'bekasi')

def selamat_datang(*daftar_nama):

    var = 'halo '
    for nama in daftar_nama:
        var += nama +', '
    
    var += 'welcome!'
    print(var)

selamat_datang('nurul', 'siska', 'lukman', 'rowi')


# Anonim 
double = lambda x: x * 2

print(double(5))


# Bonus : Docstring

def selamat_datang(nama):
    '''
    ini adalah fungsi untuk menyapa
    nama yang telah disebutkan
    '''
    var = f'halo {nama}, welcome!'
    print(var)

selamat_datang('nurul')
print(selamat_datang.__doc__)


# Bonus : Scope & Return

a = 2
def operasi(a,b,c):

    op1 = a + b
    op2 = op1 // c

    print('a di dalam function', a)

    return op2

hasil = operasi(a=10, b=5, c=3)
print(hasil)

print('a di luar function', a)
