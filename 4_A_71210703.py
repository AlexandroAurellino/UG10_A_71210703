A = input("Masukkan artikel yang ingin dipindai: ")
B = input("Masukkan nama klub favorit anda: ")
C = input("Masukkan skor yang ingin dicari: ")
if B in A and C in A:
    print("Hasil pencarian ditemukan")
elif B in A:
    print("Hanya",B,"yang ditemukan pada artikel ini")
elif C in A:
    print("Hanya skor",C,"yang ditemukan pada artikel ini")
else:
    print("Hasil pencarian",B,"dan",C,"tidak ditemukan")
