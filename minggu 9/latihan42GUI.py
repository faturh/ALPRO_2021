import tkinter as tk
import tkinter
from tkinter import messagebox
import mysql.connector

mydb = mysql.connector.connect(
  host="localhost",
  user="root",
  password="",
  database="warung putuu",
  port ="3308"
)
# F itu buat window awal harus selalu dipakai seperti variabel
f = tkinter.Tk()
f.title("Aplikasi Data Mahasiswa")
f.geometry('1000x300')

# Label untuk membedakan nama input
# Entry supaya bisa input
labelNama = tk.Label(f, text='Nama',font='verdana')
labelNama.pack(pady=2)
textnama = tk.Entry(f, width=40,bg='black',fg='white')
textnama.pack(pady=2)

labelNIM = tk.Label(f, text='NIM',font='verdana')
labelNIM.pack(pady=2)
textNIM = tk.Entry(f, width=40,bg='black',fg='white')
textNIM.pack(pady=2)

labelAlamat = tk.Label(f,text='Alamat',font='verdana')
labelAlamat.pack(pady=2)
textAlamat = tk.Entry(f, width=40,bg='black',fg='white')
textAlamat.pack(pady=2)
# textAlamat = tk.Text(f,height=3,width='40') 
# textAlamat.pack(pady=2)
# tk.Text itu buat kolom nya jadi besar

def displaytestmessage():
    nama = textnama.get()
    print(f"HEHEH {nama}")
    messagebox.showinfo('fyi aja y',f'cuma mau ngetest aja ya {nama} kalo button nya di klick')
# Button buat tombol
button1 = tk.Button(f, width = 40, text= "klik saya untuk nama",command= displaytestmessage)
button1.pack(pady =2)

labelHasil = tk.Label(text="")
labelHasil.pack(pady=2)

def simpandata():
    nama= textnama.get()
    nim = textNIM.get()
    alamat = textAlamat.get()
    print(f"Simpan data dengan NIM {nama}")
    labelHasil.config(text=nama)
    mycursor = mydb.cursor()
    sql = "INSERT INTO barang (id_Barang,nama_Barang,harga_Barang) VALUES (%s,%s,%s)"
    val = (nama,nim,alamat)
    mycursor.execute(sql, val)
    mydb.commit()
#     if nama == nama and nim == nim and alamat == alamat:
#           messagebox.showinfo("data telah ditambahkan Ke DB: ",f"nama anda adalah: {nim}")

button2 = tk.Button(f, width = 40, text= "klik saya lagi untuk simpan ke DB",command=simpandata)
button2.pack(pady =2)


# button3 = tk.Button(f, width = 40, text= "klik saya lagi untuk Alamat",command=displaytestmessage)
# button3.pack(pady =2)

f.mainloop()  