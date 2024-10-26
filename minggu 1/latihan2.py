print(" ISI DATA DI BAWAH INI \n")
Name = input("Masukan nama : ")
nim = input("Masukan NIM : ")
Prodi = input("Masukan prodi anda :")
nilai_mkppl = int(input("Masukan nilai mk ppl : "))
print("\n")
print(f"Nama saya adalah : {Name}\nNIM saya adalah : {nim}\nprodi saya adalah : {Prodi} ")

if nilai_mkppl > 80 :
          print (F"karena nilai anda = {nilai_mkppl}, Selamat anda lulus ujian!")
else :
          print(f"nilai anda = {nilai_mkppl}, belajar lagi ya!!")
print("END")