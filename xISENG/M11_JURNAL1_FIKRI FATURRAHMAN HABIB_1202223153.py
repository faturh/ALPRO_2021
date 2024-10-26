import numpy as np
print("=====Program Menghitung Nilai=====")
print("a. Input nilai")
print("b. Lihat nilai")
print("c. Rata-rata nilai")
print("d. Nilai Tertinggi")
print("e.Exit ")

nilai =[]
while True:         
        masukan_pilihan = (input("Pilih menu: "))

        if masukan_pilihan == "a" :
                Jm = int(input("Masukan jumlah siswa: "))
                    
                for i in range (Jm):
                        Nm= int(input(f"Masukan Nilai Siswa ke-{i+1} : "))
                        nilai.append(Nm)
        elif masukan_pilihan == "b":
                print(f"Nilai murid adalah : {(nilai)}")
        elif masukan_pilihan == "c":
                print(f"Nilai mean dari {Jm} adalah : {np.mean(nilai)}")
        elif masukan_pilihan == "d":
                print(f"Nilai variansi dari {Jm} adalah : {np.max(nilai)}")
        elif masukan_pilihan == "e":
                break
        else:
                print("Tidak ada menu yang di pilih, silahkan coba kembali")

                  
                               
    