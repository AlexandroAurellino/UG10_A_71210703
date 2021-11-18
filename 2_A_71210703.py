print("############################")
print("Kalkulator Advance Sederhana")
print("############################")
print("1. Menghitung sisa hasil bagi")
print("2. Membulatkan ke bawah hasil pembagian")
print("3. Mencari akar kubik sebuah bilangan")

A = int(input("masukkan menu yang anda pilih: "))
if A == 1:
    x = int(input("Masukkan bilangan yang ingin dibagi: "))
    y = int(input("Masukkan bilangan pembagi: "))
    z = int(x%y)
    print("Sisa hasil bagi",float(x),"dibagi dengan",float(y),"adalah",float(z))
elif A==2:
    x = int(input("Masukkan bilangan yang ingin dibagi: "))
    y = int(input("Masukkan bilangan pembagi: "))
    z = int(round(x/y,1))
    print("Hasil pembagian",float(x),"dibagi dengan",float(y),"dibulatkan kebawah adalah",float(z))
elif A==3:
    x = int(input("Masukkan bilangan yang ingin dicari akar kubiknya "))
    y = int(x**(1/3))
    print("Akar kubik dari",float(x),"adalah",float(y))
else:
    print("Menu yang anda pilih tidak tersedia")
