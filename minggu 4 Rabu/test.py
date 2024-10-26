def opening():
    print("====================")
    print("==== Aplikasi penghitung IPK ====")
    print("====================")


def daftarMatakuliah():
    print("1. Kalkulus | 3 sks ")
    print("2. PPL | 3 sks ")
    print("3. B.Inggris | 2 sks ")
    print("4. B.Indo | 3 sks ")
    print("5. Exit")

def closing():
    print("Terima kasih!")

opening()
daftarMatakuliah()
status = True
totalnilai = 0
semuasks= 0
listmatkul = []
listjumlah = []
listsks = []

while(status):
    matakuliah = int(input("Silahkan pilih Mata kuliah :"))
    if(matakuliah == 1):
        jumlah = int(input("Masukkan jumlah sks : "))
        semuasks = semuasks + jumlah
        nilai = int(input("Masukkan nilai anda:"))
        totalnilai = totalnilai + nilai
        listmatkul.append("Kalkulus")
        listjumlah.append(jumlah)
        listsks.append(nilai)
    if(matakuliah == 2):
        jumlah = int(input("Masukkan jumlah sks : "))
        semuasks = semuasks + jumlah
        nilai = int(input("Masukkan nilai anda:"))
        totalnilai = totalnilai + nilai
        listmatkul.append("PPL")
        listjumlah.append(jumlah)
        listsks.append(nilai)
    if(matakuliah == 3):
        jumlah = int(input("Masukkan jumlah sks : "))
        semuasks = semuasks + jumlah
        nilai = int(input("Masukkan nilai anda:"))
        totalnilai = totalnilai + nilai
        listmatkul.append("B.Inggris")
        listjumlah.append(jumlah)
        listsks.append(nilai)
    if(matakuliah == 4):
        jumlah = int(input("Masukkan jumlah sks : "))
        semuasks = semuasks + jumlah
        nilai = int(input("Masukkan nilai anda:"))
        totalnilai = totalnilai + nilai
        listmatkul.append("B.Inggris")
        listjumlah.append(jumlah)
        listsks.append(nilai)
    elif(matakuliah == 5):
        status = False
        closing()

print("Berikut daftar ipk anda!", totalnilai/semuasks )
