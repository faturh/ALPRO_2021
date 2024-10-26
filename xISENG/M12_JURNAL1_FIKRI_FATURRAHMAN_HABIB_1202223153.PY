import matplotlib.pyplot as plt

tanggal = [1,2,3,4,5,6,7,8,9,10,11,12,13,14,15,16,17,18,19,20,21,22,23,24,25,26,27,28]
absen = [5,4,6,1,2,5,4,3,2,1,2,2,3,4,5,6,1,2,3,4,1,2,1,2,3,3,4,5]
kerusakan = [ 4.5,3.8,4.4,1.8,1.2,3.3,4.2,2.1,2,1.4,1.8,2.2,2.8,4.1,4.4,5.6,1.2,1.5,3.2,4.3,0.7,2.1,2,2.3,3.3,3.8,3.7,5]

fig,ax = plt.subplots(figsize=(7,6))#menampung objek figure

#konfigurasi label sumbu x dan y plot denagn garis lurus
ax.set_xticklabels(['0 orang','1 orang','2 orang','3 orang','4 orang','5 orang','6 orang'])
ax.set_yticklabels(['0 ','1%','2%','3%','4%','5%'])
#membuat scatter denagn warna bbiru dan marker x
plt.scatter(absen,kerusakan,color='blue',marker='x', s=30)

plt.xlabel("Jumlah Absensin")#memberi judul sumbu x
plt.ylabel("Tingkat kerusakan")#memberi judul sumbu y
plt.title('Hubungan antara jumlah absensi dengan tingkat kerusakan produksi gudang DasPro')#memberi judul pada scatter

plt.grid()#menampilkan grid
plt.show()#menampillan scatter
'''berdasarkan data diatas data yang tertampilkan,terlihat kenaikan kerusakan produk'''