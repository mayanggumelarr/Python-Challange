to_do = []

# fungsi tampilkan menu
def menu():
    print("\n================== TO-DO LIST==================")
    print("1. Add Tugas")
    print("2. Show All Tugas")
    print("3. Delete Tugas")
    print("4. Keluar")

#fungsi tambah tugas
def  tambah_tugas():
    tgs = input("Masukkan tugas kamu: ")
    to_do.append(tgs)
    print('Tugas added!')
    
# Fungsi melihat semua tugas
def show_all():
    if not to_do:
        print('Null')
    else:
        print("\nDaftar Tugas:")
        for i, tgs in enumerate(to_do, start=1):
            print(f"{i}. {tgs}")

#Fungsi hapus tugas
def hapus():
    show_all()
    if to_do:
        try:
            number = int(input('nomor tugas yang ingin dihapus: '))
            if 1 <= number <= len(to_do):
                tugas_del = to_do.pop(number-1)
                print(f"Tugas {tugas_del} berhasil terhapus!")
            else:
                print("Nomor tidak valid!")
        except ValueError:
            print("Masukkan angka yang benar sayang!")
            
# Main Program
while True:
    menu()
    pilihan = input("Pilih menu (1-4): ")

    if pilihan == "1":
        tambah_tugas()
    elif pilihan == "2":
        show_all()
    elif pilihan == "3":
        hapus()
    elif pilihan == "4":
        print("Terima kasih! Sampai jumpa.")
        break
    else:
        print("Pilihan tidak valid. Coba lagi.")
                