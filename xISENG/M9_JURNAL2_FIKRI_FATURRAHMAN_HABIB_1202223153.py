# FIKRI FATURRAHMAN HABIB
# 1202223153
# SI4605
from tkinter import *
import sqlite3
from tkinter.ttk import *
from tkinter import messagebox
# from PIL import Image, ImageTk


class Data:
    db_name = "data.db"

    def __init__(self, root):
        self.root = root
        self.root.title("Daftar buku")

        self.input_frame = LabelFrame(text=" Input Data Mahasiswa")
        self.input_frame.pack(side=LEFT, padx=20)

        self.Judul = Label(self.input_frame, text= "Judul : ")
        self.Judul.grid(row=0, column=0, padx=5, pady=5, sticky=W)
        self.Judul_entry = Entry(self.input_frame)
        self.Judul_entry.grid(row=0, column=1, padx=5, pady=5)

        self.Pengarang_label = Label(self.input_frame, text="Pengarang :")
        self.Pengarang_label.grid(row=1, column=0, padx=5, pady=5, sticky=W)
        self.Pengarang_entry = Entry(self.input_frame)
        self.Pengarang_entry.grid(row=1, column=1, padx=5, pady=5)

        self.Tahun_terbit_label = Label(self.input_frame, text="Tahun terbit :")
        self.Tahun_terbit_label.grid(row=2, column=0, padx=5, pady=5, sticky=W)
        self.Tahun_terbit_entry = Entry(self.input_frame)
        self.Tahun_terbit_entry.grid(row=2, column=1, padx=5, pady=5)

        # membuat frame untuk tombol aksi
        self.button_frame = Frame()
        self.button_frame.pack(side=LEFT, padx=20)

        # membuat tombol untuk menambahkan data
        self.add_button = Button(
            self.button_frame, text="simpan", command=self.add_data
        )
        self.add_button.pack(fill=X, padx=5, pady=5)


        self.tree = Treeview(
            self.table_frame,
            columns=("Judul", "Pengarang","Tahun_Terbit"),
            show="headings",
        )
        self.tree.heading("Judul", text="Judul")
        self.tree.heading("Pengarang", text="Pengarang")
        self.tree.heading("Tahun_Terbit", text="Tahun_Terbit")
        self.tree.pack(fill=BOTH, expand=True)

        # Panggil fungsi untuk menampilkan data pada tabel
        self.create_table()       
        self.show_data()

        def on_close():
            response=messagebox.askyesno('Exit','Are you sure you want to exit?')
            if response:
                self.root.destroy()

        self.root.protocol('WM_DELETE_WINDOW', on_close)

    def run(self):
        self.root.mainloop()

    def execute_query(self, query, params=()):
        with sqlite3.connect(self.db_name) as conn:
            cursor = conn.cursor()
            result = cursor.execute(query, params)
            conn.commit()
        return result

    def create_table(self):
        # Kolom Tabel
        query = """CREATE TABLE IF NOT EXISTS Notes (
            Judul INTEGER PRIMARY KEY not null ,
            Pengarang TEXT not null,
            Tahun_Terbit TEXT not null
            )"""
        # params = (Judul, Pengarang, Tahun_Terbit )
        self.execute_query(query=query)

    def show_data(self):
        # Kosongkan tabel
        records = self.tree.get_children()
        for record in records:
            self.tree.delete(record)

        # Ambil data dari database dan tampilkan pada tabel
        query = "SELECT Judul, Pengarang, Tahun_Terbit,  FROM Notes"
        data = self.execute_query(query).fetchall()
        for row in data:    
            self.tree.insert("", END, values=row)

    def add_data(self):
        # Ambil data dari input user
        Judul = self.Judul_entry.get()
        Pengarang = self.Pengarang_entry.get()
        Tahun_Terbit = self.Tahun_Terbit_entry.get()

        # Cek apakah ada input yang kosong
        if Judul == "" or Pengarang == "" or Tahun_Terbit == "" :
            messagebox.showerror("Error", "Mohon lengkapi semua input")
            return
        
        # Cek apakah Judul sudah terdaftar
        query = "SELECT * FROM Notes WHERE Judul=?"
        params = (Judul,)
        result = (query, params).fetchone()
        if result is not None:
            messagebox.showerror("Error", "Judul sudah terdaftar")
            return

        # Insert data ke dalam database
        query = "INSERT INTO Notes (Judul,Pengarang,Tahun_Terbit,) VALUES (?, ?, ?)"
        params = (Judul,Pengarang,Tahun_Terbit,)
        self.execute_query(query, params)

        # Bersihkan input setelah data ditambahkan ke dalam database
        self.Judul_entry.delete(0, END)
        self.Pengarang_entry.delete(0, END)
        self.Tahun_Terbit_entry.delete(0, END)
        self._entry.delete(0, END)

        # Tampilkan data terbaru pada tabel
        self.show_data()

    
if __name__ == "__main__": 
    app = Data(root=Tk()) 
    app.root.mainloop()