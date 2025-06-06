'''INI ADALAH APLIKASI KALKULATOR SEDERHANA UNTUK PENJUMLAHAN, PENGURANGAN, PERKALIAN, DAN PEMBAGIAN'''

def jumlah (a,b):
    return a + b

def kurang (a,b):
    return a - b

def kali (a,b):
    return a * b

def bagi (a,b):
    return a / b

def menu():
    print("=== MENU KALKULATOR SEDERHANA ===")
    print("1. Penjumlahan")
    print("2. Pengurangan")
    print("3. Perkalian")
    print("4. Pembagian")

    pil = input("Pilih operasi (1/2/3/4): ")

    if pil in ['1', '2', '3', '4']:
        try:
            angka_1 = float(input("Masukkan angka pertama: "))
            angka_2 = float(input("Masukkan angka kedua: "))

            if pil == '1':
                hasil = jumlah(angka_1,angka_2)
                print(f"Hasil penjumlahan: {hasil}")
            if pil == '2':
                hasil = kurang(angka_1,angka_2)
                print(f"Hasil pengurangan: {hasil}")
            if pil == '3':
                hasil = kali(angka_1,angka_2)
                print(f"Hasil perkalian: {hasil}")
            if pil == '4':
                hasil = bagi(angka_1,angka_2)
                print(f"Hasil pembagian: {hasil}")
        except ValueError:
            print("Input angka BRO!")
    else:
        print("masukkan angka yang benar!")

menu()