import matplotlib.pyplot as plt
import seaborn
# Data PT Maju Mundur's profit dari tahun 2005-2019
years = [2005, 2006, 2007, 2008, 2009,2010,2011,2012,2013,2014,2015,2016,2017,2018,2019]
profits = [25, 37, 42, 50, 60,64,68,30,45,50,65,70,80,82,88]

# Menghitung total profit
total_profit = sum(profits)

# Menghitung persentase keuntungan setiap tahun
percentages = [profit/total_profit*100 for profit in profits]

# Membuat bar chart dengan warna yang berbeda untuk setiap bar
colors = ['#9B59B6', '#3498DB', '#95A5A6', '#E74C3C', '#34495E', '#2ECC71', '#F1C40F', '#1abc9c', '#2ecc71', '#3498db', '#9b59b6', '#e74c3c', '#34495e', '#f1c40f', '#95a5a6']
plt.bar(years, profits, color=colors)

# Memberi label pada sumbu x dan y
plt.xlabel('Tahun')
plt.ylabel('Keuntungan')

# Memberi judul pada grafik
plt.title('Revenue PT Maju Mundur dari 2005-2019')

# Menampilkan persentase keuntungan untuk setiap tahun di atas setiap bar
for i in range(len(years)):
    plt.text(years[i]-0.3,profits[i]+1,str(round(percentages[i],2))+'%')

# Menampilkan grafik
plt.show()
