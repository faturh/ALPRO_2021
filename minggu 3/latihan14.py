# mencari nilai terbesar
#pakai input
def fungsibesar(bil1,bil2): 
    if bil1>=bil2 :
        return bil1
    elif bil1<=bil2:
        return bil2
bilangan1 = int(input("Masukan bilangan 1 = "))
bilangan2 = int(input("Masukan bilangan 2 = "))
print(f"angka terbesar dari {bilangan1} dan {bilangan2} adalah {fungsibesar(bilangan1,bilangan2)}")

print(40*"=")

def fungsibesar(bil1,bil2): 
    if bil1>=bil2 :
        return bil1
    elif bil1<=bil2:
        return bil2
x = fungsibesar(20,45)
y = fungsibesar(12,32)
z = fungsibesar(1211,4158)
print(f"angka terbesarnya adalah {x,y,z}")