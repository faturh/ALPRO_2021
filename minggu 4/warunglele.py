def show_menu():
    print("Selamat Datang")
    print("Daftar Menu:")
    print("\n1. Lele Goreng | Rp. 15.000,00")
    print("2. Ayam Goreng | Rp. 12.000,00")
    print("3. Bebek Goreng | Rp. 20.000,00")
    print("4. Keluar")

def select_menu():
    while True:
        try:
            menu = int(input("Masukkan nomor menu pilihan Anda: "))
            if menu not in [1, 2, 3, 4]:
                print("Pilihan menu tidak valid, silakan coba lagi!")
                continue
            else:
                break
        except ValueError:
            print("Input tidak valid, silakan masukkan nomor menu yang benar!")
    return menu

def select_quantity():
    while True:
        try:
            quantity = int(input("Masukkan jumlah pesanan Anda: "))
            if quantity <= 0:
                print("Jumlah pesanan harus lebih besar dari 0, silakan coba lagi!")
                continue
            else:
                break
        except ValueError:
            print("Input tidak valid, silakan masukkan jumlah pesanan yang benar!")
    return quantity

def calculate_price(menu, quantity):
    if menu == 1:
        price = 15000
    elif menu == 2:
        price = 12000
    elif menu == 3:
        price = 20000
    else:
        price = 0
    total_price = price * quantity
    return total_price

def show_message(menu, quantity, total_price):
    if menu == 1:
        menu_name = "Lele Goreng"
    elif menu == 2:
        menu_name = "Ayam Goreng"
    elif menu == 3:
        menu_name = "Bebek Goreng"
    else:
        menu_name = "tidak ada"
    print(f"Anda telah memesan {quantity} porsi {menu_name} dengan total harga Rp {total_price}")

def main():
    total = 0
    while True:
        show_menu()
        menu = select_menu()
        if menu == 4:
            print("Terima kasih telah menggunakan aplikasi kasir kami!")
            break
        quantity = select_quantity()
        total_price = calculate_price(menu, quantity)
        show_message(menu, quantity, total_price)
        total += total_price
        print(f"Total pembayaran sementara: Rp {total}")
    print(f"Total pembayaran Anda: Rp {total}")

    
if __name__ == "__main__":
    main()
