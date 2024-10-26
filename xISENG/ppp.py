# class Orang:
#     def __init__(self, nama):
#         self.nama = nama

# class Mahasiswa(Orang):
#     def __init__(self, nama, npm, prodi):
#         super().__init__(nama)
#         self.npm = npm
#         self.prodi = prodi

# class Dosen(Orang):
#     def __init__(self, nama, nidn, jabatan):
#         super().__init__(nama)
#         self.nidn = nidn
#         self.jabatan = jabatan

# mhs = Mahasiswa("Andi", "123456789", "Teknik Informatika")
# print(mhs.nama,mhs.npm,mhs.prodi)
# dosen = Dosen("Budi", "987654321", "Dosen Tetap")
# print(dosen.nama)
# print(dosen.nidn)
# print(dosen.jabatan)

# class Orang:
#     def __init__(self, nama):
#         self.nama = nama

# class Mahasiswa(Orang):
#     def __init__(self, nama, npm, prodi):
#         super().__init__(nama)
#         self.npm = npm
#         self.prodi = prodi

#     def get_info1(self):
#         return f"Nama: {self.nama}\nNPM: {self.npm}\nProdi: {self.prodi}"

# class Dosen(Orang):
#     def __init__(self, nama, nidn, jabatan):
#         super().__init__(nama)
#         self.nidn = nidn
#         self.jabatan = jabatan

#     def get_info2(self):
#         return f"Nama: {self.nama}\nNIDN: {self.nidn}\nJabatan: {self.jabatan}"

# mhs = Mahasiswa("Andi", "123456789", "Teknik Informatika")
# mahasiswa_info = mhs.get_info1()

# dosen = Dosen("Budi", "987654321", "Dosen Tetap")
# dosen_info = dosen.get_info2()

# print(mahasiswa_info)
# print(dosen_info)

# Inisialisasi list untuk menyimpan daftar makanan dan harga
menu = [
    {'nama': 'Nasi Goreng', 'harga': 15000},
    {'nama': 'Mie Goreng', 'harga': 12000},
    {'nama': 'Bakso', 'harga': 10000},
    {'nama': 'Sate Ayam', 'harga': 12000},
    {'nama': 'Gado-gado', 'harga': 8000}
]

# Menampilkan daftar menu pada layar
print("Daftar Menu Warung:")
for makanan in menu:
    print(makanan['nama'], "\tRp", makanan['harga'])

# Menghitung jumlah makanan yang tersedia
jumlah_makanan = len(menu)
print("Jumlah makanan yang tersedia:", jumlah_makanan)

# Meminta input dari pengguna untuk memesan makanan
pesan = []
while True:
    makanan = input("Masukkan nama makanan yang ingin dipesan (selesai untuk keluar): ")
    if makanan == "selesai":
        break
    for item in menu:
        if item['nama'] == makanan:
            pesan.append(item)
            print(makanan, "telah ditambahkan ke dalam pesanan.")
            break
    else:
        print("Maaf,", makanan, "tidak tersedia.")

# Menampilkan daftar pesanan
if len(pesan) > 0:
    print("Daftar Pesanan:")
    total_harga = 0
    for item in pesan:
        print(item['nama'], "\tRp", item['harga'])
        total_harga += item['harga']
    print("Total harga:", total_harga)
else:
    print("Anda belum memesan makanan.")

# Menghitung jumlah pesanan yang dipesan
jumlah_pesanan = len(pesan)
print("Jumlah pesanan yang dipesan:", jumlah_pesanan)
