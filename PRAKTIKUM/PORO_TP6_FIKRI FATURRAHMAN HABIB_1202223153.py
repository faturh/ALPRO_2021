import matplotlib.pyplot as plt
# Data PT Maju Mundur profit dari tahun 2005-2019
years = [2005, 2006, 2007, 2008, 2009,2010,2011,2012,2013,2014,2015,2016,2017,2018,2019]
profits = [25, 37, 42, 50, 60,64,68,30,45,50,65,70,80,82,88]
# Menghitung total profit
total_profit = sum(profits)

# Menghitung persentase keuntungan setiap tahun
percentages = [profit/total_profit*100 for profit in profits]
# Membuat bar chart
plt.bar(years, profits)
# Memberi label pada sumbu x dan y
plt.xlabel('Tahun')
plt.ylabel('Keuntungan')
plt.legend(['Keuntungan'])
# Memberi judul pada grafik
plt.title('Revenue PT Maju Mundur dari 2005-2019')
# Menampilkan persentase keuntungan untuk setiap tahun di atas setiap bar
for i in range(len(years)):
    plt.text(years[i]-0.3,profits[i]+1,str(round(percentages[i],2))+'%')
# Menampilkan grafik
plt.show()
'''Dari grafik yang telah dibuat, kita dapat melihat bahwa keuntungan PT Maju Mundur cenderung 
   meningkat dari tahun ke tahun, dengan beberapa fluktuasi yang terjadi di antara tahun 2012-2014.
   Namun, kita tidak dapat dengan pasti memprediksi apakah PT Maju Mundur akan memperoleh 
   keuntungan yang lebih tinggi di tahun 2020 hanya berdasarkan data dari tahun sebelumnya.
   Dalam membuat analisis, kita perlu mempertimbangkan faktor-faktor lain yang dapat 
   mempengaruhi kinerja perusahaan tersebut. '''