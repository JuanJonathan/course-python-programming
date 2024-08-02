# Syntax Error

fruit_list = ["apple", "banana", "watermelon"]

for fruit in fruit_list:
    print(fruit)


# Logical Error
nilai = 10
pembagi = 0
#hasil = nilai/pembagi

print(dir(locals()['__builtins__']))


try:
    nilai = 10
    pembagi = 0
    hasil = nilai/pembagi
except:
    print("Oops! Terjadi error.")

try:
    nilai = 10
    pembagi = 0
    hasil = nilai/pembagi
except Exception as e:
    print("Oops! Terjadi ", e.__class__, ".")

try:
    nilai = 10
    pembagi = 0
    hasil = nilai/pembagi
except ZeroDivisionError:
    print("Oops! Terjadi ZeroDivisionError.")
except ValueError:
    print("Oops! Terjadi ValueError.")
except:
    print("Oops! terjadi error yang tidak dikenali.")


print("instruksi setelahnya")


class ValueTooSmallError(Exception):
    pass

class ValueTooLargeError(Exception):
    pass


number = 10

while True:

    try:
        i_num = int(input("masukan angka: "))

        if i_num < number:
            raise ValueTooSmallError
        elif i_num > number:
            raise ValueTooLargeError
        break

    except ValueTooSmallError:
        print("angka yang kamu tebak terlalu kecil, coba lagi!")
        print()
    except ValueTooLargeError:
        print("angka yang kamu tebak terlalu kecil, coba lagi!")
        print()

print("Betul! kamu berhasil menebak angka dengan tepat.")
