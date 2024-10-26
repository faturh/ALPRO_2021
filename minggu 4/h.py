def welcomeScreen() :
        print(40*"=")
        print("SELAMAT DATANG SILAHKAN PESAN".center(40))
        print(40*"=")
def displayMenu():
    print("")
    print(40*"=")
    print("SILAHKAN PILIH MENU")
    print(40*"=")
    print("1. Lele Goreng | Rp. 15.000,00")
    print("2. Tahu Goreng | Rp. 1.000,00")
    print("3. Ayam Goreng | Rp. 17.000,00")
    print("4. Bebek Goreng | Rp. 25.000,00")
    print("5. Nasi | Rp. 5.000,00")
    print("0. Keluar\n")
def entryPilihanMenu():
        list_makanan =["lele goreng","ayam goreng","nasi","Tahu goreng","Bebek goreng"]
        list_harga = [15000,17000,5000,1000,25000]
        total = 0
        syarat = True
        gagal = 0
        pesanan = {}
        while syarat :
                nomor_meja = input("Masukan nomor meja : ")
                displayMenu()
                pesanan = int(input("Masukan pesanan anda : "))
                jumlah_pesanan = int(input("Masukan jumlah pesanan anda : "))
                if pesanan == 0 :
                     syarat =False
                elif pesanan in list_makanan :
                       total = int((jumlah_pesanan)*list_harga)
                       total_harga += total
                       menu = list_makanan
                elif menu in list_makanan :
                       list_makanan[menu]["jumlah"] +=int(jumlah_pesanan)
                       list_makanan[menu]["harga"] += total
                else :
                       list_makanan[menu] = {
                              "jumlah": int(jumlah_pesanan),
                              "harga": total
                       }
        else:
               print("menu tidak tersedia")
               gagal += 1
               if gagal >= 3:
                      print("sudah 3x pecobaan anda akan keluar")
                      syarat = False
               print("pesanan gagal silahkan coba lagi")
        if total_harga (0):
               print("\npesanan anda: ")
               for menu, data_pesanan in pesanan.items() :
                    print(f"{nomor_meja} memesan: \n{menu} sebanyak {data_pesanan['jumlah']} x {data_pesanan['harga'] // data_pesanan['jumlah']} = Rp.{data_pesanan['harga']},00\n")
                    print("\n jumlah yang harus di bayar: Rp. {},00".format(total_harga))
                    
                    f = open("bon.txt","w")
                    f.write("Nomor meja: {}\n".format(nomor_meja))
                    f.write("detail:\n")
                    for menu,data_pesanan in pesanan.items():
                           f.write(f"{nomor_meja} memesan {menu} sebanyak {data_pesanan['jumlah']} buah x {data_pesanan['harga'] // data_pesanan['jumlah']} = Rp.{data_pesanan['harga']},00\n")
welcomeScreen()
entryPilihanMenu()                
          
                       

