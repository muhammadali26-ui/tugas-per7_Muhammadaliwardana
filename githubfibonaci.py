# Fungsi pangkat (rekursif)
def pangkat(a, b):
    if b == 0:
        return 1
    else:
        return a * pangkat(a, b - 1)

# Fungsi deret
def deret(n):
    hasil = 0
    a, b = 1, 1   # awal pembilang & penyebut
    tanda = 1     # untuk + dan -

    for i in range(n):
        hasil += tanda * (a / b)

        # update pola angka
        a, b = b, a + b   # mirip Fibonacci
        tanda *= -1       # ganti tanda

    return hasil


# Program utama
while True:
    print("\n=== MENU ===")
    print("1. A pangkat B")
    print("2. Hitung deret")
    print("0. Keluar")

    pilihan = input("Masukkan pilihan: ")

    if pilihan == '1':
        try:
            a = int(input("Masukkan bilangan: "))
            b = int(input("Masukkan pangkat: "))
            print("Hasil:", pangkat(a, b))
        except:
            print("Input harus angka!")

    elif pilihan == '2':
        try:
            n = int(input("Masukkan jumlah N: "))
            print("Hasil deret:", deret(n))
        except:
            print("Input harus angka!")

    elif pilihan == '0':
        print("Program selesai.")
        break

    else:
        print("Pilihan tidak tersedia!")