import numpy as np

# Fungsi untuk menginput data pengunjung dan pembeli
def input_data():
    # Meminta input dari pengguna untuk jumlah hari
    jumlah_hari = int(input("Masukkan jumlah hari selama sebulan: "))
    
    # Inisialisasi list untuk menyimpan data pengunjung dan pembeli
    pengunjung = []
    pembeli = []
    
    # Loop untuk meminta input pengunjung untuk setiap hari
    for i in range(1, jumlah_hari+1):
        data_pengunjung = int(input("Masukkan jumlah pengunjung pada hari ke-{}: ".format(i)))
        pengunjung.append(data_pengunjung)

    # Loop untuk meminta input pembeli untuk setiap hari
    for i in range(1, jumlah_hari+1):
        data_pembeli = int(input("Masukkan jumlah pembeli pada hari ke-{}: ".format(i)))
        pembeli.append(data_pembeli)
        
    # Menampilkan data yang telah diinput
    print("\nData pengunjung:", pengunjung)
    print("Data pembeli:", pembeli)

    # Memanggil fungsi menu
    menu(pengunjung, pembeli)

# Fungsi untuk menampilkan menu dan memproses pilihan pengguna
def menu(pengunjung, pembeli):
    while True:
        print("\n======menu======")
        print("1. Minimum")
        print("2. Maximum")
        print("3. Mean")
        print("4. Median")
        print("5. Standar deviasi")
        print("6. Quartil")
        print("7. Covarian & Korelasi")
        print("8. Variansi")
        print("9. Masukan ulang data")
        print("0. Keluar")
        
        # Meminta input dari pengguna untuk pilihan menu
        pilihan = int(input("Pilih salah satu: "))
        
        # Proses pilihan pengguna
        if pilihan == 1:
            print("Jumlah pengunjung paling sedikit dalam 1 hari adalah ", np.min(pengunjung))
            print("Jumlah pembeli paling sedikit dalam 1 hari adalah :", np.min(pembeli))
        elif pilihan == 2:
            print("Jumlah pengunjung paling sedikit dalam 1 hari adalah ", np.max(pengunjung))
            print("Jumlah pembeli paling sedikit dalam 1 hari adalah ", np.max(pembeli))
        elif pilihan == 3:
            print("Rata-rata pengunjung selama {} hari adalah ".format(len(pengunjung)), np.mean(pengunjung))
            print("Rata-rata pembeli selama {} hari adalah ".format(len(pembeli)), np.mean(pembeli))
        elif pilihan == 4:
            print("Median pengunjung selama {} hari adalah ".format(len(pengunjung)), np.median(pengunjung))
            print("Median pembeli selama {} hari adalah ".format(len(pembeli)), np.median(pembeli))
        elif pilihan == 5:
            print("Standar deviasi data pengunjung selama {} hari adalah ".format(len(pengunjung)), np.std(pengunjung))
            print("Standar deviasi data pembeli selama {} hari adalah ".format(len(pembeli)), np.std(pembeli))
        elif pilihan == 6:
            print("Nilai quartil dari data pengunjung selama {} hari adalah: ".format(len(pengunjung)))
            print("Q1:", np.percentile(pengunjung, 25))
            print("Q2:", np.percentile(pengunjung, 50))
            print("Q3", np.percentile(pengunjung, 75))
            print("Nilai quartil dari data pembeli selama {} hari adalah: ".format(len(pembeli)))
            print("Q1:", np.percentile(pembeli, 25))
            print("Q2:", np.percentile(pembeli, 50))
            print("Q3:", np.percentile(pembeli, 75))
        elif pilihan == 7:
            print("Covarian ", np.cov(pengunjung, pembeli)[0,1])
            print("Korelasi ", np.corrcoef(pengunjung, pembeli)[0,1])
        elif pilihan == 8:
            print("Variansi dari data pengunjung pengunjung selama {} hari adalah ".format(len(pengunjung)), np.var(pengunjung))
            print("Variansi dari data pembeli pembeli selama {} hari adalah ".format(len(pembeli)), np.var(pembeli))
        elif pilihan == 9:
            input_data()
        elif pilihan == 0:
            print("=====PROGRAM SELESAI=====")
            break
        else:
            print("Pilihan tidak valid. Silakan pilih menu yang tersedia.") 
input_data()