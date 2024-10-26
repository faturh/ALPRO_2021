syarat = True
total = 0
while syarat :
    print("Selamat datang di warung saya")
    print("pilihan menu : ")
    print("1. Lele = 15.000")
    print("2. Ayam = 17.000")
    print("3. Tahu = 1.500")
    print("4. Nasi = 5.000")
    print("5. END ORDER")
    print("6. EXIT")
    pilihan_menu = int(input("Silahkan pilih menu yang tersedia : \n"))
    if pilihan_menu == 1 :
        jumlah = int(input("Silahkan masukan jumlah nya : "))
        total += 15000*jumlah
    elif pilihan_menu == 2 :
        jumlah = int(input("Silahkan masukan jumlah nya : "))
        total += 17000*jumlah
    elif pilihan_menu == 3 :
        jumlah = int(input("Silahkan masukan jumlah nya : "))
        total += 1500*jumlah
    elif pilihan_menu == 4 :
        jumlah = int(input("Silahkan masukan jumlah nya : "))
        total += 5000*jumlah
    elif pilihan_menu == 5 :
        print (f"totalnya adalah = {total}")
        break
    elif pilihan_menu == 6 : 
        print ("kenapa gajadi mesen kack")
        break