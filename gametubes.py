import tkinter as tk
import pygame
import random
import tkinter.messagebox as mbox

SCREEN_WIDTH = 400
SCREEN_HEIGHT = 400
BLACK = (0, 0, 0)

# Buat objek tkinter root
root = tk.Tk()
root.geometry(f"{SCREEN_WIDTH}x{SCREEN_HEIGHT}")
root.title("Game with GUI")

# Buat objek pygame
pygame.init()
screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
pygame.display.set_caption("Game with GUI")

# Buat kotak yang bisa digerakkan oleh user
box = pygame.Rect(SCREEN_WIDTH // 2 - 25, SCREEN_HEIGHT - 50, 50, 50)
box_speed = 10

# Inisialisasi bola
ball_x = random.randint(0, SCREEN_WIDTH)
ball_y = 0
ball_radius = 10
ball_speed = 5

class Scoreboard(tk.Frame):
    def __init__(self, master):
        super().__init__(master)

        # Skor awal
        self.score = 0

        # Tampilan skor
        self.score_label = tk.Label(self, text=f"Score: {self.score}")
        self.score_label.pack()

    def update_score(self):
        self.score += 1
        self.score_label.config(text=f"Score: {self.score}")

class Menu(tk.Menu):
    def __init__(self, master):
        super().__init__(master)
        self.master = master

        # Buat menu bar
        self.menu_bar = tk.Menu(self.master)

        # Buat menu play
        self.play_menu = tk.Menu(self.menu_bar, tearoff=0)
        self.play_menu.add_command(label="Play", command=self.play_game)
        self.menu_bar.add_cascade(label="Play", menu=self.play_menu)

        # Buat menu setting
        self.setting_menu = tk.Menu(self.menu_bar, tearoff=0)
        self.setting_menu.add_command(label="Background Color", command=self.set_bg_color)
        self.setting_menu.add_command(label="Box Color", command=self.set_box_color)
        self.setting_menu.add_command(label="Ball Color", command=self.set_ball_color)
        self.menu_bar.add_cascade(label="Setting", menu=self.setting_menu)

        # Buat menu exit
        self.exit_menu = tk.Menu(self.menu_bar, tearoff=0)
        self.exit_menu.add_command(label="Exit", command=self.exit_game)
        self.menu_bar.add_cascade(label="Exit", menu=self.exit_menu)

        # Atur menu bar pada objek root
        self.master.config(menu=self.menu_bar)

    def play_game(self):
        mbox.showinfo("Game Started", "Enjoy the game!")

    def set_bg_color(self):
        color = mbox.askcolor(title="Choose background color")[1]
        screen.fill(color)

    def set_box_color(self):
        color = mbox.askcolor(title="Choose box color")[1]
        pygame.draw.rect(screen, color, box)

    def set_ball_color(self):
        color = mbox.askcolor(title="Choose ball color")[1]
        pygame.draw.circle(screen, color, (ball_x, ball_y), ball_radius)

def exit_game(self):
    """Keluar dari game."""
    confirm_exit = mbox.askquestion("Konfirmasi Keluar", "Apakah Anda yakin ingin keluar dari game?")
    if confirm_exit == 'yes':
        pygame.quit()
        root.destroy()
        exit()

def open_settings(self):
    """Buka jendela pengaturan."""
    settings_window = tk.Toplevel(self)
    settings_window.title("Pengaturan")

    # Buat daftar warna yang dapat dipilih
    color_options = ['Hitam', 'Merah', 'Biru', 'Hijau', 'Kuning']

    # Buat variabel tkinter untuk masing-masing pilihan warna
    bg_color_var = tk.StringVar(value=self.get_color_name(self.bg_color))
    box_color_var = tk.StringVar(value=self.get_color_name(self.box_color))
    ball_color_var = tk.StringVar(value=self.get_color_name(self.ball_color))

    # Buat label dan option menu untuk memilih warna latar belakang
    bg_color_label = tk.Label(settings_window, text="Warna Latar Belakang:")
    bg_color_label.grid(row=0, column=0, padx=5, pady=5, sticky="W")
    bg_color_option = tk.OptionMenu(settings_window, bg_color_var, *color_options, command=lambda color: self.set_color(color, 'bg'))
    bg_color_option.grid(row=0, column=1, padx=5, pady=5, sticky="W")

    # Buat label dan option menu untuk memilih warna kotak
    box_color_label = tk.Label(settings_window, text="Warna Kotak:")
    box_color_label.grid(row=1, column=0, padx=5, pady=5, sticky="W")
    box_color_option = tk.OptionMenu(settings_window, box_color_var, *color_options, command=lambda color: self.set_color(color, 'box'))
    box_color_option.grid(row=1, column=1, padx=5, pady=5, sticky="W")

    # Buat label dan option menu untuk memilih warna bola
    ball_color_label = tk.Label(settings_window, text="Warna Bola:")
    ball_color_label.grid(row=2, column=0, padx=5, pady=5, sticky="W")
    ball_color_option = tk.OptionMenu(settings_window, ball_color_var, *color_options, command=lambda color: self.set_color(color, 'ball'))
    ball_color_option.grid(row=2, column=1, padx=5, pady=5, sticky="W")

    # Buat tombol "Simpan" untuk menyimpan pengaturan warna
    save_button = tk.Button(settings_window, text="Simpan", command=settings_window.destroy)
    save_button.grid(row=3, column=1, padx=5, pady=5, sticky="E")

def set_color(self, color_name, color_type):
    """Mengubah warna sesuai dengan pilihan pengguna."""
    color_dict = {
        'Hitam': BLACK,
        'Merah': RED,
        'Biru': BLUE,
        'Hijau': (0, 255, 0),
        'Kuning': (255, 255, 0)
    }
    color = color_dict[color_name]
    if color_type == 'bg':
        self.bg_color = color
        screen.fill(self.bg_color)
    elif color_type == 'box':
        self.box_color = color
    elif color_type == 'ball':
        self.ball_color = color

    def get_color_name(self, color):
        """
        Mengembalikan nama warna berdasarkan tuple RGB-nya.
        """
        # Daftar warna yang didukung beserta nama mereka
        colors = {
            (0, 0, 0): "Black",
            (255, 0, 0): "Red",
            (0, 0, 255): "Blue",
            (0, 255, 0): "Green",
            (255, 255, 0): "Yellow",
            (255, 255, 255): "White"
        }

        # Cari warna yang cocok dan kembalikan namanya
        for rgb, name in colors.items():
            if color == rgb:
                return name

        # Jika tidak ada warna yang cocok, kembalikan string kosong
        return ""
    def show_color_settings(self):
        """
        Menampilkan dialog pengaturan warna.
        """
        # Buat dialog pengaturan warna
        color_dialog = tk.Toplevel(self)
        color_dialog.title("Color Settings")
        color_dialog.geometry("300x200")

        # Buat label untuk setiap warna
        bg_label = tk.Label(color_dialog, text="Background Color:")
        bg_label.grid(row=0, column=0, padx=10, pady=10)
        ball_label = tk.Label(color_dialog, text="Ball Color:")
        ball_label.grid(row=1, column=0, padx=10, pady=10)
        box_label = tk.Label(color_dialog, text="Box Color:")
        box_label.grid(row=2, column=0, padx=10, pady=10)

        # Buat tombol untuk memilih warna
        bg_color_btn = tk.Button(color_dialog, text="Choose Color", command=lambda: self.change_color("background"))
        bg_color_btn.grid(row=0, column=1)
        ball_color_btn = tk.Button(color_dialog, text="Choose Color", command=lambda: self.change_color("ball"))
        ball_color_btn.grid(row=1, column=1)
        box_color_btn = tk.Button(color_dialog, text="Choose Color", command=lambda: self.change_color("box"))
        box_color_btn.grid(row=2, column=1)

        # Buat tombol untuk menutup dialog
        close_btn = tk.Button(color_dialog, text="Close", command=color_dialog.destroy)
        close_btn.grid(row=3, column=1, pady=20)
def exit_game(self):
    # Menampilkan messagebox konfirmasi exit
    response = mbox.askyesno("Konfirmasi", "Apakah anda yakin ingin keluar?")
    if response:
        pygame.quit()
        root.destroy()
        exit()
# Buat objek SettingMenu
setting_menu = open_settings(root)

# Buat menu bar
menubar = tk.Menu(root)

# Buat menu "File"
filemenu = tk.Menu(menubar, tearoff=0)
filemenu.add_command(label="Play", command=start_game)
filemenu.add_command(label="Exit", command=setting_menu.exit_game)
menubar.add_cascade(label="File", menu=filemenu)

# Buat menu "Settings"
settingsmenu = tk.Menu(menubar, tearoff=0)
settingsmenu.add_command(label="Background color", command=setting_menu.change_bg_color)
settingsmenu.add_command(label="Ball color", command=setting_menu.change_ball_color)
settingsmenu.add_command(label="Box color", command=setting_menu.change_box_color)
menubar.add_cascade(label="Settings", menu=settingsmenu)

# Tampilkan menu bar
root.config(menu=menubar)

# Jalankan mainloop
root.mainloop()