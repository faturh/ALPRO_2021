def film (kelamin,umur):
          if (kelamin == "pria" and umur>= 17 ):
                    return "kamu hanya bisa menonton film sport"
          elif (kelamin == "pria" and umur>= 17 ):
                    return "anda belum cukup umur"
          elif (kelamin == "perempuan" and umur>= 17 ):
                    return "kamu hanya bisa menontonton drakor"
kelamin = input("masukan kelamin anda : ")
umur = int(input("masukan umur anda: "))
print(f"karena umur anda {umur} maka {film(kelamin,umur)}")
# print(y)