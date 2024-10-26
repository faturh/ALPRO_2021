data_mahasiswa = {
    "fatur" : "hehe",
    "hah" : "heh"
}
syarat = True
i = 3
while syarat :
    print ("Silahkan login ke aplikasi")
    username = input ("Masukan username anda : ")
    password = input ("Masukan password anda : ")
    if username in data_mahasiswa and data_mahasiswa[username] == password :
        print("Selamat datang di aplikasi")
        break
    else :
        print("DATA TIDAK SAMA!")
        i -= 1
    if i == 2 :
          print ("percobaan sisa 2")
    elif i == 1 :
          print ("percobaan sisa 1")
    else :
          print ("login anda gagal")
          syarat = False