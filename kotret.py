from datetime import datetime
import mysql.connector

# Fungsi untuk membuat koneksi ke MySQL
def create_connection():
    conn = mysql.connector.connect(
        host='localhost',
        port='3308',
        user='root',
        password='',
        database='alpro_absen_karyawan'
    )
    return conn

# Fungsi untuk membuat tabel karyawan dan absensi jika belum ada
def create_tables():
    conn = create_connection()
    c = conn.cursor()

    c.execute("CREATE TABLE IF NOT EXISTS user (id_pegawai INT AUTO_INCREMENT PRIMARY KEY, username VARCHAR(255), password VARCHAR(255), nama VARCHAR(255), jabatan VARCHAR(255))")
    c.execute("CREATE TABLE IF NOT EXISTS absensi (id_absen INT AUTO_INCREMENT PRIMARY KEY, tanggal DATE, jam_masuk TIME, jam_pulang TIME, id_pegawai INT, FOREIGN KEY (id_pegawai) REFERENCES user(id_pegawai))")

    conn.commit()
    conn.close()

# Fungsi untuk menambahkan data karyawan
def add_karyawan(username, password, nama, jabatan):
    conn = create_connection()
    c = conn.cursor()
    c.execute("INSERT INTO user (username, password, nama, jabatan) VALUES (%s, %s, %s, %s)",
              (username, password, nama, jabatan))
    conn.commit()
    conn.close()

# Fungsi untuk melakukan login
def login(username, password):
    conn = create_connection()
    c = conn.cursor()
    c.execute("SELECT jabatan FROM user WHERE username=%s AND password=%s", (username, password))
    role = c.fetchone()
    conn.close()
    return role

# Fungsi untuk melakukan absensi
def absensi(tanggal, jam_masuk, jam_pulang, id_pegawai):
    conn = create_connection()
    c = conn.cursor()
    c.execute("INSERT INTO absensi (tanggal, jam_masuk, jam_pulang, id_pegawai) VALUES (%s, %s, %s, %s)",
              (tanggal, jam_masuk, jam_pulang, id_pegawai))
    conn.commit()
    conn.close()

# Fungsi untuk mendapatkan data absensi berdasarkan id_pegawai
def get_absensi(id_pegawai):
    conn = create_connection()
    c = conn.cursor()
    c.execute("SELECT tanggal, jam_masuk, jam_pulang FROM absensi WHERE id_pegawai=%s", (id_pegawai,))
    absensi = c.fetchall()
    conn.close()
    return absensi

# Fungsi untuk mengatur tampilan saat melakukan login
def login_screen():
    username = input("Username: ")
    password = input("Password: ")
    role = login(username, password)
    if role is not None:
        if role[0] == "admin":
            admin_screen()
        else:
            karyawan_screen(username)
    else:
        print("Username or password is incorrect!")

# Fungsi untuk mengatur tampilan saat admin berhasil login
def admin_screen():
    absensi_data = get_absensi(0)  # 0 untuk mendapatkan semua data absensi
    if len(absensi_data) > 0:
        print("Absensi Data:")
        for data in absensi_data:
            tanggal = data[0]
            jam_masuk = datetime.strptime(data[1], "%H:%M:%S").time()
            jam_pulang = None if data[2] is None else datetime.strptime(data[2], "%H:%M:%S").time()
            print(f"Tanggal: {tanggal}, Jam Masuk: {jam_masuk}, Jam Keluar: {jam_pulang}")
    else:
        print("No absensi data available.")

# Fungsi untuk mengatur tampilan saat karyawan berhasil login
def karyawan_screen(username):
    def absensi_action():
        jam_masuk = datetime.now().strftime("%H:%M:%S")
        karyawan_id = get_karyawan_id(username)
        if karyawan_id is not None:
            absensi(datetime.now().date(), jam_masuk, "", karyawan_id)
            print("Absensi berhasil!")
        else:
            print("Karyawan tidak ditemukan!")

    def keluar_action():
        jam_pulang = datetime.now().strftime("%H:%M:%S")
        karyawan_id = get_karyawan_id(username)
        if karyawan_id is not None:
            absensi_data = get_absensi(karyawan_id)
            if len(absensi_data) > 0 and absensi_data[-1][2] is None:
                conn = create_connection()
                c = conn.cursor()
                c.execute("UPDATE absensi SET jam_pulang=%s WHERE id_absen=%s", (jam_pulang, absensi_data[-1][0]))
                conn.commit()
                conn.close()
                print("Absensi keluar berhasil!")
            else:
                print("Anda belum melakukan absensi masuk!")
        else:
            print("Karyawan tidak ditemukan!")

    def get_karyawan_id(username):
        conn = create_connection()
        c = conn.cursor()
        c.execute("SELECT id_pegawai FROM user WHERE username=%s", (username,))
        karyawan_id = c.fetchone()
        conn.close()
        return karyawan_id[0] if karyawan_id is not None else None

    print("Karyawan Panel:")
    print("1. Absensi")
    print("2. Keluar")
    choice = input("Enter your choice: ")
    if choice == "1":
        absensi_action()
    elif choice == "2":
        keluar_action()
    else:
        print("Invalid choice!")

# Fungsi untuk mengatur tampilan saat melakukan registrasi
def register_screen():
    username = input("Username: ")
    password = input("Password: ")
    nama = input("Nama: ")
    jabatan = input("Jabatan: ")
    if username == "" or password == "":
        print("Username and password are required!")
    else:
        add_karyawan(username, password, nama, jabatan)
        print("Registration successful!")

# Fungsi untuk menampilkan menu utama
def main_menu():
    create_tables()  # Membuat tabel jika belum ada
    print("Absensi SDM")
    print("1. Register")
    print("2. Login")
    print("3. Exit")

    while True:
        choice = input("Enter your choice: ")
        if choice == "1":
            register_screen()
        elif choice == "2":
            login_screen()
        elif choice == "3":
            print("Anda keluar dari program!")
            break
        else:
            print("Invalid choice!")

# Menampilkan menu utama
main_menu()
