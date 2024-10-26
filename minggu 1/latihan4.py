nama = input("Masukan nama anda : ")
usia = int(input("Masukan usia anda : "))
jenis_kelamin = input("Masukan jenis kelamin anda : ")

p = "pria"
c = "perempuan"

if jenis_kelamin == p and usia >= 17 :
           print (f"Selamat datang {nama}, kamu PRIA DEWASA")
elif jenis_kelamin == p and usia < 17 :
           print("usia anda belum cukup")
else :
          print(f"selamat datang {nama}, semua WANITA")