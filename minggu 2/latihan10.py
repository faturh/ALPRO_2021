syarat = True
i = 0
while syarat :
    print("pilih menu")
    print("1. Biodata")
    print("2. Perwalian")
    print("3. EXIT")
    pilihan = int(input("Masukan pilihan anda : "))
    if pilihan == 1 :
         print ("="*40)
         print ("Menu Data Entry Biodata".center(40))
         print ("="*40)
         nama = input("Masukan nama anda : ")
         usia = input("Masukan usia anda : ")
         print ("Terima kasih anda telah mengisi biodata")
         print (f"Nama anda {nama}")
         print (f"usia anda {usia}")
    elif pilihan == 2 :
         print ("="*40)
         print ("besok perwalian jam 07.30".center(40))
         print ("="*40)
         absen = input("apakah anda hadir? hadir/tidak ")
         if absen == "hadir":
              print("oke")
         else :
              print ("anda di hukum")
    elif pilihan == 3 :
         break
