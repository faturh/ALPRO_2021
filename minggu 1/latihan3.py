idmu = "si"
pwmu = "HEI"
while True :
          username = input("Masukan username anda : ")
          password = input("Masukan password anda : ")
          if username == idmu and password == pwmu :
                    print ("Selamat datang di aplikasi SI")
                    break
          elif username != idmu and password == pwmu :
                    print ("username anda salah, coba lagi!")
          elif username == idmu and password != pwmu :
                    print ("password anda salah, coba lagi!")
          else : 
                    print ("USERNAME DAN PASSWORD ANDA SALAH")