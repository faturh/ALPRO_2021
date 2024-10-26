# print(" ISI DATA DI BAWAH INI \n")
# Name = input("Masukan nama : ")
# nim = input("Masukan NIM : ")
# Prodi = input("Masukan prodi anda :")
# print("\n")
# print(f"Nama saya adalah : {Name}\nNIM saya adalah : {nim}\nprodi saya adalah : {Prodi} ")
# print("END")
# print("===============================================")

# print(" ISI DATA DI BAWAH INI \n")
# Name = input("Masukan nama : ")
# nim = input("Masukan NIM : ")
# Prodi = input("Masukan prodi anda :")
# nilai_mkppl = int(input("Masukan nilai mk ppl : "))
# print("\n")
# print(f"Nama saya adalah : {Name}\nNIM saya adalah : {nim}\nprodi saya adalah : {Prodi} ")

# if nilai_mkppl > 80 :
#           print (F"karena nilai anda = {nilai_mkppl}, Selamat anda lulus ujian!")
# else :
#           print(f"nilai anda = {nilai_mkppl}, belajar lagi ya!!")
# print("END")

# print("=================================================")

# idmu = "si"
# pwmu = "HEI"
# while True :
#           username = input("Masukan username anda : ")
#           password = input("Masukan password anda : ")
#           if username == idmu and password == pwmu :
#                     print ("Selamat datang di aplikasi SI")
#                     break
#           elif username != idmu and password == pwmu :
#                     print ("username anda salah, coba lagi!")
#           elif username == idmu and password != pwmu :
#                     print ("password anda salah, coba lagi!")
#           else : 
#                     print ("USERNAME DAN PASSWORD ANDA SALAH")

# print("=================================================")

# nama = input("Masukan nama anda : ")
# usia = int(input("Masukan usia anda : "))
# jenis_kelamin = input("Masukan jenis kelamin anda : ")

# p = "pria"
# c = "perempuan"

# if jenis_kelamin == p and usia >= 17 :
#            print (f"Selamat datang {nama}, kamu PRIA DEWASA")
# elif jenis_kelamin == p and usia < 17 :
#            print("usia anda belum cukup")
# else :
#           print(f"selamat datang {nama}, semua WANITA")

# print("==============================================")

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

# def is_leap(year):
#     if year % 4 != 0:  # Jika tahun tidak habis dibagi 4
#         leap = False  # Tahun bukan tahun kabisat
#     else:
#         if year % 100 == 0 and year % 400 != 0:  # Jika tahun habis dibagi 100 tapi tidak habis dibagi 400
#             leap = False  # Tahun bukan tahun kabisat
#         else:
#             leap = True  # Tahun adalah tahun kabisat
#     return leap  # Mengembalikan nilai boolean True/False

# year = int(input())  # Membaca input tahun dari pengguna
# print(is_leap(year))  # Memanggil fungsi is_leap dan mencetak hasilnya
