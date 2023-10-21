total_belanja = float(input("Masukkan Jumlah Belanja: "))

if total_belanja > 500000:
    print("selamat anda mendapatkan diskon 10%")
    harga_diskon = (10 / 100) * total_belanja 
    harga_dibayar = total_belanja - harga_diskon
    print(f"Total yang harus di bayar adalah {harga_dibayar}")
else:
    print("Pelanggan tidak mendapat dikson")
