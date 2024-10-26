import numpy as np
print("=====Selamat Datang=====")

print("\n======menu======")
print("1. Input nilai")
print("2. Mean")
print("3. Median")
print("4. Variansi")
print("5.Coveriansi ")
print("0Exit ")
print("===============")



nilai =[]
while True:         
          masukan_pilihan = int(input("\nPilih menu: "))

          if masukan_pilihan == 1 :
                    Jm = int(input("Masukan jumlah siswa: "))
                    
                    for i in range (Jm):
                              Nm= int(input(f"Masukan Nilai Siswa ke-{i+1} : "))
                              nilai.append(Nm)
          elif masukan_pilihan == 2:
                    print(f"Nilai mean dari {Jm} adalah : {np.mean(nilai)}")
          elif masukan_pilihan == 3:
                    print(f"Nilai median dari {Jm} adalah : {np.median(nilai)}")
          elif masukan_pilihan == 4:
                    print(f"Nilai variansi dari {Jm} adalah : {np.var(nilai)}")
          elif masukan_pilihan == 5:
                    print(f"Nilai coveriansi dari {Jm} adalah : {np.cov(nilai)}")
          elif masukan_pilihan == 0:
                  print("===========")
                  print("Sampai jumpa....")
                  print("===========")
                  break

                  
                               
    