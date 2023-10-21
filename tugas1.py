nilai = int(input("Masukkan Nilai Anda: "))

if nilai >= 90:
    predikat_nilai = "A"
elif nilai >= 80:
    predikat_nilai = "B"
elif nilai >= 70:
    predikat_nilai = "C"
else:
    predikat_nilai = "D"

print(f"Predikat Nilai Anda: {predikat_nilai}")
