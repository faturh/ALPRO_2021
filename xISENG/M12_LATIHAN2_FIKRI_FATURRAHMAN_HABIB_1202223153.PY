import matplotlib.pyplot as plt

tahun = [2013,2014,2015,2016,2017,2018,2019,2020,2021,2022]
b = [80000,55000,65000,50000,70000,65000,90000,85000,60000,75000]
s = [42000,64000,36000,50000,72000,47000,58000,88000,86000,74000]
ppp = b+s

fig,ax = plt.subplots(figsize=(10,10))

plt.plot(tahun,b,marker='o',markerfacecolor='b',markersize=9,label='Bandung')
plt.plot(tahun,s,marker='*',markerfacecolor='r',markersize=9,label='Subang')

plt.xticks(tahun)
plt.xlabel("Tahun")
plt.ylabel("Kota")
plt.legend()
plt.title("Grafik persebaran penduduk")
plt.grid()
plt.show()

'''Setelah melihat data tersebut dapat kita simpulkan bahwa pertumbuhan penduduk di kota Bandung dan Subang
meningkat dalam tahun ke tahun dengan beberapa fluktuasi yang terlihat didalam data akan hal itu kita perlu 
melakukan persebaran penduduk'''