def labelnilai (angka):
          if (angka > 80 ):
                    return "A"
          elif (angka >= 70) :
                    return "B"
          elif (angka >= 60) :
                    return "C"
          elif (angka <= 59) :
                    return "E"
labelnilai =labelnilai(int(input("Masukan nilai akhir anda : ")))
print(f"Nilai anda adalah {labelnilai}")
# x = labelnilai(90)
# print(x)
# y = labelnilai(45)
# print(y)        