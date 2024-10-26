from tkinter import *
from tkinter.ttk import *
from tkinter import messagebox
from PIL import Image, ImageTk

tp = Tk()
tp.geometry("900x500")
tp.title("PERCOBAAN (1)")
tp.configure(bg='#abcdef')

# gambar
bg = ImageTk.PhotoImage(file=("C:/Users/fikri/OneDrive/Desktop/file/COOLYEAHHH/ALPRO (Coding)/Untitled design(batu).png"))
my_label = Label(tp,image=bg)
my_label.place(x=0,y=0,relwidth=1,relheight=1)

# nama
nama = Label(tp, text= "Nama")
nama.grid(row=1, column=1,padx=5,pady=5)
inputnama = Entry(tp, width=30,background='white',foreground='red')
inputnama.grid(row=2, column=1,padx=5,pady=5)
inputnama.insert(0,"Masukan nama anda: ")

def tombol():
    nama = inputnama.get()
    salam = f"assalamualaikum {nama}"
    tplabel = Label(tp, text= salam)
    tplabel.grid(row=3, column=2,padx=5,pady=5)
    tplabel.config(text=salam)
    messagebox.showinfo("Data",f"nama: {nama} \n alamat: {inputalamat.get()}")

tombol1 = Button(tp, text="submit", command=tombol)
tombol1.grid(row=2, column=2,padx=5,pady=5)

# alamat
alamat = Label(tp, text="alamat")
alamat.grid(row=4, column=1,padx=5,pady=5)
inputalamat = Entry(tp, width=30,background='white',foreground='red')
inputalamat.grid(row = 5,column = 1,padx=5,pady=5)
inputalamat.insert(0,"Masukan alamat anda: ")

def Tombol2():
    alamat = inputalamat.get()
    fyi = f"Alamat anda : {alamat}"
    tplabel2 = Label(tp, text= fyi)
    tplabel2.grid(row=6, column=2,padx=5,pady=5)
    tplabel2.config(text=fyi)

tombol2 = Button(tp, text="submit", command=Tombol2)
tombol2.grid(row = 5, column = 2, padx=5, pady=5)

button_exit = Button(tp, text="Exit", command=tp.quit)
button_exit.grid(row=20, column=2,padx=5,pady=5)



tp.mainloop()