dm =["putu","raihan","ican","dery","andi"]
uts =[90,75,80,85,40]
uas =[85,60,85,85,50]
max_temp = 0
min_temp = 0
for i in range (len(dm)) :
    final = 0.4*uts[i]+0.6*uas[i]
    print("nilai akhir",dm[i],"adalah ",final)
    if(final > max_temp):
        max_temp = final
    else :
        min_temp = final
# for x in range(0, len(uas)):
#     #perhitungan final di sini 
#     final = 0.4*uts[x]+0.6*uas[x]
#     print("nilai akhir",dm[x],"adalah ",final)
print(f"\nnilai tertinggi adalah : {max_temp}")
print(f"nilai terendah adalah : {min_temp}")


