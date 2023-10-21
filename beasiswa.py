nilai = int(input("Masukkan Nilai Anda: "))
keuangan = int(input("Masukkan Keuangan Keluarga Anda: "))

if nilai > 90 and keuangan < 2000000:
    print("Selamat, Anda mendapat beasiswa!")
elif 80 < nilai <= 90 and keuangan < 4000000:
    print("Selamat, Anda Mendapat beasiswa Parsial!!!")
else:
    print("Maaf, anda belum bisa apply beasiswa")