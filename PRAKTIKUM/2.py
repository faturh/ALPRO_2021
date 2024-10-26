class Data:
    def __init__(self, kode, nama, harga, stok):
        self.kode_produk = kode
        self.nama_produk = nama
        self.harga_produk = harga
        self.stok_produk = stok
    def screen ():
            print(40 * "=")
            print("Toko online".center(40))
            print(40 * "=")
            print("1. Tambah Produk".center(40))
            print("2. Daftar Produk".center(40))
            print("3. Hapus produk".center(40))
            print("4. Keluar".center(33))
    screen()

class aplikasi_toko_online(Data):
    def __init__(self):
        self.data_produk = []

    def tambah_data(self, kode, nama, harga, stok):
        self.data_produk.append(Data(kode, nama, harga, stok))

    def menampilkan_data(self):
        print("Daftar produk: ")
        for data in self.data_produk:
            print(f"Kode: {data.kode_produk} | Nama: {data.nama_produk} | Harga: {data.harga_produk} | Stok: {data.stok_produk}")

    def hapus_data(self, kode):
        for data in self.data_produk:
            if data.kode_produk == kode:
                self.data_produk.remove(data)
                print("Produk berhasil dihapus!")
                return
        print("Data produk tidak ditemukan")

    def menunya(self):
        while True:
            pilihan = int(input("Silahkan pilih menu (1/2/3/4): "))
            if pilihan == 1:
                kode = int(input("Masukkan kode produk  : "))
                nama = input("Masukkan nama produk  : ")
                harga = int(input("Masukkan harga produk : "))
                stok = int(input("Masukkan stok produk  : "))
                self.tambah_data(kode, nama, harga, stok)
                print("Produk berhasil ditambahkan")
            elif pilihan == 2:
                self.menampilkan_data()
            elif pilihan == 3:
                hapus_data = int(input("Masukkan kode produk yang ingin dihapus: "))
                self.hapus_data(hapus_data)
            elif pilihan == 4:
                break
        print("Terima kasih telah menggunakan aplikasi toko online!")

    def run(self):
        self.menunya()


aplikasi = aplikasi_toko_online()
aplikasi.run()
