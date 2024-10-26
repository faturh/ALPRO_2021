from tkinter import *
import sqlite3


p = Tk()
p.title('cek prima')

db_name = "database.db"
def create ():
    conn = sqlite3.connect()
    cur = conn.cursor()
    cur.execute('''CREATE TABLE IF NOT EXISTS bilangan_prima
    prima INTEGER NOT NULL PRIMARY KEY,
    '''
    )
    conn.commit()
    conn.close()

inputan = Entry(p, width=35,borderwidth=5)
inputan.grid(row=0,column=0,columnspan=3,padx=10,pady=10)

def cek_prima():
    inputan_1 = int(inputan.get())
    if inputan_1 > 1:
        for i in range(2, inputan_1):
            if inputan_1 % i == 0:
                hasil_label = Label(p,text='')
                hasil_label.grid(row=2, column=0,padx=5,pady=5)
                hasil_label.config(text=f"{inputan_1} bukan bilangan prima")
                break
        else:
            hasil_label = Label(p,text='')
            hasil_label.grid(row=3, column=0,padx=5,pady=5)
            hasil_label.config(text=f"{inputan_1} adalah bilangan prima")
    else:
        hasil_label = Label(p,text='')
        hasil_label.grid(row=3, column=0,padx=5,pady=5)
        hasil_label.config(text=f"{inputan_1} bukan bilangan prima")

button_1 = Button(p,text='cek bilangan prima',padx=5,pady=5,command=cek_prima)
button_1.grid(row=1,column=1)
def insert_data():
    input_bilangan = inputan.get()
    conn = sqlite3.connect("database.db")
    curr = conn.cursor()
    curr.execute('INSERT INTO bilangan_prima VALUES (inputan)')
    query = "INSERT INTO Notes (NIM,Nama,Alamat,Jurusan) VALUES (?"
    params = (inputan_bilangan)


def show_data():
    data = 

button_2 = Button(p,text='cek bilangan prima',padx=5,pady=5,command=cek_prima)
button_2.grid(row=2,column=1)


p.mainloop()