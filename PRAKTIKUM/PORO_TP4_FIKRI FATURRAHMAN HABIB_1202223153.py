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
        self.root.title("Program CRUD Mahasiswa")

        # membuat frame untuk input data mahasiswa
        self.input_frame = LabelFrame(text=" Input Data Mahasiswa")
        self.input_frame.pack(side=LEFT, padx=20)

        # membuat widget untuk input nim
        self.nim = Label(self.input_frame, text= "nim : ")
        self.nim.grid(row=0, column=0, padx=5, pady=5, sticky=W)
        self.nim_entry = Entry(self.input_frame)
        self.nim_entry.grid(row=0, column=1, padx=5, pady=5)

        # membuat widget untuk input nama
        self.nama_label = Label(self.input_frame, text="nama :")
        self.nama_label.grid(row=1, column=0, padx=5, pady=5, sticky=W)
        self.nama_entry = Entry(self.input_frame)
        self.nama_entry.grid(row=1, column=1, padx=5, pady=5)

        # membuat widget untuk input alamat
        self.alamat_label = Label(self.input_frame, text="alamat :")
        self.alamat_label.grid(row=2, column=0, padx=5, pady=5, sticky=W)
        self.alamat_entry = Entry(self.input_frame)
        self.alamat_entry.grid(row=2, column=1, padx=5, pady=5)

        # membuat widget untuk input jurusan
        self.jurusan_label = Label(self.input_frame, text="jurusan :")
        self.jurusan_label.grid(row=3, column=0, padx=5, pady=5, sticky=W)
        self.jurusan_entry = Entry(self.input_frame)
        self.jurusan_entry.grid(row=3, column=1, padx=5, pady=5)

        # membuat frame untuk tombol aksi
        self.button_frame = Frame()
        self.button_frame.pack(side=LEFT, padx=20)

        # membuat tombol untuk menambahkan data
        self.add_button = Button(
            self.button_frame, text="Add", command=self.add_data
        )
        self.add_button.pack(fill=X, padx=5, pady=5)

        # membuat tombol untuk mengedit data
        self.edit_button = Button(
            self.button_frame, text="Edit", command=self.edit_data
        )
        self.edit_button.pack(fill=X, padx=5, pady=5)

        # Tombol Delete
        self.delete_button = Button(
            self.button_frame, text="Delete", command=self.delete_data
        )
        self.delete_button.pack(fill=X, padx=5, pady=5)

        # Tabel Data
        self.table_frame = Frame(self.root)
        self.table_frame.pack(fill=BOTH, padx=10, pady=10)

        self.tree = Treeview(
            self.table_frame,
            columns=("nim", "nama","alamat","jurusan"),
            show="headings",
        )
        self.tree.heading("nim", text="nim")
        self.tree.heading("nama", text="nama")
        self.tree.heading("alamat", text="alamat")
        self.tree.heading("jurusan", text="jurusan")
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
            NIM INTEGER PRIMARY KEY not null ,
            Nama TEXT not null,
            Alamat TEXT not null,
            Jurusan TEXT not null
            )"""
        # params = (nim, nama, alamat, jurusan)
        self.execute_query(query=query)

    def show_data(self):
        # Kosongkan tabel
        records = self.tree.get_children()
        for record in records:
            self.tree.delete(record)

        # Ambil data dari database dan tampilkan pada tabel
        query = "SELECT nim, nama, alamat, jurusan FROM Notes"
        data = self.execute_query(query).fetchall()
        for row in data:    
            self.tree.insert("", END, values=row)

    def add_data(self):
        # Ambil data dari input user
        nim = self.nim_entry.get()
        nama = self.nama_entry.get()
        alamat = self.alamat_entry.get()
        jurusan = self.jurusan_entry.get()

        # Cek apakah ada input yang kosong
        if nim == "" or nama == "" or alamat == "" or jurusan == "":
            messagebox.showerror("Error", "Mohon lengkapi semua input")
            return
        
        # Cek apakah nim sudah terdaftar
        query = "SELECT * FROM Notes WHERE nim=?"
        params = (nim,)
        result = self.execute_query(query, params).fetchone()
        if result is not None:
            messagebox.showerror("Error", "NIM sudah terdaftar")
            return

        # Insert data ke dalam database
        query = "INSERT INTO Notes (NIM,Nama,Alamat,Jurusan) VALUES (?, ?, ?, ?)"
        params = (nim,nama,alamat,jurusan)
        self.execute_query(query, params)

        # Bersihkan input setelah data ditambahkan ke dalam database
        self.nim_entry.delete(0, END)
        self.nama_entry.delete(0, END)
        self.alamat_entry.delete(0, END)
        self.jurusan_entry.delete(0, END)

        # Tampilkan data terbaru pada tabel
        self.show_data()

    def edit_data(self):
        # Ambil data dari input user
        nim = self.nim_entry.get()
        nama = self.nama_entry.get()
        alamat = self.alamat_entry.get()
        jurusan = self.jurusan_entry.get()

        # Ambil ID data yang akan di-update
        selected_item = self.tree.focus()
        values = self.tree.item(selected_item, "values")
        id = values[0]
        # Cek apakah ada input yang kosong
        if nim == "" or nama ==  "" or alamat == "" or jurusan == "":
            messagebox.showerror("Error", "Mohon lengkapi semua input")
            return
        # Cek apakah nim sudah terdaftar
        query = "SELECT * FROM Notes WHERE nim=?"
        params = (nim,)
        result = self.execute_query(query, params).fetchone()
        if result is not None:
            messagebox.showerror("Error", "NIM sudah terdaftar")
            return

        # Update data pada database
        query = "UPDATE Notes SET NIM=?, Nama=?, Alamat=?,Jurusan=? WHERE NIM=?"
        params = (nim,nama,alamat,jurusan, id)
        self.execute_query(query, params)

        # Tampilkan data terbaru pada tabel
        self.show_data()

        # Clear input fields
        self.clear_entries()

    def delete_data(self):
        # Ambil ID data yang akan dihapus
        selected_item = self.tree.focus()
        values = self.tree.item(selected_item, "values")
        id = values[0]

        # Hapus data dari database
        query = "DELETE FROM Notes WHERE NIM=?"
        params = (id,)
        self.execute_query(query, params)

        # Tampilkan data terbaru pada tabel
        self.show_data()

    def clear_entries(self):
        self.nim_entry.delete(0, END)
        self.nama_entry.delete(0, END)
        self.alamat_entry.delete(0, END)
        self.jurusan_entry.delete(0, END)
        self.show_data()

    def delete_data(self):
        if not self.tree.focus():
            messagebox.showwarning(
                title="Warning", message="Please select data to delete"
            )
            return

        result = messagebox.askquestion(
            title="Delete Confirmation", message="Are you sure to delete this data?"
        )
        if result == "yes":
            selected_item = self.tree.focus()
            nim = self.tree.item(selected_item)["values"][0]
            query = f"DELETE FROM Notes WHERE NIM = '{nim}'"
            self.execute_query(query=query)
            self.show_data()

    
if __name__ == "__main__": 
    app = Data(root=Tk()) 
    app.root.mainloop()