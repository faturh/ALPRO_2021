def fungsibesar(bil1,bil2,bil3): 
    if bil1 > bil2 and bil1 > bil3:
        return bil1
    elif bil1 < bil2 and bil2 > bil3:
        return bil2
    elif bil3 > bil1 and bil3 > bil2:
        return bil3
y = fungsibesar(12,32,100)
z = fungsibesar(1211,4158,9999)
print(f"angka terbesarnya adalah {y,z}")