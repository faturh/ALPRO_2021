def aplikasiJNE (daerah,kg):
    if daerah == "jakarta" and kg:
        return kg*11000
    elif daerah == "semarang" and kg:
        return kg*15000
    elif daerah == "surabaya" and kg:
        return kg*20000
d = (input("masukan d anda : "))
k = (int(input("masukan k anda : ")))
# print(aplikasiJNE(d,k))
print(f"harga dari {d} dan berat nya {k} adalah {aplikasiJNE(d,k)}")














# x = aplikasiJNE ("jakarta",2)
# print(x)