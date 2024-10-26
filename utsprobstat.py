import numpy as np
import os

os.system("cls")

angka = [10, 12,16, 24 ,80,90]
print(angka)
print(f"standar deviasi =  {np.std(angka,ddof=1)}")
print(f"JAK adalah = {np.percentile(angka,75) - np.percentile(angka,25)}")
print(f"rata-rata = {np.mean(angka)}")
print(f"variansi = {np.var(angka, ddof=1)}")
print(f"median = {np.median(angka)}")
print("Q1:", np.percentile(angka, 25))
print("Q2:", np.percentile(angka, 50))
print("Q3:", np.percentile(angka, 75)) 

print("")

angka1 = [20, 20, 30, 50, 30, 60, 70, 70, 60, 20]
print(angka1)
print(f"standar deviasi =  {np.std(angka1,ddof=1)}")
print(f"rata-rata = {np.mean(angka1)}")
print(f"JAK adalah = {np.percentile(angka1,75) - np.percentile(angka1,25)}")
print(f"variansi = {np.var(angka1, ddof=1)}")
print(f"median = {np.median(angka1)}")
print("Q1:", np.percentile(angka1, 25))
print("Q2:", np.percentile(angka1, 50))
print("Q3:", np.percentile(angka1, 75)) 

print("")

angka2 = [3  ,  2  ,  4 ,   3   , 6   , 5   , 4    ,3]
print(angka2)
print(f"standar deviasi = {np.std(angka2, ddof=1)}")
print(f"JAK adalah = {np.percentile(angka2, 75) - np.percentile(angka2, 25)}")
print(f"rata-rata = {np.mean(angka2)}")
print(f"variansi = {np.var(angka2, ddof=1)}")
print(f"median = {np.median(angka2)}")
print("Q1:", np.percentile(angka2, 25))
print("Q2:", np.percentile(angka2, 50))
print("Q3:", np.percentile(angka2, 75)) 

print("")

angka3 = [5  ,  1   , 3  ,  6  ,  5  ,  7  ,  3   , 6    ,4    ,4]
print(angka3)
print(f"standar deviasi = {np.std(angka3, ddof=1)}")
print(f"JAK adalah = {np.percentile(angka3, 75) - np.percentile(angka3, 25)}")
print(f"rata-rata = {np.mean(angka3)}")
print(f"variansi = {np.var(angka3, ddof=1)}")
print(f"median = {np.median(angka3)}")
print("Q1:", np.percentile(angka3, 25))
print("Q2:", np.percentile(angka3, 50))
print("Q3:", np.percentile(angka3, 75)) 

print("")

angka4 = [2 ,   4  ,  3  ,  6  ,  5 ,   4  ,  3    ,6]
print(angka4)
print(f"standar deviasi = {np.std(angka4, ddof=1)}")
print(f"JAK adalah = {np.percentile(angka4, 75) - np.percentile(angka4, 25)}")
print(f"rata-rata = {np.mean(angka4)}")
print(f"variansi = {np.var(angka4, ddof=1)}")
print(f"median = {np.median(angka4)}")
print("Q1:", np.percentile(angka4, 25))
print("Q2:", np.percentile(angka4, 50))
print("Q3:", np.percentile(angka4, 75)) 