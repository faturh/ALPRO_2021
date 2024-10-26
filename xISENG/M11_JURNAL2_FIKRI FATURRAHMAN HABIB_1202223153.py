import numpy as np
print(" Program Pencari nilai Standar Deviasi dan Variansi ")
nilai =[]        
Jm = int(input("Masukan jumlah siswa: "))
                    
for i in range (Jm):
          Nm= int(input(f"Masukan Nilai Siswa ke-{i+1} : "))
          nilai.append(Nm)

print(f"Nilai Standar Deviasi dari data tersebut adalah {np.std(nilai)} ")
print(f"Nilai Standar Variansi dari data tersebut adalah {np.var(nilai)} ")
