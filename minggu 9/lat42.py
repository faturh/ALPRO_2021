import tkinter
import tkinter as tk
from tkinter import messagebox
import mysql.connector

mydb = mysql.connector.connect(
  host="localhost",
  user="root",
  password="",
  database="warungputuu",
  port ="3308"
)

f = tkinter.Tk()

f.title("Aplikasi Data Mahasiswa")
f.geometry("300x350")

labelNama = tk.Label(f,text="Nama")
labelNama.pack(pady=2)

txtnama = tk.Entry(f, width=35)
txtnama.pack(pady=2)

labelNIM = tk.Label(f,text="NIM")
labelNIM.pack(pady=2)

txtNIM = tk.Entry(f, width=35)
txtNIM.pack(pady=2)

labelAlamat = tk.Label(f, text="Alamat", font="Verdana")
labelAlamat.pack(pady=2)

txtAlamat = tk.Text(f,height=3, width=35)
txtAlamat.pack(pady=2)

labelHasil = tk.Label(f, text="")
labelHasil.pack(pady=2)

# ini buat insert data ke database
# mycursor = mydb.cursor()
# sql = "INSERT INTO barang (id_Barang,Nama_Barang,Harga_Barang) VALUES (%s,%s,%s)"
# values = (3,"nasi", "5000")
# mycursor.execute(sql, values)
# mydb.commit()
def simpan():
    nama = txtnama.get()
    nim = txtNIM.get()
    alamat=txtAlamat.get()
    print("Simpan data dengan nama ", nama)
    labelHasil.config(text=nama)
    mycursor = mydb.cursor()
    sql = "INSERT INTO barang (id_Barang,nama_Barang,harga_Barang) VALUES (%s,%s,%s)"
    val = (nama,nim,alamat)
    mycursor.execute(sql, val)
    mydb.commit()
    messagebox.showinfo("Sukses", "Simpan data berhasil!")

button1 = tk.Button(f, width=35, text="SIMPAN", command=simpan)
button1.pack(pady=2) 
#padding y : membeirkan jarak ke sumbu y (atas dan bawah sebesar 100 pixel)

def displaytestmessage():
    print("testing saja")
    messagebox.showinfo("Info ajah", "Ini hanya test ketika diklik")

button2 = tk.Button(f, width=35, text="TEST", command=displaytestmessage)
button2.pack(pady=2) 
f.mainloop()