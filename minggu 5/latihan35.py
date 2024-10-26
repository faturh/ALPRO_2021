import numpy as np

nilai = np.array([85,81,75,68,95,63,77,82])

# hasil filter diletakkan di aray baru (empty array)
hasilFilter = []

#ingin filter hanya ambil data diatas 80 saja
for element in nilai:
    if(element > 80):
        hasilFilter.append(element) # .append(element) untuk menambahkan nilai yang sesuai pengkondisian kedalam hasilFilter

print(hasilFilter)
