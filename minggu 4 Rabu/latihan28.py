def opening():
    print(30*"=")
    print("NILAI IPK".center(30))
    print(30*"=")

def menuWarunglele():
    print("1. Kalkulus      | 3 sks")
    print("2. PPL           | 3 sks")
    print("3. B.Inggris     | 2 sks")
    print("4. B.Indo        | 3 sks")
    print("5. exit")

def closing():
    print("SELAMAT!")

opening()
menuWarunglele()

listmatkul = []
listSKS = []
listnilai = []
status = True
nilai = 0
sks = 0
nilai_kali = 0
while(status) :
    mata_kuliah  = int(input("Silahkan pilih mata kuliah :"))
    if(mata_kuliah == 1) :
        jumlah_sks = int(input("Masukan jumlah sks anda : "))
        nilai_matkul = float(input("Masukan nilai anda: "))
        total_nilai = (jumlah_sks*nilai_matkul)
        sks += jumlah_sks
        nilai += total_nilai
        kali = nilai/sks
        nilai_kali += kali 
        print (f"nilai anda sekarang {nilai_kali}")
        listmatkul.append("kalkulus")
        listSKS.append(jumlah_sks)
        listnilai.append(nilai)

    elif(mata_kuliah == 2) :
        jumlah_sks = int(input("Masukan jumlah sks anda : "))
        nilai_matkul = float(input("Masukan nilai anda: "))
        total_nilai = (jumlah_sks*nilai_matkul)
        sks += jumlah_sks
        nilai += total_nilai
        kali = nilai/sks
        nilai_kali += kali 
        print (f"nilai anda sekarang {nilai_kali}")
        listmatkul.append("PPL")
        listSKS.append(jumlah_sks)
        listnilai.append(nilai_matkul)

    elif(mata_kuliah == 3) :
        jumlah_sks = int(input("Masukan jumlah sks anda : "))
        nilai_matkul = float(input("Masukan nilai anda: "))
        total_nilai = (jumlah_sks*nilai_matkul)
        sks +=jumlah_sks
        nilai += total_nilai
        kali = nilai/sks
        nilai_kali += kali 
        print (f"nilai anda sekarang {nilai_kali}")
        listmatkul.append("B.Inggris")
        listSKS.append(jumlah_sks)
        listnilai.append(nilai_matkul)

    elif(mata_kuliah == 4) :
        jumlah_sks = int(input("Masukan jumlah sks anda : "))
        nilai_matkul = float(input("Masukan nilai anda: "))
        total_nilai =(jumlah_sks*nilai_matkul)
        sks +=jumlah_sks
        nilai += total_nilai
        kali = nilai/sks
        nilai_kali += kali 
        print (f"nilai anda sekarang {nilai_kali}")
        listmatkul.append("B.Indo")
        listSKS.append(jumlah_sks)
        listnilai.append(nilai_matkul)

    elif(mata_kuliah == 5) : 
        status = False
closing()     
print(f"Berikut nilai anda {nilai/sks}")
print("Berikut daftar nilai anda")
f = open("IPK.txt","w")
for i in range(len(listmatkul)) :
    print(i,"",listmatkul[i]," | ",listnilai[i]," | ", listSKS[i])
    row = "" + str(i) + " | " + str(listmatkul[i]) + str(listnilai[i]) + " | " + str(listSKS) + " | "+ str(listnilai[i])
    f.write(row)
    f.write("\n")