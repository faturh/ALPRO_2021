def hitungLuasPersegipanjang(panjang, Lebar) :
    luas =(panjang * Lebar)
    return luas
panjang = int(input("Masukan panjang persegi = "))
lebar = int(input("Masukan lebar persegi = "))
L = hitungLuasPersegipanjang(panjang,lebar)
print(f"hasil = {L}")
L2 = hitungLuasPersegipanjang(111,5)
print(f"hasil = {L2}")

for i in range (10,20) : 
    L3 = hitungLuasPersegipanjang(50,i)
    print(f"hasil {L3}")