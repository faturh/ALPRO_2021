nama = input("Masukan nama anda : ")
f = open("file.txt","a")
f.write (f"halo {nama}")
f.close()

f = open("file.txt","r")
print(f.read())
f.close()
