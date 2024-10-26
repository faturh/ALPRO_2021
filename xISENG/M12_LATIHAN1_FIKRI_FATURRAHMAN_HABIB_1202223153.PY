import matplotlib.pyplot as plt

a = [100,135,45,135,95,80,110,115,85,40]
b = [115,45,50,35,160,80,140,130,85,95]
c = [85,55,135,140,170,75,40,140,50,55]
ppp = a+b+c

plt.hist(ppp, color='blue',bins=range(60,120,10),edgecolor='black',label='Berat Badan Ideal')

plt.xticks(range(60,120,10))
plt.xlabel("Berat badan(kg)")
plt.ylabel("Frekuensi")
plt.legend()
plt.title("Distribusi Berat Badan Mahasiswa DasPro")

plt.show()

'''Dari grafik yang telah dibuat,kita dapat melihat ada data dari berat badan
mahasiswa yang mengalami kenaikan berat badan pada range 80-90 lalu menurun lagi'''