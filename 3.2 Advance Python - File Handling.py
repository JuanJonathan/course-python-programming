
# Read

data = open('./data.txt', mode='r')
#print(data.read())

#data = open('./data.txt', mode='r', encoding='utf-8') #recommended
#print(data.read())

string = data.read()
string = string.replace('adalah', 'merupakan')
print(string)

# Append
data = open('./data.txt', mode='a', encoding='utf-8') #recommended
data.write("\nYuk belajar bahasa pemrograman python!")
data.write("\nAgar jago harus sering berlatih!")

data.close()


# Write
data = open('./data.txt', mode='w', encoding='utf-8') #recommended
data.write("\nYuk belajar bahasa pemrograman python!")
data.write("\nAgar jago harus sering berlatih!")

data.close()



# Better practice
try:
    f = open('./data.txt', mode='a', encoding='utf-8')
finally:
    f.close()




# Best practice
with open('./data.txt', mode='a', encoding='utf-8') as f:
    # bisa diisi kodingan apa saja
    pass

