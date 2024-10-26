from tkinter import *

p = Tk()
p.title("Kapitalisasi")
p.geometry()

def kapitalisasi_text():
    input_text = input_box1.get()
    output_text = input_text.upper()
    output_box.delete(1.0, END)
    output_box.insert(END, output_text)

input_label = Label(p, text="Input teks:")
input_label.grid(row=0, column=1, padx=5, pady=5)

input_box1 =Entry(p)
input_box1.grid(row=1, column=1, padx=5, pady=5)


output_label =Label(p, text="Output:")
output_label.grid(row=3, column=1, padx=5, pady=5)

input_box2 = Entry(p)
input_box2.grid(row=2, column=1, padx=5, pady=5)

output_box =Text(p)
output_box.grid(row=4, column=1, padx=5, pady=5)

kapitalisasi_button =Button(p, text="Kapitalisasi", command=kapitalisasi_text)
kapitalisasi_button.grid(row=3,column=1)

p.mainloop()
