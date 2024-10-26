def opening():
    print("================================")
    print("SELAMAT DATANG DI APLIKASI WARUNG LELE")
    print("================================")

def menuWarunglele():
    print("\n1. Lele Goreng | Rp. 11.000,00")
    print("2. Tahu Goreng | Rp. 3.000,00")
    print("3. Ayam Goreng | Rp. 20.000,00")

def closing():
    print("Terima kasih anda sudah berkunjung!")

opening()
menuWarunglele()
listmenu = []
listjumlah = []
listharga = []
status =True
while(status) :
    menu =int(input("Silahkan pilih menu :"))
    jumlah = int(input("Masukan jumlah yang anda inginkan : "))
    if(menu == 1) :
        listmenu.append(menu)
        listjumlah.append(jumlah)
        listharga.append(10000)
    if(menu == 2) :
        listmenu.append(menu)
        listjumlah.append(jumlah)
        listharga.append(1000)
    if(menu == 3) :
        listmenu.append(menu)
        listjumlah.append(jumlah)
        listharga.append(11000)

    elif(menu == 4) and jumlah == 4 : 
        status = False
        closing()
        
print("Berikut daftar pesanan anda")
f = open("tagihan.txt","w")
for i in range(len(listmenu)) :
    print(i,"",listmenu[i]," | ",listharga[i]," | ", listjumlah[i])
    row = "" + str(i) + " | " + str(listmenu[i]) + str(listharga[i]) + " | " + str(listjumlah) + " | "+ str(listharga[i])
    f.write(row)
    f.write("\n")
