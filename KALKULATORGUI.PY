from tkinter import *
from PIL import Image, ImageTk

c = Tk()
c.title("Kalkulator")
c.geometry('380x360')

bg = ImageTk.PhotoImage(file=("C:/Users/fikri/OneDrive/Desktop/file/COOLYEAHHH/ALPRO (Coding)/Untitled design(batu).png"))
my_label = Label(c,image=bg)
my_label.place(x=0,y=0,relwidth=1,relheight=1)

inputan = Entry(c, width=35,borderwidth=5)
inputan.grid(row=0,column=0,columnspan=3,padx=10,pady=10)

def button_add(number):
    current = inputan.get()
    inputan.delete(0,END)
    inputan.insert(0,str(current) + str(number))

def plus_input():
    first_number=inputan.get()
    global f_num
    global math
    math = "addition"
    f_num = int(first_number)
    inputan.delete(0,END)

def minus_input():
    first_number=inputan.get()
    global f_num
    global math
    math = "subtraction"
    f_num = int(first_number)
    inputan.delete(0,END)

def divide_input():
    first_number=inputan.get()
    global f_num
    global math
    math = "division"
    f_num = int(first_number)
    inputan.delete(0,END)

def multiply_input():
    first_number=inputan.get()
    global f_num
    global math
    math = "multiplication"
    f_num = int(first_number)
    inputan.delete(0,END)

def sama_dengan_input():
    second_number = inputan.get()
    inputan.delete(0,END)
    if math == "addition":
        inputan.insert(0,f_num + int(second_number))
    if math == "subtraction":   
        inputan.insert(0,f_num - int(second_number))
    if math == "multiplication":
        inputan.insert(0,f_num * int(second_number))
    if math == "division":
        inputan.insert(0,f_num / int(second_number))

def clear_input():
    inputan.delete(0,END)

button_1 = Button(c,text='1',padx=40,pady=20,command=lambda: button_add(1))
button_2 = Button(c,text='2',padx=40,pady=20,command=lambda: button_add(2))
button_3 = Button(c,text='3',padx=40,pady=20,command=lambda: button_add(3))
button_4 = Button(c,text='4',padx=40,pady=20,command=lambda: button_add(4))
button_5 = Button(c,text='5',padx=40,pady=20,command=lambda: button_add(5))
button_6 = Button(c,text='6',padx=40,pady=20,command=lambda: button_add(6))
button_7 = Button(c,text='7',padx=40,pady=20,command=lambda: button_add(7))
button_8 = Button(c,text='8',padx=40,pady=20,command=lambda: button_add(8))
button_9 = Button(c,text='9',padx=40,pady=20,command=lambda: button_add(9))
button_0 = Button(c,text='0',padx=40,pady=20,command=lambda: button_add(0))

button_plus = Button(c,text='+',padx=39,pady=20,command=plus_input)
button_equal = Button(c,text='=',padx=39,pady=20,command=sama_dengan_input)
button_minus = Button(c,text='-',padx=39,pady=20,command=minus_input)
button_bagi = Button(c,text='/',padx=39,pady=20,command=divide_input)
button_kali = Button(c,text='x',padx=39,pady=20,command=multiply_input)
button_clear = Button(c,text='C',padx=39,pady=20,command=clear_input)

button_1.grid(row=3,column=0)
button_2.grid(row=3,column=1)
button_3.grid(row=3,column=2)

button_4.grid(row=2,column=0)
button_5.grid(row=2,column=1)
button_6.grid(row=2,column=2)

button_7.grid(row=1,column=0)
button_8.grid(row=1,column=1)
button_9.grid(row=1,column=2)

button_0.grid(row=4,column=0)
button_plus.grid(row=1,column=3)
button_minus.grid(row=2,column=3)
button_clear.grid(row=4,column=1)
button_bagi.grid(row=3,column=3)
button_kali.grid(row=4,column=3)
button_equal.grid(row=4,column=2)

c.mainloop()