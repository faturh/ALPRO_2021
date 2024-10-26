import tkinter as tk
from tkinter import messagebox
from tkinter import *
from tkinter import ttk
from tkinter.ttk import *
from datetime import datetime
from PIL import ImageTk, Image
import mysql.connector
import os

os.system("cls")

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

# Fungsi untuk menambahkan data karyawan
def add_karyawan(username, password, nama, jabatan):
    conn = create_connection()
    c = conn.cursor()
    c.execute("INSERT INTO user (id_pegawai, username, password, nama, jabatan) VALUES (%s, %s, %s, %s, %s)",
              ('',username, password, nama, jabatan))
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
def absensi(tanggal, jam_masuk, username):
    conn = create_connection()
    c = conn.cursor()

    # Retrieve the id_pegawai using the provided username
    c.execute("SELECT id_pegawai FROM user WHERE username=%s", (username,))
    result = c.fetchone()
    if result is None:
        # User not found
        conn.close()
        messagebox.showerror("Error", "Username is not valid!")
        return

    id_pegawai = result[0]
    c.execute("INSERT INTO absensi (tanggal, jam_masuk, id_pegawai) VALUES (%s, %s, %s)",
              (tanggal, jam_masuk, id_pegawai))
    conn.commit()
    conn.close()

# Fungsi untuk mendapatkan data absensi berdasarkan username
def get_absensi(username):
    conn = create_connection()
    c = conn.cursor()

    # Retrieve the id_pegawai using the provided username
    c.execute("SELECT id_pegawai FROM user WHERE username=%s", (username,))
    result = c.fetchone()
    if result is None:
        # User not found
        conn.close()
        return []

    id_pegawai = result[0]
    c.execute("SELECT tanggal, jam_masuk, jam_keluar FROM absensi WHERE id_pegawai=%s", (id_pegawai,))
    absensi = c.fetchall()
    conn.close()
    return absensi

# Fungsi untuk mengatur tampilan saat melakukan login
def login_screen():
    def login_action():
        username = username_entry.get()
        password = password_entry.get()
        jabatan = login(username, password)
        if jabatan is not None:
            if jabatan[0] == "Admin":
                admin_screen()
                login_window.destroy()
            else:
                karyawan_screen(username)
                login_window.destroy()
        else:
            messagebox.showerror("Error", "Username or password is incorrect!")
            login_window.destroy()

    login_window = tk.Tk()
    login_window.title("Login")
    login_window.geometry("925x500+300+200")
    login_window.resizable(False,False)

    font_style = ("Helvetica", 12,"bold")

    login_frame = tk.Frame(login_window)
    login_frame.pack(expand=True)

    username_label = tk.Label(login_frame, text="Username :", font=font_style)
    username_label.grid(row=0, column=0, padx=10, pady=10, sticky="e")
    username_entry = tk.Entry(login_frame, font=font_style)
    username_entry.grid(row=0, column=1, padx=10, pady=10, sticky="w")

    password_label = tk.Label(login_frame, text="Password :", font=font_style)
    password_label.grid(row=1, column=0, padx=10, pady=10, sticky="e")
    password_entry = tk.Entry(login_frame, show="*", font=font_style)
    password_entry.grid(row=1, column=1, padx=10, pady=10, sticky="w")

    login_button = tk.Button(login_window,width=30, text="Login", command=login_action, font=font_style)
    login_button.pack(pady=(0, 50))

    login_window.mainloop()

# Fungsi untuk mengatur tampilan saat admin berhasil login
def admin_screen():
    def view_absensi():
        absensi_data = get_absensi("Admin")
        if len(absensi_data) > 0:
            messagebox.showinfo("Absensi Data", "\n".join([f"Tanggal: {data[0]}, Jam Masuk: {data[1]}, Jam Keluar: {data[2]}" for data in absensi_data]))
        else:
            messagebox.showinfo("Info", "No absensi data available.")

    admin_window = tk.Toplevel()
    admin_window.title("Admin Panel")
    admin_window.geometry("925x500+300+200")

    font_style = ("Helvetica", 12, "bold")

    view_absensi_button = tk.Button(admin_window, width=35, text="View Tabel Absensi", command=view_absensi, font=font_style)
    view_absensi_button.pack(pady=100)


