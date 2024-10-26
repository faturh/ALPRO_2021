import os
def welcomescreen():
    os.system("cls")
    print(40*"=")
    print("SELAMAT DATANG DI APLIKASI WARUNG LELE")
    print(40*"=")
    
def displaypilihanmenu() :
       print("Lele goreng  | Rp. 11.000")
       print("Tahu goreng  | Rp. 3.000")
       print("Ayam goreng  | Rp. 15.000")
       print("Bebek goreng | Rp. 20.000")
def entrypilihanmenu():
          x = int(input("MASUKAN PILIHAN MENU ANDA : "))
          return x
welcomescreen()
displaypilihanmenu()
pilihan = entrypilihanmenu()
print("pilihan anda adalah:",pilihan)