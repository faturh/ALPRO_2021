mahasiswa = ["","Fatur","rahman","habib"]
print(mahasiswa[1])
mahasiswa[0] = "fikri"
print (mahasiswa[2])
# untuk menambah kata pake.append
mahasiswa.append("kerja")
mahasiswa.append("nya bagus")
# untuk menghapus memakai del
del mahasiswa[1]

for i in range(len(mahasiswa)):
    print(i, "", mahasiswa[i])