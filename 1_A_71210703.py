A = float(input("Masukkan nilai rata-rata UG anda: "))
B = float(input("Masukkan nilai TTS anda: "))
C = float(input("Masukkan nilai TAS anda: "))
print("=========================")
A1 = A*70/100
B1 = B*15/100
C1 = C*15/100
Hasil = float(A1+B1+C1)
print("Nilai anda: ", Hasil)
if Hasil >= 85:
    print("Nilai huruf anda: A")
elif Hasil >= 80:
    print("Nilai huruf anda: A-")
elif Hasil >= 75:
    print("Nilai huruf anda: B+")
elif Hasil >= 70:
    print("Nilai huruf anda: B")
elif Hasil >= 65:
    print("Nilai huruf anda: B-")
elif Hasil >= 60:
    print("Nilai huruf anda: C+")
elif Hasil >= 55:
    print("Nilai huruf anda: C")
elif Hasil >= 45:
    print("Nilai huruf anda: D")
else:
    print("Nilai huruf anda: E")
