nama = input("Masukan nama anda : ")
usia = int(input("Masukan usia anda : "))
jenis_kelamin = input("Masukan jenis kelamin anda : ")

p = "pria"
c = "perempuan"

if jenis_kelamin == p and usia >= 17 :
          print (f"Selamat datang {nama}, kamu hanya bisa menonton film sport")
elif jenis_kelamin == p and usia != 17 :
          print(f"anda belum cukup umur")
        
elif jenis_kelamin == c and usia < 17 :
           print("anda hanya bisa menonton drakor")
