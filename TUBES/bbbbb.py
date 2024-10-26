from datetime import datetime
from datetime import date
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

    c.execute("CREATE TABLE IF NOT EXISTS absensi (id_absen INT AUTO_INCREMENT PRIMARY KEY, tanggal DATE, jam_masuk TIME, jam_keluar TIME, id_pegawai INT, FOREIGN KEY (id_pegawai) REFERENCES user(id_pegawai))")

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
def absensi(tanggal, jam_masuk, id_pegawai):
    conn = create_connection()
    c = conn.cursor()
    c.execute("INSERT INTO absensi (id_absen,tanggal, jam_masuk, id_pegawai) VALUES (%s, %s, %s, %s)",
              ("", tanggal, jam_masuk, id_pegawai))
    conn.commit()
    conn.close()

# Fungsi untuk mendapatkan data absensi berdasarkan id_pegawai
def get_absensi(id_pegawai):
    conn = create_connection()
    c = conn.cursor()
    c.execute("SELECT tanggal, jam_masuk, jam_keluar FROM absensi WHERE id_pegawai=%s", (id_pegawai,))
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
    conn = create_connection()
    c = conn.cursor()
    c.execute("SELECT user.nama,tanggal,jam_masuk,jam_keluar FROM absensi INNER JOIN user ON absensi.id_pegawai = user.id_pegawai;")
    absensi_data = c.fetchall() # 0 untuk mendapatkan semua data absensi
    if len(absensi_data) > 0:
        print("Absensi Data:")
        for data in absensi_data:
            nama = data[0]
            tanggal = data[1]
            jam_masuk = data[2]
            jam_keluar = data[3]
            print(f"nama: {nama} Tanggal: {tanggal}, Jam Masuk: {jam_masuk}, Jam Keluar: {jam_keluar}")
    else:
        print("No absensi data available.")

# Fungsi untuk mengatur tampilan saat karyawan berhasil login
def karyawan_screen(username):
    def absensi_action():
        login_id = get_karyawan_id(username)
        con = create_connection()
        cur = con.cursor()
        datetoday = date.today()
        time = datetime.now().strftime("%H:%M:%S")
        cur.execute("INSERT INTO ABSENSI (id_absen,tanggal,jam_masuk,id_pegawai)VALUES ('{}','{}','{}','{}')".format("",datetoday,time,login_id))
        cur.execute("SELECT tanggal FROM absensi WHERE id_pegawai = '{}'".format(login_id))
        data_tanggal = cur.fetchall()
        if data_tanggal[-1][-1] == datetoday and len(data_tanggal) >1  :
            cur.execute("SELECT max(id_absen) FROM absensi WHERE id_pegawai = '{}'".format(login_id))
            id_absen = cur.fetchone()[0]
            cur.execute("DELETE FROM absensi WHERE id_absen = '{}'".format(id_absen))
            print("Absen masuk gagal")
        else : 
            print("Absen masuk berhasil")
        con.commit()
   

    def keluar_action():
        karyawan_id = get_karyawan_id(username)
        con = create_connection()
        cur = con.cursor()
        datetoday = date.today()
        time = datetime.now().strftime("%H:%M:%S")
        cur.execute("SELECT jam_keluar FROM absensi WHERE id_pegawai = '{}'".format(karyawan_id))
        s = (cur.fetchall()[-1][0])
        if s == None :
            cur.execute("UPDATE absensi SET jam_keluar = '{}' WHERE id_pegawai = '{}' and tanggal = '{}'".format(time,karyawan_id,datetoday))
            con.commit()
            print('Absen keluar berhasil')
        else :
            print('Absen keluar gagal')

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
    print("3. Rekap absensi")
    choice = input("Enter your choice: ")
    if choice == "1":
        absensi_action()
    elif choice == "2":
        keluar_action()
    elif choice == "3":
        rekapabsen(username)
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

# untuk rekap asben
def rekapabsen(username, password):
    con = create_connection()
    cur = con.cursor()
    cur.execute("SELECT user.nama,tanggal,jam_masuk,jam_keluar FROM absensi INNER JOIN user ON absensi.id_pegawai = user.id_pegawai;")
    data = cur.fetchall()
    a = []
    for x in range(len(data)) :
     a.append(f"{data[x][0]}--{data[x][1]}--{data[x][2]}--{data[x][3]}")
     
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