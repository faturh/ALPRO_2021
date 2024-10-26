import numpy as np

#sort ascending(dari yg kecil) 
nomor = np.array([20,1,5,18,8,25,3,7,12])
print(np.sort(nomor))

#descending (dari yg besar)
print(np.sort(nomor)[::-1])

nomor_sudahdiurutkan = np.sort(nomor)
print(nomor_sudahdiurutkan[0])
