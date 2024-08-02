
angka = 10

angka = 100
print(angka)

email = "juan.jonathan.n@gmail.com"
print(email)

angka1, angka2, email1 = 10, 0.1, "juan.jonathan.n@gmail.com"
print(angka1)
print(angka2)
print(email1)

angka3 = angka4 = angka5 = 1000
print(angka3)
print(angka4)
print(angka5)

# CONSTANTA
PI = 3.14
GRAVITY = 9.8

# Naming
nama_variable = "Indonesia AI 1"
NAMA_VARIABLE = "Indonesia AI 2"
print(nama_variable)
print(NAMA_VARIABLE)

# Dilarang: !, @, #, $, %, ^, &, *, (, )

# Literals
nomor_biner = 0b1010
nomor_desimal = 100
nomor_float = 1.5e2

print(nomor_float)

a = 5
print(type(a))
b = 2.0
print(type(b))
c = 4/5
print(type(c))
c = a + b
print(type(c))

print(c)

c = 8/5
c = c.__ceil__()
print(c)

# String
s = "Ini adalah string single-line"
print(type(s))

s = '''Ini adalah string
namun bukan single-line melainkan multi-line
'''
print(type(s))

s = "Ini adalah string single-line"
s = s.lower()
print(s)

s = "Ini adalah string single-line"
s = s.upper()
print(s)

s = s.replace('ADALAH', 'MERUPAKAN')
print(s)

nama = "Juan"
s = f"Nama saya adalah {nama}"
print(s)

# Boolean
b = True
print(type(b))

print(type(b == 1))

# Logika 
# True and True = True
# False and False = False
# False and True = False
# False or True = True

print(True or False)
print(True and False)

# List, Tuple & Dictionary
l = [1, 2.2, "python"]
print(l)
print(type(l))

t = (1, 2.2, "python")
print(t)
print(type(t))

#Dictionary
d = {'key1': 'value1', 'key2': 'value2'}
print(d)
print(type(d))
