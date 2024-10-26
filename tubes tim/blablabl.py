import mysql.connector
import tkinter as tk
# from tkinter import Tk
# import tkinter as ttk
# from PIL import ImageTk, Image
# import pwinput

root = tk.Tk()
root.title("Login")
root.geometry("925x500")
root.configure(bg="#fff")
root.resizable(False, False)
img = tk.PhotoImage(file="C:/Users/MSI/AppData/Local/Programs/Python/login.png")

tk.Label(root,image=img,bg="white").place(x=50,y=50)

frame=tk.Frame(root,width=350,height=350,bg="#F0F8FF")
frame.place(x=480,y=70)

heading=tk.Label(frame,text="Login", fg="#000080",bg="white",font=("Times New Roman",23,"bold"))
heading.place(x=100,y=5)

def on_enter(e):
    user.delete(0,"end")
def on_leave(e):
    nama=user.get()
    if nama=="":
        user.insert(0,"Username")
        
user = tk.Entry(frame,width=25,fg="black",border=0,bg="white",font=("Times New Roman",11))
user.place(x=30, y=80)
user.insert(0,"Username")
user.bind("<FocusIn>", on_enter)
user.bind("<FocusOut>", on_leave)

tk.Frame(frame,width=295, heigh=2, bg="black").place(x=25,y=107)
def on_enter_pass(e):
    passw.delete(0,"end")
    passw.config(show="*")
def on_leave_pass(e):
    nama=user.get()
    if nama=="":
        passw.insert(0,"password")
        
passw = tk.Entry(frame,width=25,fg="black",border=0,bg="white",font=("Times New Roman",11))
passw.place(x=30, y=150)
passw.insert(0,"password")
passw.bind("<FocusIn>", on_enter_pass)
passw.bind("<FocusOut>", on_leave_pass)

tk.Frame(frame,width=295, heigh=2, bg="black").place(x=25,y=177)

tk.Button(frame,width=39,pady=7,text="Login",bg="#4169E1",fg="white",border=0).place(x=35,y=204)
label=tk.Label(frame,text="Don't have an account?", fg="black",bg="white",font=("Times New Roman",9))
