nama = input("Masukan nama anda : ")
ipk = float(input("Masukin IPK anda : "))
jumlah_sks = int(input("Masukan jumlah SKS anda : "))
pernah_publikasi = input("apakah kamu pernah publikasi? ")
publikasi ="pernah"
if jumlah_sks < 144 :
          print(f"maaf {nama} belum berhak LULUS dari kampus")
elif jumlah_sks >= 144 and ipk < 2.5 :
          print(f"maaf {nama}, anda masih perlu mengulang agar IPK makin tinggi")
elif jumlah_sks >= 144  and ipk >3.5 and pernah_publikasi == publikasi :
          print(f"selamat {nama} LULUS dengam gelar CUMLAUDE")
else :
          print(f"Selamat {nama} telah LULUS")