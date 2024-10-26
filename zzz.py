import tkinter as tk
from tkinter import messagebox
from random import randint

class Button:
    def __init__(self, value, x, y, width, height, color, master):
        self.value = value
        self.selected = False
        self.color = color
        self.master = master
        self.button = tk.Button(master, text=str(value), command=self.toggle_select, width=width, height=height)
        self.button.place(x=x, y=y)
        self.update_color()

    def toggle_select(self):
        self.selected = not self.selected
        self.update_color()

    def update_color(self):
        if self.selected:
            self.button.configure(bg=self.color, activebackground=self.color)
        else:
            self.button.configure(bg="white", activebackground=self.color)

class Game:
    def __init__(self, master):
        self.master = master
        self.target_number = 0
        self.total_buttons = 4
        self.buttons = []
        self.clicks = 0
        self.create_buttons()
        self.create_target_number_label()
        self.create_reset_button()

    def create_buttons(self):
        for i in range(self.total_buttons):
            button_width = 6
            button_height = 3
            button_x = 100 + i*100
            button_y = 150
            button_color = "blue"
            button_value = randint(1, 9)
            button = Button(button_value, button_x, button_y, button_width, button_height, button_color, self.master)
            self.buttons.append(button)

    def create_target_number_label(self):
        self.target_number = randint(10, 40)
        target_number_label = tk.Label(self.master, text=f"Target number: {self.target_number}", font=("Arial", 20))
        target_number_label.place
        # menempatkan label untuk bilangan sasaran di atas layar permainan
        target_number_label = tk.Label(
            self.window, text="Target: " + str(self.target_number), font=("Arial", 18))
        target_number_label.place(x=10, y=10)

        # membuat label untuk menampilkan jumlah klik pemain
        clicks_label = tk.Label(
            self.window, text="Clicks: " + str(self.clicks), font=("Arial", 18))
        clicks_label.place(x=300, y=10)

        # membuat label untuk menampilkan hasil penjumlahan
        sum_label = tk.Label(
            self.window, text="Sum: " + str(self.current_sum), font=("Arial", 18))
        sum_label.place(x=10, y=60)

        # membuat tombol untuk reset permainan
        reset_button = tk.Button(
            self.window, text="Reset", command=self.reset_game, font=("Arial", 18))
        reset_button.place(x=300, y=60)

        # membuat daftar tombol untuk angka
        number_buttons = []
        for i in range(10):
            number_buttons.append(tk.Button(
                self.window, text=str(i), command=lambda i=i: self.number_button_clicked(i), font=("Arial", 18)))

        # menempatkan tombol angka pada layar permainan
        for i in range(1, 10):
            number_buttons[i].place(x=20+60*((i-1) % 3), y=150+60*((i-1)//3))
        number_buttons[0].place(x=80, y=390)

        # menampilkan layar permainan
        self.window.mainloop()
