def screen( ):
          print(60*"=")
          print("PROGRAM MANAJEMEN DATA PENDAPATAN NASI GORENG KATSU".center(60))
          print(60*"=")
def menu ():
          print("1. Tambahan Data pendapatan")
          print("2. Mengurutkan Data (dari yang terbesar)")
          print("3. Menghitung Total Data Pendapatan")
          print("4. Menghapus Data pendapatan")
          print("5. Menampilkan Seluruh Data Pendapatan")
          print("0. exit")
def selesai():
        print("Program selesai. Terima kasih!")
screen()
menu()

pendapatan = []
status = True
total_pendapatan = 0
while status :
          pilihan = int(input("Masukan menu pilihan anda : "))
          if pilihan == 1 :
                  uang_masuk = int(input("Masukan data pendapatan : "))
                  total_pendapatan +=uang_masuk
                  pendapatan.append(uang_masuk)
                  print(f"Data pendapatan penjualan nasi goreng katsu sebsesar {uang_masuk} berhasil di tambahkan")
          elif pilihan == 2 :
                  pendapatan.sort(reverse = True)
                  print("Data penjualan nasi goreng katsu berhasil di urutkan")
          elif pilihan == 3 :
                  print (f"Total pendapatan penjualan nasi goreng katsu adalah {total_pendapatan}")
          elif pilihan == 4 :
                  menghapus_data = int(input("Masukan data yang akan di hapus : "))
                  pendapatan.remove(menghapus_data)
                  print(f"Data pendapatan penjualan nasi goreng katsu sebesar {menghapus_data} berhasil dihapus")
          elif pilihan == 5 :
                    for x, p in enumerate(pendapatan):
                        print(f"{x+1}. Rp. {p}")
          elif pilihan == 0 :
                  status = False
                  selesai()
          elif pilihan not in [1,2,3,4,5,0] :
                  print("Menu tidak tersedia, silahkan pilih menu lain")
                  continue
          else :
                  break