# Fungsi untuk mengatur tampilan saat karyawan berhasil login
def karyawan_screen(username):
    def absensi_action():
        jam_masuk = datetime.now().strftime("%H:%M:%S")
        absensi(datetime.now().date(), jam_masuk, username)
        messagebox.showinfo("Info", "Absensi berhasil!")
        karyawan_window.destroy()

    def keluar_action():
        conn = create_connection()
        c = conn.cursor()
        id_karyawan = get_karyawan_id(username)
        c.execute("SELECT id_absen,jam_keluar FROM absensi WHERE id_pegawai = %s",(id_karyawan,))
        jam_keluar = datetime.now().strftime("%H:%M:%S")
        absensi_data = c.fetchall()
        if len(absensi_data) > 0 and absensi_data[-1][1] == None:
            c.execute("UPDATE absensi SET jam_keluar=%s WHERE id_absen=%s", (jam_keluar, absensi_data[-1][0]))
            conn.commit()
            conn.close()
            messagebox.showinfo("Info",  "Absensi keluar berhasil!")
        else:
            messagebox.showinfo("Info", "Anda belum melakukan absensi masuk!")

    karyawan_window = tk.Toplevel()
    karyawan_window.title("Karyawan Panel")
    karyawan_window.geometry("925x500+300+200")
    karyawan_window.resizable(False,False)

    font_style = ("Helvetica", 12, "bold")

    absensi_button = tk.Button(karyawan_window, width=35, text="Absensi", command=absensi_action, font=font_style)
    absensi_button.pack(pady=[50,10])

    keluar_button = tk.Button(karyawan_window, width=35, text="Keluar", command=keluar_action, font=font_style)
    keluar_button.pack(pady=10)

    def get_karyawan_id(username):
            conn = create_connection()
            c = conn.cursor()
            c.execute("SELECT id_pegawai FROM user WHERE username=%s", (username,))
            karyawan_id = c.fetchone()
            conn.close()
            return karyawan_id[0] if karyawan_id is not None else None

# Fungsi untuk mengatur tampilan saat melakukan registrasi
def register_screen():
    def register_action():
        username = username_entry.get()
        password = password_entry.get()
        nama = nama_entry.get()
        jabatan = role_combobox.get()

        if username == "" or password == "":
            messagebox.showerror("Error", "Username and password are required!")
        else:
            add_karyawan(username, password, nama, jabatan)
            messagebox.showinfo("Info", "Registration successful!")
            register_window.destroy()

    register_window = tk.Tk()
    register_window.title("Register")
    register_window.geometry("925x500+300+200")
    register_window.resizable(False, False)

    font_style = ("Helvetica", 12,"bold")

    label_frame = tk.Frame(register_window)
    label_frame.pack(pady=(50, 10))

    username_label = tk.Label(label_frame, text="Username :", font=font_style)
    username_label.pack(padx=10, pady=(5, 5))

    username_entry = tk.Entry(label_frame, font=font_style)
    username_entry.pack(padx=10, pady=(0, 5))

    password_label = tk.Label(label_frame, text="Password :", font=font_style)
    password_label.pack(padx=10, pady=(5, 5))

    password_entry = tk.Entry(label_frame, show="*", font=font_style)
    password_entry.pack(padx=10, pady=(0, 5))

    nama_label = tk.Label(register_window, text="Nama :", font=font_style)
    nama_label.pack(padx=10, pady=(5, 5))

    nama_entry = tk.Entry(register_window, font=font_style)
    nama_entry.pack(padx=10, pady=(0, 5))

    role_label = tk.Label(register_window, text="Jabatan :", font=font_style)
    role_label.pack(padx=10, pady=(5, 5))

    role_combobox = ttk.Combobox(register_window, values=["Karyawan", "Admin"], font=font_style, justify='center')
    role_combobox.pack(padx=10, pady=(0, 5))

    register_button = tk.Button(register_window, text="Register", command=register_action, font=font_style)
    register_button.pack(pady=(10, 50))

    register_window.mainloop()

# Fungsi untuk menampilkan menu utama
# Membuat tampilan awal
def mainwindow():
    main_window = tk.Tk()
    main_window.title("Absensi SDM")
    main_window.geometry("925x500+300+200")
    main_window.configure(bg="white")  # Set background color
    main_window.resizable(False,False)
    
    img = PhotoImage(file=r"C:\Users\denma\Desktop\Farrell\TELKOM\SMT 2\ALPRO\TUBES\login.png")
    Label(main_window,image=img,background="white").place(x=50,y=50)

    frame = tk.Frame(main_window, width=350, height=350, bg='white')
    frame.place(x=480,y=125)

    heading = tk.Label(frame,text="Silakan Absen", fg="#000080",bg="white",font=("Helvetica",23,"bold"))
    heading.place(x=100,y=5)
    

    register_button = tk.Button(frame, width=30, text="REGISTER", command=register_screen, font=("Helvetica",12,"bold"))
    register_button.pack(padx=60, pady=(50, 10))

    login_button = tk.Button(frame, width=30, text="LOGIN", command=login_screen, font=("Helvetica",12,"bold"))
    login_button.pack(padx=60, pady=10) 


    exit_button = tk.Button(frame, width=30, text="EXIT", command=main_window.destroy, font=("Helvetica",12,"bold"))
    exit_button.pack(padx=60, pady=10)


    main_window.mainloop()

mainwindow()