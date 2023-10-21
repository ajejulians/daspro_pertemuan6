user = (input("Masukkan Angka: "))

if user.isdigit():
    angka = int(user)
    if angka % 2 == 0:
        print(f"{angka} adalah Genap")
    else:
        print(f"{angka} adalah Ganjil")
else:
    print("Silahkan Masukkan Angka Lagi")
