from datetime import datetime, time
import mysql.connector

# Fungsi untuk membuat koneksi ke MySQL
def create_connection():
    conn = mysql.connector.connect(
        host='localhost',
        port='3308',
        user='root',
        password='',
        database='absen_karyawan'
    )
    return conn

# Fungsi untuk membuat tabel karyawan dan absensi jika belum ada
def create_tables():
    conn = create_connection()
    c = conn.cursor()

    c.execute('''CREATE TABLE IF NOT EXISTS user (
        id_pegawai INT PRIMARY KEY AUTO_INCREMENT,
        username VARCHAR(50) UNIQUE NOT NULL,
        password VARCHAR(50) NOT NULL,
        nama VARCHAR(100) NOT NULL,
        jabatan VARCHAR(50) NOT NULL
    )''')

    c.execute('''CREATE TABLE IF NOT EXISTS absensi (
        id_absen INT PRIMARY KEY AUTO_INCREMENT,
        tanggal DATE NOT NULL,
        jam_masuk TIME NOT NULL,
        jam_keluar TIME,
        id_pegawai INT NOT NULL,
        FOREIGN KEY (id_pegawai) REFERENCES user (id_pegawai)
    )''')

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
def absensi(tanggal, jam_masuk, jam_keluar, username):
    conn = create_connection()
    c = conn.cursor()

    # Retrieve the id_pegawai using the provided username
    c.execute("SELECT id_pegawai FROM user WHERE username=%s", (username,))
    result = c.fetchone()
    if result is None:
        # User not found
        conn.close()
        print("Username is not valid!")
        return

    id_pegawai = result[0]
    c.execute("INSERT INTO absensi (tanggal, jam_masuk, jam_keluar, id_pegawai) VALUES (%s, %s, %s, %s)",
              (tanggal, jam_masuk, jam_keluar, id_pegawai))
    conn.commit()
    conn.close()

# Fungsi untuk mendapatkan data absensi berdasarkan id_pegawai atau username (opsional)
def get_absensi(id_pegawai=None, username=None):
    conn = create_connection()
    c = conn.cursor()

    if id_pegawai is not None:
        c.execute("SELECT tanggal, jam_masuk, jam_keluar FROM absensi WHERE id_pegawai=%s", (id_pegawai,))
    elif username is not None:
        # Retrieve the id_pegawai using the provided username
        c.execute("SELECT id_pegawai FROM user WHERE username=%s", (username,))
        result = c.fetchone()
        if result is None:
            # User not found
            conn.close()
            return []
        id_pegawai = result[0]
        c.execute("SELECT tanggal, jam_masuk, jam_keluar FROM absensi WHERE id_pegawai=%s", (id_pegawai,))
    else:
        c.execute("SELECT tanggal, jam_masuk, jam_keluar FROM absensi")

    absensi = c.fetchall()
    conn.close()
    return absensi

# Fungsi untuk mengatur tampilan saat melakukan login
def login_screen():
    print("Login")
    username = input("Username: ")
    password = input("Password: ")
    jabatan = login(username, password)
    if jabatan is not None:
        if jabatan[0] == "admin":
            admin_screen()
        else:
            karyawan_screen(username)
    else:
        print("Username or password is incorrect!")

# Fungsi untuk mengatur tampilan saat admin berhasil login
def admin_screen():
    print("Admin Panel")
    choice = ""
    while choice != "3":
        print("1. View Absensi")
        print("2. Exit")
        choice = input("Enter your choice: ")
        if choice == "1":
            absensi_data = get_absensi()
            if len(absensi_data) > 0:
                print("Absensi Data:")
                for data in absensi_data:
                    print(f"Tanggal: {data[0]}, Jam_masuk: {data[1]}, Jam_Keluar: {data[2]}")
            else:
                print("No absensi data available.")
        elif choice == "2":
            break
        else:
            print("Invalid choice!")

# Fungsi untuk mengatur tampilan saat karyawan berhasil login
def karyawan_screen(username):
    print("Karyawan Panel")
    choice = ""
    while choice != "3":
        print("1. Absensi")
        print("2. Keluar")
        choice = input("Enter your choice: ")
        if choice == "1":
            jam_masuk = datetime.now().strftime("%H:%M:%S")
            absensi(datetime.now().date(), jam_masuk, None, username)
            print("Absensi berhasil!")
        elif choice == "2":
            jam_keluar = datetime.now().strftime("%H:%M:%S")
            absensi_data = get_absensi(username=username)
            if len(absensi_data) > 0 and absensi_data[-1][2] is None:
                conn = create_connection()
                c = conn.cursor()
                c.execute("UPDATE absensi SET jam_keluar=%s WHERE id_absen=%s", (jam_keluar, absensi_data[-1][0]))
                conn.commit()
                conn.close()
                print("Absensi keluar berhasil!")
            else:
                print("Anda belum melakukan absensi masuk!")
        else:
            print("Invalid choice!")

# Fungsi untuk mengatur tampilan saat melakukan registrasi
def register_screen():
    print("Register")
    username = input("Username: ")
    password = input("Password: ")
    nama = input("Nama: ")
    jabatan = input("Jabatan (Karyawan/Admin): ")
    add_karyawan(username, password, nama, jabatan)
    print("Registration successful!")

# Fungsi untuk menampilkan menu utama
def main_menu():
    create_tables()

    choice = ""
    while choice != "3":
        print("1. Register")
        print("2. Login")
        print("3. Exit")
        choice = input("Enter your choice: ")
        if choice == "1":
            register_screen()
        elif choice == "2":
            login_screen()
        elif choice == "3":
            print("Exiting program!")
        else:
            print("Invalid choice!")

# Menampilkan menu utama
main_menu()
