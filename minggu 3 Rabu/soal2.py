def jarakanda (kelamin,jarakk):
        if kelamin == "perempuan" and jarakk >= 100 :
                return "LULUS"
        elif kelamin == "pria" and jarakk >= 200 :
                return "lulus"
        elif kelamin=="pria" and jarakk <= 200 :
                return "Tidak lulus"
        elif kelamin=="perempuan" and jarakk <= 100 :
                return "Tidak lulus"
kelamin = input("masukan jenis kelamin anda :")
jarak  = int(input("massukan jarak anda :"))
print(f"jarak anda {jarakanda(kelamin,jarak)}")
