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

def set_color(self, color, element):
    """Atur warna elemen tertentu."""
    if color == 'Hitam':
        color_code = (0, 0, 0)
    elif color == 'Merah':
        color_code = (255, 0, 0)
    elif color == 'Biru':
        color_code = (0, 0, 255)
    elif color == 'Hijau':
        color_code = (0, 255, 0)
    elif color == 'Kuning':
        color_code = (255, 255, 0)

    if element == 'bg':
        self.bg_color = color_code
        screen.fill(color_code)
    elif element == 'box':
        self.box_color = color_code
        pygame.draw.rect(screen, color_code, box)
    elif element == 'ball':
        self.ball_color = color_code
        pygame.draw.circle(screen, color_code, (ball_x, ball_y), ball_radius)

def get_color_name(self, color):
    """Dapatkan nama warna berdasarkan kode warna RGB."""
    if color == (0, 0, 0):
        return 'Hitam'
    elif color == (255, 0, 0):
        return 'Merah'
    elif color == (0, 0, 255):
        return 'Biru'
    elif color == (0, 255, 0):
        return 'Hijau'
    elif color == (255, 255, 0):
        return 'Kuning'
# Buat objek Scoreboard
scoreboard = Scoreboard(root)
scoreboard.pack()

# Buat objek Menu
menu = Menu(root)

# Mulai game loop
running = True
while running:
          for event in pygame.event.get():
                    if event.type == pygame.QUIT:
                              running = False
          # Buat objek Scoreboard
          scoreboard = Scoreboard(root)
          scoreboard.pack()

          # Buat objek Menu
          menu = Menu(root)

          # Mulai game loop
          running = True
while running:
          for event in pygame.event.get():
                    if event.type == pygame.QUIT:
                              running = False
          # Gerakkan kotak dengan tombol arrow kiri dan kanan
          keys = pygame.key.get_pressed()
          if keys[pygame.K_LEFT] and box.x > 0:
                    box.x -= box_speed
          if keys[pygame.K_RIGHT] and box.x < SCREEN_WIDTH - box.width:
                    box.x += box_speed

          # Gerakkan bola ke bawah
          ball_y += ball_speed

          # Jika bola mencapai batas bawah layar, reset posisi bola
          if ball_y > SCREEN_HEIGHT:
                    ball_x = random.randint(0, SCREEN_WIDTH)
          ball_y = 0
          scoreboard.update_score()

          # Jika bola menyentuh kotak, reset posisi bola dan tambahkan skor
          if box.colliderect(pygame.Rect(ball_x - ball_radius, ball_y - ball_radius, ball_radius * 2, ball_radius * 2)):
                    ball_x = random.randint(0, SCREEN_WIDTH)
          ball_y = 0
          scoreboard.update_score()

# Gambar elemen game pada layar
screen.fill(BLACK)
pygame.draw.rect(screen, menu.box_color, box)
pygame.draw.circle(screen, menu.ball_color, (ball_x, ball_y), ball_radius)
scoreboard.update_score()

# Perbarui layar
pygame.display.update()
pygame.quit()
root.destroy()