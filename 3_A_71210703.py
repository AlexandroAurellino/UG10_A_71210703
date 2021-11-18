A = input("Mendatar/Menurun?: ")
if A == "Mendatar":
    x = int(input("Masukkan kolom: "))
    print("#"*x)
elif A == "Menurun":
    x = int(input("Masukkan baris: "))
    print("*\n"*x)
else:
    print("Print tidak dikenali")