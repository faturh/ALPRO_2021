def fungsibesar(bil1,bil2,bil3): 
    if bil1 > bil2 and bil1 > bil3:
        return bil1
    elif bil1 < bil2 and bil2 > bil3:
        return bil2
    elif bil3 > bil1 and bil3 > bil2:
        return bil3
x = fungsibesar(45,12,67)
y = fungsibesar(15,92,37)
print(f"angka terbesarnya adalah {x,y}")