import sqlite3
import tkinter as tk
from tkinter import ttk
from tkinter.messagebox import showinfo
DATABASE_FILE = "DBA.sqlite3"

tampilan = tk.Tk()
tampilan.title('Program CRUD Mahasiswa')
tampilan.configure(bg = 'white')
tampilan.geometry('1000x300')


def create_table():
          conn = sqlite3.connect(DATABASE_FILE)
          cur = conn.cursor()
          cur.execute('''CREATE TABLE IF NOT EXISTS data_mahasiswa(
          NIM INTEGER NOT NULL PRIMARY KEY, 
          Nama TEXT NOT NULL, 
          Jurusan TEXT NOT NULL,
          Alamat TEXT NOT NULL,)''')
          conn.commit()
          conn.close()  

input_frame = ttk.Frame(tampilan)
input_frame.pack(padx=0,fill ='x',expand=True)

judul = ttk.Label(input_frame,text='Input Data Mahasiswa')
judul.pack(padx=0,fill ='x',expand=True)

input_NIM = ttk.Label(input_frame,text = 'NIM : ')
input_NIM.pack(padx=0,fill ='x',expand=True)
MASUKAN_NIM =tk.StringVar()
masukan_NIM = ttk.Entry(input_frame,textvariable=MASUKAN_NIM)
masukan_NIM.pack(padx=30,pady=30,fill ='both',expand=True)

input_nama = ttk.Label(input_frame,text = 'Nama : ')
input_nama.pack(padx=1,fill ='x',expand=True)
MASUKAN_NAMA =tk.StringVar()
masukan_nama = ttk.Entry(input_frame,textvariable=MASUKAN_NAMA)
masukan_nama.pack(padx=1,fill ='x',expand=True)

input_alamat = ttk.Label(input_frame,text = 'Alamat : ')
input_alamat.pack(padx=2,fill ='x',expand=True)
MASUKAN_ALAMAT =tk.StringVar()
masukan_ALAMAT = ttk.Entry(input_frame,textvariable=MASUKAN_ALAMAT)
masukan_ALAMAT.pack(padx=2,fill ='x',expand=True)

input_jurusan = ttk.Label(input_frame,text = 'Jurusan : ')
input_jurusan.pack(padx=3,fill ='x',expand=True)
MASUKAN_JURUSAN =tk.StringVar()
masukan_JURUSAN = ttk.Entry(input_frame,textvariable=MASUKAN_JURUSAN)
masukan_JURUSAN.pack(padx=3,fill ='x',expand=True)

def tombol_submit():
    print(MASUKAN_NIM.get(),'|',MASUKAN_NAMA.get(),'|',MASUKAN_ALAMAT.get(),'|',MASUKAN_JURUSAN.get())

tombol = ttk.Button(input_frame,text= 'Submit',command= tombol_submit)
tombol.pack(fill='x',expand=True,padx=10,pady=10)

def tombol_delete():
       print()
       

tombol = ttk.Button(input_frame,text= 'dekete',command= tombol_delete)
tombol.pack(fill='x',expand=True,padx=10,pady=10)



tampilan.mainloop()












                    



















                    
                    
                    
                    
                    