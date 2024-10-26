def welcomeScreen():
    print("================================")
    print("SELAMAT DATANG DI APLIKASI WARUNG LELE")
    print("================================")

def displayPilihanMenu():
    print("\n1. Lele Goreng | Rp. 11.000,00")
    print("2. Tahu Goreng | Rp. 3.000,00")
    print("3. Ayam Goreng | Rp. 20.000,00")
    print("4. Bebek Goreng | Rp. 25.000,00")
    print("5. Nasi | Rp. 5.000,00")
    print("0. Selesai\n")

def entryPilihanMenu():
    syarat = True
    gagal = 0
    total_bayar = 0
    pesanan = {}

    nama_pembeli = input("Masukan nama: ")
    while syarat:
        displayPilihanMenu()

        pilih_menu = input("Silahkan pilih menu yang tersedia: ")

        if pilih_menu == "0":
            syarat = False
        else:
            jumlah_pilih = input("Silahkan masukkan jumlahnya: ")
            if pilih_menu in ["1", "2", "3", "4","5"]:
                harga_satuan = {
                    "1": 11000,
                    "2": 3000,
                    "3": 20000,
                    "4": 25000,
                    "5": 5000
                }[pilih_menu]
                harga_total = int(jumlah_pilih) * harga_satuan
                total_bayar += harga_total
                nama_menu = {
                    "1": "Lele Goreng",
                    "2": "Tahu Goreng",
                    "3": "Ayam Goreng",
                    "4": "Bebek Goreng",
                    "5": "Nasi"
                }[pilih_menu]
                if nama_menu in pesanan:
                    pesanan[nama_menu]["jumlah"] += int(jumlah_pilih)
                    pesanan[nama_menu]["harga"] += harga_total
                else:
                    pesanan[nama_menu] = {
                        "jumlah": int(jumlah_pilih),
                        "harga": harga_total
                    }
            else:
                print("Menu yang dipilih tidak tersedia")
                gagal += 1
                if gagal >= 3:
                    print("Anda telah salah memasukkan pilihan menu sebanyak 3 kali, aplikasi akan keluar")
                    syarat = False

                print(f"Pesanan gagal, silakan coba lagi.")

    if total_bayar > 0:
        print("\nPesanan Anda:")
        for menu, data_pesanan in pesanan.items():
            print(f"{nama_pembeli} memesan: \n{menu} sebanyak {data_pesanan['jumlah']} x {data_pesanan['harga'] // data_pesanan['jumlah']} = Rp. {data_pesanan['harga']},00") 

        print("\nJumlah yang harus dibayar: Rp. {},00".format(total_bayar))

    # menulis pesanan ke dalam file
    f = open("struk.txt", "a")
    f.write("Nama Pembeli: {}\n".format(nama_pembeli))
    f.write("Detail:\n")
    for menu, data_pesanan in pesanan.items():
        f.write(f"{nama_pembeli} memesan {menu} sebanyak {data_pesanan['jumlah']} buah x {data_pesanan['harga'] // data_pesanan['jumlah']} = Rp. {data_pesanan['harga']},00\n") 


welcomeScreen()
pesanan = entryPilihanMenu()