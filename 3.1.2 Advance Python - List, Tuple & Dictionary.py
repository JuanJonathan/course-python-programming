# Tuple

tuple1 = ("apple", "banana", "watermelon")
tuple2 = (1, 3, 7, 9, 10) 
tuple3 = (True, False, True)
tuple4 = ("abc", 10, True, 40, "male")

fruit_tuple = ("apple", "banana", "watermelon", "orange", "mango")
fruit_tuple[1]
print(fruit_tuple[1:4])
print(fruit_tuple[-2:])


# IMMUTABLE
# fruit_tuple[1] = "apple"

# del fruit_tuple[1]

for fruit in fruit_tuple:
    print ("nama buah", fruit)



#DICTIONARY

fruit_dict = {'nama': 'pisang',
              'jenis': 'ambon',
              'kode': 891,
              'harga': 20000, }

print(fruit_dict)
print(fruit_dict['nama'])

fruit_dict['nama'] = 'jeruk'
print(fruit_dict)

for key, value in fruit_dict.items():
    print(key, value)

for key in fruit_dict.keys():
    print(key, fruit_dict[key])


fruit_dict = [{'nama': 'pisang',
              'jenis': 'ambon',
              'kode': 891,
              'harga': 20000}, 
              
              {'nama': 'pisang',
              'jenis': 'ambon',
              'kode': 891,
              'harga': 20000}]

print(fruit_dict)


# SET
A = { 1, 2, 3, 4, 5 }
B = { 4, 5, 6, 7, 8 }

# Union
print(A | B)

# Intersection
print(A & B)

# Difference
print(A - B)

# Symmetric Difference
print(A ^ B)