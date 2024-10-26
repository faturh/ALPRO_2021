list_makanan =["lele goreng","ayam goreng","nasi","Tahu goreng","Bebek goreng"]
list_harga = [15000,17000,5000,1000,25000]
total = 0
import os
def welcomeScreen() :
        os.system('cls')
        print(40*"=")
        print("SELAMAT DATANG SILAHKAN PESAN".center(40))
        print(40*"=")
def displayMenu():
    print("\n1. Lele Goreng | Rp. 15.000,00")
    print("2. Tahu Goreng | Rp. 1.000,00")
    print("3. Ayam Goreng | Rp. 17.000,00")
    print("4. Bebek Goreng | Rp. 25.000,00")
    print("5. Nasi | Rp. 5.000,00")
    print("0. Keluar\n")
def entryPilihanMenu():
        displayMenu()
        nomor_meja = input("Masukan nomor meja : ")
        pesanan = input("Masukan pesanan anda : ")
        jumlah_pesanan = int(input("Masukan jumlah pesanan anda : "))
        warunglele(nomor_meja,pesanan,jumlah_pesanan)
def warunglele (pesanan,jumlah_pesanan):
          if pesanan == list_makanan[0] :
                  total += jumlah_pesanan*list_harga[0]
          elif pesanan == list_makanan[1] :
                  total += jumlah_pesanan*list_harga[1]
          elif pesanan == list_makanan[2] :
                  total += jumlah_pesanan*list_harga[2]
          print (f"total harganya {warunglele(jumlah_pesanan+total)}")

          f = open("bon.txt","a")
          f.write (f"anda memesan {pesanan}")
          f.write(f"\njumlah pesanan : {jumlah_pesanan}")
          # f.write(f"\ntotal harganya : {total_harga}")
          f.write(30*"=")
          f = open("bon.txt","r")
          print(f.read())
          f.close()


welcomeScreen()
entryPilihanMenu()