import numpy as np
print("===> MENU DOSEN <===")
print("1. Nilai MIN dan Nilai Max")
print("2.Nilai quartil")
print("0.Exit")
print("==============================")

nilai =[98,55,76,83,75,77,65,90,98,84,77,74,80,90,100,97]
kelas = input("masukan nama kelas : ")

while True:         
          masukan_pilihan = int(input("\nPilih menu: "))

          if masukan_pilihan == 1 :
                    print(f"Nilai Maximum Kelas {kelas} : {np.max(nilai)}")
                    print(f"Nilai Minimum Kelas {kelas} : {np.min(nilai)}")
          elif masukan_pilihan == 2:
                    print(f"Q1 kelas {kelas}: ", np.percentile(nilai, 25))
                    print(f"Q2 kelas{kelas}: ", np.percentile(nilai, 50))
                    print(f"Q3 kelas{kelas}: ", np.percentile(nilai, 75))
          elif masukan_pilihan == 0:
                    print("sampai jumpa lagi")
                    break
          else:
                    print("Pilihan menu tidak tersedia")